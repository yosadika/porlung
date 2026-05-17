import numpy as np
import pandas as pd


def estimate_sampling_rate(df: pd.DataFrame) -> float:
    """
    Mengestimasi sampling rate dari kolom time.
    """
    time = df["time"].values

    if len(time) < 2:
        raise ValueError("Data time terlalu pendek untuk estimasi sampling rate.")

    dt = np.median(np.diff(time))

    if dt <= 0:
        raise ValueError("Kolom time tidak valid.")

    return 1.0 / dt


def calculate_rms_sliding(signal: np.ndarray, samples_per_cycle: int) -> np.ndarray:
    """
    Menghitung RMS sliding window 1 siklus.
    Output dibuat sepanjang input dengan padding NaN di awal.
    """
    signal = np.asarray(signal, dtype=float)

    if samples_per_cycle < 2:
        raise ValueError("samples_per_cycle terlalu kecil.")

    rms = np.full(len(signal), np.nan)

    if len(signal) <= samples_per_cycle:
        return rms

    squared = signal ** 2
    cumulative = np.concatenate([[0.0], np.cumsum(squared)])
    window_energy = (
        cumulative[samples_per_cycle:len(signal)]
        - cumulative[:len(signal) - samples_per_cycle]
    )
    rms[samples_per_cycle:] = np.sqrt(window_energy / samples_per_cycle)

    return rms


def robust_sigma(values: np.ndarray, eps: float = 1e-9) -> float:
    """
    Robust spread estimator dari pre-fault baseline.

    MAD dipakai agar threshold tidak mudah tertarik oleh spike/noise sesaat.
    """

    values = np.asarray(values, dtype=float)
    values = values[~np.isnan(values)]

    if len(values) == 0:
        return eps

    median = np.median(values)
    mad = np.median(np.abs(values - median))

    return max(1.4826 * mad, eps)


def find_persistent_pickup(mask: np.ndarray, start_index: int, consecutive_samples: int):
    counter = 0

    for index in range(start_index, len(mask)):
        if mask[index]:
            counter += 1

            if counter >= consecutive_samples:
                return index - consecutive_samples + 1
        else:
            counter = 0

    return None


def refine_fault_index_from_instantaneous_change(
    df: pd.DataFrame,
    candidate_index: int,
    prefault_samples: int,
    samples_per_cycle: int,
    sensitivity: float = 6.0,
):
    """
    RMS 1 siklus bagus untuk stabilitas, tetapi fault bar bisa terlambat.
    Fungsi ini backtrack dari kandidat RMS ke perubahan instantaneous pertama.
    """

    search_start = max(prefault_samples, candidate_index - samples_per_cycle)
    search_end = min(len(df), candidate_index + 1)

    if search_start >= search_end:
        return candidate_index

    currents = df[["Ia", "Ib", "Ic"]].to_numpy(dtype=float)
    voltages = df[["Va", "Vb", "Vc"]].to_numpy(dtype=float)

    current_abs_max = np.max(np.abs(currents), axis=1)
    voltage_abs_max = np.max(np.abs(voltages), axis=1)

    current_step = np.zeros(len(df))
    voltage_step = np.zeros(len(df))

    current_step[1:] = np.max(np.abs(np.diff(currents, axis=0)), axis=1)
    voltage_step[1:] = np.max(np.abs(np.diff(voltages, axis=0)), axis=1)

    baseline_start = max(0, prefault_samples - samples_per_cycle)
    baseline_end = max(baseline_start + 1, prefault_samples)

    current_abs_base = current_abs_max[baseline_start:baseline_end]
    voltage_abs_base = voltage_abs_max[baseline_start:baseline_end]
    current_step_base = current_step[baseline_start:baseline_end]
    voltage_step_base = voltage_step[baseline_start:baseline_end]

    current_abs_threshold = (
        np.median(current_abs_base)
        + sensitivity * robust_sigma(current_abs_base)
    )
    current_step_threshold = (
        np.median(current_step_base)
        + sensitivity * robust_sigma(current_step_base)
    )
    voltage_step_threshold = (
        np.median(voltage_step_base)
        + sensitivity * robust_sigma(voltage_step_base)
    )
    voltage_drop_threshold = (
        np.median(voltage_abs_base)
        - sensitivity * robust_sigma(voltage_abs_base)
    )

    for index in range(search_start, search_end):
        current_changed = (
            current_abs_max[index] > current_abs_threshold
            or current_step[index] > current_step_threshold
        )
        voltage_changed = (
            voltage_abs_max[index] < voltage_drop_threshold
            or voltage_step[index] > voltage_step_threshold
        )

        if current_changed or voltage_changed:
            return index

    return candidate_index


def calculate_superimposed_energy(
    df: pd.DataFrame,
    samples_per_cycle: int,
    current_weight: float = 1.0,
    voltage_weight: float = 1.0,
):
    """
    Menghitung energi superimposed satu siklus.

    Sinyal gangguan dibandingkan dengan sinyal satu siklus sebelumnya:
    delta_x[n] = x[n] - x[n - samples_per_cycle].
    Pada kondisi pre-fault sinusoidal stabil, delta relatif kecil. Saat fault
    terjadi, delta melonjak dan biasanya lebih dekat ke inception daripada RMS.
    """

    currents = df[["Ia", "Ib", "Ic"]].to_numpy(dtype=float)
    voltages = df[["Va", "Vb", "Vc"]].to_numpy(dtype=float)

    current_delta = np.zeros_like(currents)
    voltage_delta = np.zeros_like(voltages)

    current_delta[samples_per_cycle:] = (
        currents[samples_per_cycle:] - currents[:-samples_per_cycle]
    )
    voltage_delta[samples_per_cycle:] = (
        voltages[samples_per_cycle:] - voltages[:-samples_per_cycle]
    )

    current_scale = np.nanmedian(
        np.max(np.abs(currents[:samples_per_cycle]), axis=1)
    )
    voltage_scale = np.nanmedian(
        np.max(np.abs(voltages[:samples_per_cycle]), axis=1)
    )

    current_scale = max(float(current_scale), 1e-9)
    voltage_scale = max(float(voltage_scale), 1e-9)

    normalized_current_delta = current_delta / current_scale
    normalized_voltage_delta = voltage_delta / voltage_scale

    current_energy = np.sum(normalized_current_delta ** 2, axis=1)
    voltage_energy = np.sum(normalized_voltage_delta ** 2, axis=1)
    total_energy = (
        current_weight * current_energy
        + voltage_weight * voltage_energy
    )

    return {
        "total_energy": total_energy,
        "current_energy": current_energy,
        "voltage_energy": voltage_energy,
    }


def detect_superimposed_fault_inception(
    df: pd.DataFrame,
    prefault_samples: int,
    samples_per_cycle: int,
    threshold_sigma: float = 8.0,
    consecutive_samples: int | None = None,
):
    energy = calculate_superimposed_energy(df, samples_per_cycle)
    total_energy = energy["total_energy"]

    baseline_start = samples_per_cycle
    baseline_end = max(baseline_start + 1, prefault_samples)
    baseline = total_energy[baseline_start:baseline_end]

    baseline_median = float(np.nanmedian(baseline))
    baseline_sigma = robust_sigma(baseline)
    threshold = baseline_median + threshold_sigma * baseline_sigma

    if consecutive_samples is None:
        consecutive_samples = max(2, int(round(0.05 * samples_per_cycle)))

    pickup_mask = total_energy > threshold

    candidate_index = find_persistent_pickup(
        pickup_mask,
        start_index=prefault_samples,
        consecutive_samples=consecutive_samples,
    )

    if candidate_index is None:
        return {
            "detected": False,
            "energy": energy,
            "threshold": threshold,
            "baseline_median": baseline_median,
            "baseline_sigma": baseline_sigma,
            "consecutive_samples": consecutive_samples,
        }

    local_left = max(prefault_samples, candidate_index - consecutive_samples)
    local_right = min(
        len(total_energy),
        candidate_index + max(consecutive_samples, int(round(0.25 * samples_per_cycle))),
    )

    if local_left < local_right:
        local_index = int(
            local_left + np.argmax(total_energy[local_left:local_right])
        )
    else:
        local_index = candidate_index

    return {
        "detected": True,
        "fault_index": int(candidate_index),
        "peak_index": int(local_index),
        "energy": energy,
        "threshold": threshold,
        "baseline_median": baseline_median,
        "baseline_sigma": baseline_sigma,
        "consecutive_samples": consecutive_samples,
        "peak_energy": float(total_energy[local_index]),
    }


def detect_fault_inception(
    df: pd.DataFrame,
    frequency: float = 50.0,
    current_threshold_multiplier: float = 2.0,
    voltage_drop_threshold: float = 0.85,
    min_prefault_cycles: int = 2,
    adaptive_threshold_sigma: float | None = None,
    consecutive_samples: int | None = None,
    refine_fault_bar: bool = False,
    method: str = "legacy_rms",
    superimposed_threshold_sigma: float = 8.0,
):
    """
    Deteksi awal gangguan berdasarkan:
    - kenaikan RMS arus terhadap pre-fault
    - penurunan RMS tegangan terhadap pre-fault

    Input df wajib berisi:
    time, Va, Vb, Vc, Ia, Ib, Ic

    Output:
    dictionary berisi index dan waktu fault inception.
    """

    fs = estimate_sampling_rate(df)
    samples_per_cycle = int(round(fs / frequency))

    if samples_per_cycle < 4:
        raise ValueError("Sampling rate terlalu rendah untuk analisis 1 siklus.")

    prefault_samples = min_prefault_cycles * samples_per_cycle

    if len(df) <= prefault_samples + samples_per_cycle:
        raise ValueError("Data terlalu pendek untuk deteksi gangguan.")

    # RMS sliding untuk arus dan tegangan
    ia_rms = calculate_rms_sliding(df["Ia"].values, samples_per_cycle)
    ib_rms = calculate_rms_sliding(df["Ib"].values, samples_per_cycle)
    ic_rms = calculate_rms_sliding(df["Ic"].values, samples_per_cycle)

    va_rms = calculate_rms_sliding(df["Va"].values, samples_per_cycle)
    vb_rms = calculate_rms_sliding(df["Vb"].values, samples_per_cycle)
    vc_rms = calculate_rms_sliding(df["Vc"].values, samples_per_cycle)

    current_rms_max = np.max(
        np.vstack([
            np.nan_to_num(ia_rms, nan=-np.inf),
            np.nan_to_num(ib_rms, nan=-np.inf),
            np.nan_to_num(ic_rms, nan=-np.inf),
        ]),
        axis=0,
    )
    voltage_rms_min = np.min(
        np.vstack([
            np.nan_to_num(va_rms, nan=np.inf),
            np.nan_to_num(vb_rms, nan=np.inf),
            np.nan_to_num(vc_rms, nan=np.inf),
        ]),
        axis=0,
    )

    current_rms_max[~np.isfinite(current_rms_max)] = np.nan
    voltage_rms_min[~np.isfinite(voltage_rms_min)] = np.nan

    prefault_current = np.nanmedian(
        current_rms_max[samples_per_cycle:prefault_samples]
    )

    prefault_voltage = np.nanmedian(
        voltage_rms_min[samples_per_cycle:prefault_samples]
    )

    current_pickup = prefault_current * current_threshold_multiplier
    voltage_pickup = prefault_voltage * voltage_drop_threshold

    current_condition = current_rms_max > current_pickup
    voltage_condition = voltage_rms_min < voltage_pickup

    pickup_mask = current_condition | voltage_condition
    current_sigma = None
    voltage_sigma = None
    disturbance_score = None

    if adaptive_threshold_sigma is not None:
        current_baseline = current_rms_max[samples_per_cycle:prefault_samples]
        voltage_baseline = voltage_rms_min[samples_per_cycle:prefault_samples]

        current_sigma = robust_sigma(current_baseline)
        voltage_sigma = robust_sigma(voltage_baseline)

        current_score = (current_rms_max - prefault_current) / current_sigma
        voltage_score = (prefault_voltage - voltage_rms_min) / voltage_sigma
        current_score = np.nan_to_num(current_score, nan=-np.inf)
        voltage_score = np.nan_to_num(voltage_score, nan=-np.inf)
        disturbance_score = np.maximum(current_score, voltage_score)

        pickup_mask = pickup_mask | (disturbance_score >= adaptive_threshold_sigma)

    if consecutive_samples is None:
        consecutive_samples = 1

    rms_fault_index = find_persistent_pickup(
        pickup_mask,
        start_index=prefault_samples,
        consecutive_samples=consecutive_samples,
    )

    superimposed_result = None

    if method == "hybrid_superimposed":
        superimposed_result = detect_superimposed_fault_inception(
            df=df,
            prefault_samples=prefault_samples,
            samples_per_cycle=samples_per_cycle,
            threshold_sigma=superimposed_threshold_sigma,
            consecutive_samples=None,
        )

        if superimposed_result["detected"]:
            if rms_fault_index is None:
                rms_fault_index = superimposed_result["fault_index"]
            else:
                max_early_shift = max(2, samples_per_cycle)

                if (
                    superimposed_result["fault_index"] <= rms_fault_index
                    and rms_fault_index - superimposed_result["fault_index"] <= max_early_shift
                ):
                    rms_fault_index = superimposed_result["fault_index"]

    if rms_fault_index is None:
        result = {
            "detected": False,
            "message": "Awal gangguan tidak terdeteksi otomatis. Silakan gunakan cursor manual.",
            "fs": fs,
            "samples_per_cycle": samples_per_cycle,
            "prefault_current": prefault_current,
            "prefault_voltage": prefault_voltage,
            "current_sigma": current_sigma,
            "voltage_sigma": voltage_sigma,
            "adaptive_threshold_sigma": adaptive_threshold_sigma,
            "consecutive_samples": consecutive_samples,
            "method": method,
        }

        if superimposed_result is not None:
            result["superimposed"] = superimposed_result

        return result

    if refine_fault_bar:
        fault_index = refine_fault_index_from_instantaneous_change(
            df=df,
            candidate_index=rms_fault_index,
            prefault_samples=prefault_samples,
            samples_per_cycle=samples_per_cycle,
            sensitivity=adaptive_threshold_sigma or 6.0,
        )
    else:
        fault_index = rms_fault_index

    fault_time = float(df["time"].iloc[fault_index])
    rms_fault_time = float(df["time"].iloc[rms_fault_index])

    if disturbance_score is not None:
        confidence_score = min(
            10.0,
            max(
                0.0,
                float(
                    np.nanmax(
                        disturbance_score[
                            rms_fault_index:rms_fault_index + samples_per_cycle
                        ]
                    ) / 2.0
                ),
            ),
        )
    else:
        confidence_score = 8.0

    result = {
        "detected": True,
        "fault_index": int(fault_index),
        "rms_fault_index": int(rms_fault_index),
        "fault_time": fault_time,
        "rms_fault_time": rms_fault_time,
        "fs": fs,
        "samples_per_cycle": samples_per_cycle,
        "prefault_current": prefault_current,
        "prefault_voltage": prefault_voltage,
        "current_sigma": current_sigma,
        "voltage_sigma": voltage_sigma,
        "current_pickup": current_pickup,
        "voltage_pickup": voltage_pickup,
        "adaptive_threshold_sigma": adaptive_threshold_sigma,
        "consecutive_samples": consecutive_samples,
        "refine_fault_bar": refine_fault_bar,
        "method": method,
        "confidence_score": round(confidence_score, 2),
        "current_rms_max": current_rms_max,
        "voltage_rms_min": voltage_rms_min,
    }

    if disturbance_score is not None:
        result["disturbance_score"] = disturbance_score

    if superimposed_result is not None:
        result["superimposed"] = superimposed_result

    return result


def build_fault_window(
    df: pd.DataFrame,
    fault_index: int,
    samples_per_cycle: int,
    pre_fault_cycles: int = 2,
    post_fault_cycles: int = 4,
):
    """
    Membuat window analisis:
    - left cursor = beberapa siklus sebelum fault
    - right cursor = beberapa siklus setelah fault
    - dft cursor = 1 siklus setelah fault inception

    DFT cursor diletakkan setelah gangguan agar window DFT di sebelah kirinya
    tidak melintasi titik fault inception.
    """

    left_index = max(0, fault_index - pre_fault_cycles * samples_per_cycle)
    right_index = min(len(df) - 1, fault_index + post_fault_cycles * samples_per_cycle)

    # Cursor DFT untuk Step 4.
    # Karena DFT window berada di kiri cursor, maka cursor ini diletakkan
    # minimal 1 siklus setelah awal gangguan.
    dft_index = min(len(df) - 1, fault_index + samples_per_cycle)

    return {
        "left_index": int(left_index),
        "right_index": int(right_index),
        "fault_index": int(fault_index),
        "dft_index": int(dft_index),
        "left_time": float(df["time"].iloc[left_index]),
        "right_time": float(df["time"].iloc[right_index]),
        "fault_time": float(df["time"].iloc[fault_index]),
        "dft_time": float(df["time"].iloc[dft_index]),
    }
