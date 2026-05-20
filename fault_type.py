import pandas as pd


def get_mag(phasors: dict, signal_name: str) -> float:
    return float(phasors[signal_name]["magnitude"])


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def calculate_auto_fault_type_thresholds(
    phasors: dict,
    prefault_phasors: dict | None = None,
):
    """
    Membuat threshold deteksi tipe gangguan dari kondisi normal rekaman.

    Nilai normal diambil dari fasor pre-fault yang sudah diskalakan oleh rasio
    CT/VT pada signal assignment. Dengan begitu user tidak perlu menebak apakah
    2% drop tegangan atau kenaikan arus tertentu sudah signifikan; aplikasi
    menilai perubahan relatif terhadap rekaman itu sendiri.
    """

    defaults = {
        "mode": "default_no_prefault",
        "voltage_drop_threshold": 0.80,
        "current_rise_threshold": 1.50,
        "ground_current_threshold": 0.20,
        "delta_current_threshold": 0.45,
        "delta_voltage_threshold": 0.01,
        "normal_voltage_rms": 0.0,
        "normal_current_rms": 0.0,
        "normal_ground_current_rms": 0.0,
        "max_voltage_drop_pct": 0.0,
        "max_current_change_pct": 0.0,
        "ground_current_rise_ratio": 0.0,
    }

    if prefault_phasors is None:
        return defaults

    required = ["Va", "Vb", "Vc", "Ia", "Ib", "Ic"]
    if any(name not in phasors or name not in prefault_phasors for name in required):
        return defaults

    phase_signal = {"A": "a", "B": "b", "C": "c"}
    prefault_voltages = {
        phase: get_mag(prefault_phasors, f"V{suffix}")
        for phase, suffix in phase_signal.items()
    }
    fault_voltages = {
        phase: get_mag(phasors, f"V{suffix}")
        for phase, suffix in phase_signal.items()
    }
    prefault_currents = {
        phase: get_mag(prefault_phasors, f"I{suffix}")
        for phase, suffix in phase_signal.items()
    }
    fault_currents = {
        phase: get_mag(phasors, f"I{suffix}")
        for phase, suffix in phase_signal.items()
    }

    normal_voltage = sum(prefault_voltages.values()) / 3.0
    normal_current = sum(prefault_currents.values()) / 3.0
    max_prefault_voltage = max(max(prefault_voltages.values()), 1e-9)
    max_prefault_current = max(max(prefault_currents.values()), 1e-9)

    voltage_drop_fractions = {
        phase: max(0.0, (prefault_voltages[phase] - fault_voltages[phase]) / max(prefault_voltages[phase], 1e-9))
        for phase in ["A", "B", "C"]
    }
    current_change_fractions = {
        phase: abs(fault_currents[phase] - prefault_currents[phase]) / max(prefault_currents[phase], 1e-9)
        for phase in ["A", "B", "C"]
    }

    max_voltage_drop = max(voltage_drop_fractions.values())
    max_current_change = max(current_change_fractions.values())

    # Threshold tegangan utama dipakai untuk perbandingan antar fasa pada kondisi fault.
    # Untuk high resistance fault, sag bisa hanya 1-2%, jadi threshold dibuat lebih
    # dekat ke normal bila pre-fault menunjukkan drop kecil tetapi konsisten.
    voltage_drop_threshold = clamp(1.0 - max(0.002, 0.45 * max_voltage_drop), 0.80, 0.995)

    # Threshold arus antar fasa diturunkan saat perubahan arus dominan kecil atau
    # ketika salah satu arus justru turun akibat load flow.
    current_rise_threshold = clamp(1.0 + max(0.05, 0.35 * max_current_change), 1.05, 1.80)

    # Delta current memakai dominansi antar delta, bukan magnitude absolut.
    # Makin dominan perubahan satu fasa, threshold bisa sedikit lebih longgar.
    delta_current_threshold = clamp(0.30 + 0.15 / max(1.0 + 3.0 * max_current_change, 1e-9), 0.25, 0.45)

    # Delta voltage threshold adalah fraksi terhadap tegangan normal. Dibuat sensitif
    # untuk sag kecil tetapi tetap punya lantai terhadap noise.
    delta_voltage_threshold = clamp(max(0.001, 0.50 * max_voltage_drop), 0.001, 0.02)

    prefault_ie = get_mag(prefault_phasors, "IE") if "IE" in prefault_phasors else 0.0
    fault_ie = get_mag(phasors, "IE") if "IE" in phasors else 0.0
    ground_rise_ratio = (fault_ie - prefault_ie) / max(max_prefault_current, 1e-9)
    ground_fault_ratio = fault_ie / max(max(fault_currents.values()), 1e-9)

    # Ground threshold dibuat mengikuti noise pre-fault IE. Bila IE naik jelas dari
    # baseline, threshold rasio dapat dibuat lebih sensitif.
    prefault_ground_ratio = prefault_ie / max(max_prefault_current, 1e-9)
    ground_current_threshold = clamp(max(0.03, prefault_ground_ratio * 2.5, ground_fault_ratio * 0.55), 0.03, 0.20)

    return {
        "mode": "auto_prefault",
        "voltage_drop_threshold": voltage_drop_threshold,
        "current_rise_threshold": current_rise_threshold,
        "ground_current_threshold": ground_current_threshold,
        "delta_current_threshold": delta_current_threshold,
        "delta_voltage_threshold": delta_voltage_threshold,
        "normal_voltage_rms": normal_voltage,
        "normal_current_rms": normal_current,
        "normal_ground_current_rms": prefault_ie,
        "max_voltage_drop_pct": max_voltage_drop * 100.0,
        "max_current_change_pct": max_current_change * 100.0,
        "ground_current_rise_ratio": ground_rise_ratio,
    }


def detect_fault_type(
    phasors: dict,
    prefault_phasors: dict | None = None,
    voltage_drop_threshold: float = 0.80,
    current_rise_threshold: float = 1.50,
    ground_current_threshold: float = 0.20,
    delta_current_threshold: float = 0.45,
    delta_voltage_threshold: float = 0.01,
):
    """
    Deteksi jenis gangguan berbasis fasor RMS fundamental.

    Logika utama:
    1. Cari fasa dengan arus tinggi relatif terhadap arus minimum.
    2. Cari fasa dengan tegangan drop relatif terhadap tegangan maksimum.
    3. Cek keberadaan arus tanah / zero sequence.
    4. Klasifikasikan menjadi AG, BG, CG, AB, BC, CA, ABG, BCG, CAG, ABC.

    Catatan:
    - Ini rule-based awal.
    - Nanti dapat diperkuat dengan pre-fault phasor dan negative/zero sequence.
    """

    Va = get_mag(phasors, "Va")
    Vb = get_mag(phasors, "Vb")
    Vc = get_mag(phasors, "Vc")

    Ia = get_mag(phasors, "Ia")
    Ib = get_mag(phasors, "Ib")
    Ic = get_mag(phasors, "Ic")

    IE = get_mag(phasors, "IE") if "IE" in phasors else 0.0
    I0 = get_mag(phasors, "I0") if "I0" in phasors else IE / 3.0

    voltages = {
        "A": Va,
        "B": Vb,
        "C": Vc,
    }

    currents = {
        "A": Ia,
        "B": Ib,
        "C": Ic,
    }

    max_voltage = max(voltages.values())
    min_voltage = min(voltages.values())

    max_current = max(currents.values())
    min_current = max(min(currents.values()), 1e-9)

    avg_current = sum(currents.values()) / 3.0
    avg_voltage = sum(voltages.values()) / 3.0

    # Fasa dianggap terganggu jika:
    # - arusnya tinggi dibanding arus minimum, atau
    # - tegangannya drop dibanding tegangan maksimum.
    faulted_by_current = [
        phase for phase, current in currents.items()
        if current >= current_rise_threshold * min_current
    ]

    faulted_by_voltage = [
        phase for phase, voltage in voltages.items()
        if voltage <= voltage_drop_threshold * max_voltage
    ]

    delta_currents = {}
    delta_voltages = {}
    current_magnitude_change_pct = {}
    voltage_magnitude_change_pct = {}
    faulted_by_delta_current = []
    faulted_by_delta_voltage = []
    depressed_current_phases = []
    prefault_available = prefault_phasors is not None

    if prefault_available:
        for phase, v_name, i_name in [
            ("A", "Va", "Ia"),
            ("B", "Vb", "Ib"),
            ("C", "Vc", "Ic"),
        ]:
            if (
                v_name not in prefault_phasors
                or i_name not in prefault_phasors
                or v_name not in phasors
                or i_name not in phasors
            ):
                prefault_available = False
                break

            v_prefault = prefault_phasors[v_name]["complex"]
            i_prefault = prefault_phasors[i_name]["complex"]
            v_fault = phasors[v_name]["complex"]
            i_fault = phasors[i_name]["complex"]

            delta_voltages[phase] = abs(v_fault - v_prefault)
            delta_currents[phase] = abs(i_fault - i_prefault)
            voltage_magnitude_change_pct[phase] = (
                (abs(v_fault) - abs(v_prefault)) / max(abs(v_prefault), 1e-9) * 100.0
            )
            current_magnitude_change_pct[phase] = (
                (abs(i_fault) - abs(i_prefault)) / max(abs(i_prefault), 1e-9) * 100.0
            )

        if prefault_available:
            max_delta_current = max(delta_currents.values())
            max_delta_voltage = max(delta_voltages.values())
            max_prefault_current = max(
                abs(prefault_phasors[name]["complex"]) for name in ["Ia", "Ib", "Ic"]
            )
            max_prefault_voltage = max(
                abs(prefault_phasors[name]["complex"]) for name in ["Va", "Vb", "Vc"]
            )

            faulted_by_delta_current = [
                phase
                for phase, value in delta_currents.items()
                if (
                    value >= delta_current_threshold * max(max_delta_current, 1e-9)
                    and value >= 0.02 * max(max_prefault_current, 1e-9)
                )
            ]
            faulted_by_delta_voltage = [
                phase
                for phase, value in delta_voltages.items()
                if (
                    value >= max(delta_voltage_threshold * max(max_prefault_voltage, 1e-9), 1e-9)
                    and voltage_magnitude_change_pct[phase] <= -0.2
                )
            ]
            depressed_current_phases = [
                phase
                for phase, value in current_magnitude_change_pct.items()
                if value <= -5.0 and phase in faulted_by_delta_current
            ]

    faulted_phases = sorted(
        list(
            set(
                faulted_by_current
                + faulted_by_voltage
                + faulted_by_delta_current
                + faulted_by_delta_voltage
            )
        )
    )

    # Deteksi ground involvement.
    # Ground fault biasanya memunculkan I0/IE signifikan.
    ground_ratio_to_max_current = IE / max(max_current, 1e-9)
    ground_ratio_to_avg_current = I0 / max(avg_current, 1e-9)

    ground_involved = (
        ground_ratio_to_max_current >= ground_current_threshold
        or ground_ratio_to_avg_current >= ground_current_threshold
    )

    if prefault_available:
        prefault_ie = get_mag(prefault_phasors, "IE") if "IE" in prefault_phasors else 0.0
        prefault_i0 = get_mag(prefault_phasors, "I0") if "I0" in prefault_phasors else prefault_ie / 3.0
        max_prefault_current = max(
            abs(prefault_phasors[name]["complex"]) for name in ["Ia", "Ib", "Ic"]
        )
        ground_involved_by_delta = (
            IE - prefault_ie >= max(0.03 * max(max_prefault_current, 1e-9), 2.0 * prefault_ie)
            or I0 - prefault_i0 >= max(0.01 * max(max_prefault_current, 1e-9), 2.0 * prefault_i0)
        )
        ground_involved = ground_involved or ground_involved_by_delta
    else:
        ground_involved_by_delta = False

    # Fallback jika semua fasa terdeteksi karena arus besar simetris.
    # ABC fault umumnya arus tiga fasa besar dan ground current kecil.
    current_balance_ratio = min_current / max(max_current, 1e-9)
    voltage_balance_ratio = min_voltage / max(max_voltage, 1e-9)

    is_three_phase_candidate = (
        current_balance_ratio >= 0.60
        and len(faulted_by_current) >= 2
        and not ground_involved
    )

    if is_three_phase_candidate:
        fault_type = "ABC"
        faulted_phases = ["A", "B", "C"]

    elif len(faulted_phases) == 1:
        phase = faulted_phases[0]
        if ground_involved:
            fault_type = f"{phase}G"
        else:
            # Jarang, tapi disediakan sebagai indikasi tidak pasti.
            fault_type = f"{phase}?"
    
    elif len(faulted_phases) == 2:
        pair = "".join(faulted_phases)

        if pair == "AC":
            pair = "CA"

        if ground_involved:
            fault_type = f"{pair}G"
        else:
            fault_type = pair

    elif len(faulted_phases) >= 3:
        if ground_involved:
            fault_type = "ABCG"
        else:
            fault_type = "ABC"

    else:
        fault_type = "UNKNOWN"

    if (
        prefault_available
        and ground_involved
        and len(faulted_phases) != 1
        and faulted_by_delta_current
    ):
        dominant_phase = max(
            faulted_by_delta_current,
            key=lambda phase: delta_currents.get(phase, 0.0),
        )
        if delta_currents[dominant_phase] >= 1.25 * max(
            [
                value
                for phase, value in delta_currents.items()
                if phase != dominant_phase
            ]
            or [0.0]
        ):
            faulted_phases = [dominant_phase]
            fault_type = f"{dominant_phase}G"

    confidence = calculate_fault_type_confidence(
        fault_type=fault_type,
        ground_involved=ground_involved,
        ground_ratio=ground_ratio_to_max_current,
        current_balance_ratio=current_balance_ratio,
        voltage_balance_ratio=voltage_balance_ratio,
        faulted_phases=faulted_phases,
    )

    result = {
        "fault_type": fault_type,
        "faulted_phases": faulted_phases,
        "ground_involved": ground_involved,
        "confidence": confidence,
        "metrics": {
            "Va": Va,
            "Vb": Vb,
            "Vc": Vc,
            "Ia": Ia,
            "Ib": Ib,
            "Ic": Ic,
            "IE": IE,
            "I0": I0,
            "max_voltage": max_voltage,
            "min_voltage": min_voltage,
            "max_current": max_current,
            "min_current": min_current,
            "avg_current": avg_current,
            "avg_voltage": avg_voltage,
            "ground_ratio_to_max_current": ground_ratio_to_max_current,
            "ground_ratio_to_avg_current": ground_ratio_to_avg_current,
            "ground_involved_by_delta": ground_involved_by_delta,
            "current_balance_ratio": current_balance_ratio,
            "voltage_balance_ratio": voltage_balance_ratio,
            "faulted_by_current": faulted_by_current,
            "faulted_by_voltage": faulted_by_voltage,
            "prefault_available": prefault_available,
            "faulted_by_delta_current": faulted_by_delta_current,
            "faulted_by_delta_voltage": faulted_by_delta_voltage,
            "depressed_current_phases": depressed_current_phases,
            "delta_current_A": delta_currents.get("A", 0.0),
            "delta_current_B": delta_currents.get("B", 0.0),
            "delta_current_C": delta_currents.get("C", 0.0),
            "delta_voltage_A": delta_voltages.get("A", 0.0),
            "delta_voltage_B": delta_voltages.get("B", 0.0),
            "delta_voltage_C": delta_voltages.get("C", 0.0),
            "current_magnitude_change_pct_A": current_magnitude_change_pct.get("A", 0.0),
            "current_magnitude_change_pct_B": current_magnitude_change_pct.get("B", 0.0),
            "current_magnitude_change_pct_C": current_magnitude_change_pct.get("C", 0.0),
            "voltage_magnitude_change_pct_A": voltage_magnitude_change_pct.get("A", 0.0),
            "voltage_magnitude_change_pct_B": voltage_magnitude_change_pct.get("B", 0.0),
            "voltage_magnitude_change_pct_C": voltage_magnitude_change_pct.get("C", 0.0),
        },
    }

    return result


def calculate_fault_type_confidence(
    fault_type: str,
    ground_involved: bool,
    ground_ratio: float,
    current_balance_ratio: float,
    voltage_balance_ratio: float,
    faulted_phases: list,
):
    """
    Skor confidence sederhana 0 sampai 10.
    Ini bukan standar relay, tetapi indikator kualitas klasifikasi awal.
    """

    score = 5.0

    if fault_type != "UNKNOWN":
        score += 1.5

    if "?" not in fault_type:
        score += 1.0

    if ground_involved and ground_ratio >= 0.25:
        score += 1.0

    if fault_type in ["ABC", "ABCG"]:
        if current_balance_ratio >= 0.70:
            score += 1.0
    else:
        if voltage_balance_ratio <= 0.90:
            score += 0.5

    if len(faulted_phases) >= 1:
        score += 0.5

    return round(min(score, 10.0), 2)


def build_fault_type_metrics_dataframe(result: dict):
    """
    Membuat DataFrame ringkasan metrik deteksi.
    """

    metrics = result["metrics"]

    rows = [
        {"Metric": "Fault Type", "Value": result["fault_type"]},
        {"Metric": "Faulted Phases", "Value": ", ".join(result["faulted_phases"])},
        {"Metric": "Ground Involved", "Value": result["ground_involved"]},
        {"Metric": "Confidence 0-10", "Value": result["confidence"]},
        {"Metric": "Va RMS", "Value": metrics["Va"]},
        {"Metric": "Vb RMS", "Value": metrics["Vb"]},
        {"Metric": "Vc RMS", "Value": metrics["Vc"]},
        {"Metric": "Ia RMS", "Value": metrics["Ia"]},
        {"Metric": "Ib RMS", "Value": metrics["Ib"]},
        {"Metric": "Ic RMS", "Value": metrics["Ic"]},
        {"Metric": "IE RMS", "Value": metrics["IE"]},
        {"Metric": "I0 RMS", "Value": metrics["I0"]},
        {
            "Metric": "Ground Ratio to Max Current",
            "Value": metrics["ground_ratio_to_max_current"],
        },
        {
            "Metric": "Ground Involved by Delta",
            "Value": metrics["ground_involved_by_delta"],
        },
        {
            "Metric": "Current Balance Ratio",
            "Value": metrics["current_balance_ratio"],
        },
        {
            "Metric": "Voltage Balance Ratio",
            "Value": metrics["voltage_balance_ratio"],
        },
        {
            "Metric": "Faulted by Current",
            "Value": ", ".join(metrics["faulted_by_current"]),
        },
        {
            "Metric": "Faulted by Voltage",
            "Value": ", ".join(metrics["faulted_by_voltage"]),
        },
        {"Metric": "Pre-fault Phasor Available", "Value": metrics["prefault_available"]},
        {
            "Metric": "Faulted by Delta Current",
            "Value": ", ".join(metrics["faulted_by_delta_current"]),
        },
        {
            "Metric": "Faulted by Delta Voltage",
            "Value": ", ".join(metrics["faulted_by_delta_voltage"]),
        },
        {
            "Metric": "Depressed Current Phase",
            "Value": ", ".join(metrics["depressed_current_phases"]),
        },
        {"Metric": "Delta Ia RMS", "Value": metrics["delta_current_A"]},
        {"Metric": "Delta Ib RMS", "Value": metrics["delta_current_B"]},
        {"Metric": "Delta Ic RMS", "Value": metrics["delta_current_C"]},
        {"Metric": "Delta Va RMS", "Value": metrics["delta_voltage_A"]},
        {"Metric": "Delta Vb RMS", "Value": metrics["delta_voltage_B"]},
        {"Metric": "Delta Vc RMS", "Value": metrics["delta_voltage_C"]},
        {
            "Metric": "Ia Magnitude Change %",
            "Value": metrics["current_magnitude_change_pct_A"],
        },
        {
            "Metric": "Ib Magnitude Change %",
            "Value": metrics["current_magnitude_change_pct_B"],
        },
        {
            "Metric": "Ic Magnitude Change %",
            "Value": metrics["current_magnitude_change_pct_C"],
        },
        {
            "Metric": "Va Magnitude Change %",
            "Value": metrics["voltage_magnitude_change_pct_A"],
        },
        {
            "Metric": "Vb Magnitude Change %",
            "Value": metrics["voltage_magnitude_change_pct_B"],
        },
        {
            "Metric": "Vc Magnitude Change %",
            "Value": metrics["voltage_magnitude_change_pct_C"],
        },
    ]

    return pd.DataFrame(rows)
