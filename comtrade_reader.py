import re
import tempfile
import comtrade
import pandas as pd


def _safe_getattr(obj, attr, default=None):
    try:
        return getattr(obj, attr, default)
    except Exception:
        return default


def _parse_cfg_analog_metadata(cfg_path: str):
    """
    Parser ringan untuk mengambil metadata analog dari file .cfg.

    Format umum channel analog COMTRADE:
    An,ch_id,ph,ccbm,uu,a,b,skew,min,max,primary,secondary,PS

    Tidak semua relay mengisi primary/secondary dengan benar.
    Jadi hasil ini tetap perlu ditampilkan agar user bisa validasi.
    """

    analog_meta = []

    with open(cfg_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if len(lines) < 3:
        return analog_meta

    # Baris kedua biasanya: total_channels, analog_countA, digital_countD
    try:
        channel_line = lines[1].split(",")
        analog_count = 0

        for item in channel_line:
            item = item.strip().upper()
            if item.endswith("A"):
                analog_count = int(item.replace("A", ""))
                break
    except Exception:
        analog_count = 0

    # Channel analog biasanya mulai dari baris ke-3 sebanyak analog_count
    for line in lines[2:2 + analog_count]:
        parts = [p.strip() for p in line.split(",")]

        if len(parts) < 6:
            continue

        # Default COMTRADE analog channel fields
        # index: 0 An, 1 ch_id, 2 phase, 3 ccbm, 4 unit, 5 a, 6 b, ...
        item = {
            "raw": line,
            "index": parts[0] if len(parts) > 0 else "",
            "name": parts[1] if len(parts) > 1 else "",
            "phase": parts[2] if len(parts) > 2 else "",
            "ccbm": parts[3] if len(parts) > 3 else "",
            "unit": parts[4] if len(parts) > 4 else "",
            "a": _to_float(parts[5]) if len(parts) > 5 else None,
            "b": _to_float(parts[6]) if len(parts) > 6 else None,
            "skew": _to_float(parts[7]) if len(parts) > 7 else None,
            "min": _to_float(parts[8]) if len(parts) > 8 else None,
            "max": _to_float(parts[9]) if len(parts) > 9 else None,
            "primary": _to_float(parts[10]) if len(parts) > 10 else None,
            "secondary": _to_float(parts[11]) if len(parts) > 11 else None,
            "ps": parts[12] if len(parts) > 12 else "",
        }

        analog_meta.append(item)

    return analog_meta


def _parse_cfg_trigger_time(cfg_path: str):
    """
    Mencoba mengambil start time dan trigger time dari .cfg.

    Pada COMTRADE, setelah sampling-rate section biasanya ada:
    start timestamp
    trigger timestamp

    Karena variasi format cukup banyak, parser ini memakai pendekatan heuristik.
    """

    with open(cfg_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Cari baris yang menyerupai timestamp dd/mm/yyyy,hh:mm:ss.sss
    timestamp_lines = []
    pattern = re.compile(r"\d{1,2}/\d{1,2}/\d{4}.*\d{1,2}:\d{1,2}:\d{1,2}")

    for line in lines:
        if pattern.search(line):
            timestamp_lines.append(line)

    start_time = timestamp_lines[0] if len(timestamp_lines) >= 1 else None
    trigger_time = timestamp_lines[1] if len(timestamp_lines) >= 2 else None

    return start_time, trigger_time


def _to_float(value):
    try:
        if value is None:
            return None

        value = str(value).strip()

        if value == "":
            return None

        return float(value)
    except Exception:
        return None


def _infer_ratio_from_channel_meta(analog_meta):
    """
    Mengambil perkiraan rasio VT dan CT dari metadata channel.

    Jika unit channel mengandung V/kV, dianggap voltage.
    Jika unit channel mengandung A/kA, dianggap current.

    Rasio dihitung dari primary/secondary jika tersedia.
    """

    voltage_ratios = []
    current_ratios = []

    for ch in analog_meta:
        unit = str(ch.get("unit", "")).lower()
        primary = ch.get("primary")
        secondary = ch.get("secondary")

        if primary in [None, 0] or secondary in [None, 0]:
            continue

        ratio = primary / secondary

        if "v" in unit:
            voltage_ratios.append(ratio)

        elif "a" in unit:
            current_ratios.append(ratio)

    vt_ratio = _most_common_float(voltage_ratios)
    ct_ratio = _most_common_float(current_ratios)

    return vt_ratio, ct_ratio


def _most_common_float(values):
    if not values:
        return None

    rounded = [round(v, 6) for v in values]
    return max(set(rounded), key=rounded.count)


def read_comtrade(cfg_path: str, dat_path: str):
    """
    Membaca file COMTRADE .cfg dan .dat.

    Output:
    - df: DataFrame time + analog channel
    - metadata: metadata record, channel, ratio, trigger
    """

    record, cfg_path_for_metadata = _load_comtrade_with_fallbacks(cfg_path, dat_path)

    time = record.time
    analog_channel_names_raw = list(record.analog_channel_ids)
    analog_values = record.analog

    df = pd.DataFrame()
    df["time"] = time

    analog_channel_names = []
    channel_label_map = []

    for index, raw_channel_name in enumerate(analog_channel_names_raw):
        unique_label = f"A{index + 1:03d} | {raw_channel_name}"

        analog_channel_names.append(unique_label)

        channel_label_map.append(
            {
                "analog_index": index + 1,
                "original_name": raw_channel_name,
                "unique_label": unique_label,
            }
        )

        df[unique_label] = analog_values[index]

    analog_meta = _parse_cfg_analog_metadata(cfg_path_for_metadata)
    start_time_cfg, trigger_time_cfg = _parse_cfg_trigger_time(cfg_path_for_metadata)

    vt_ratio_cfg, ct_ratio_cfg = _infer_ratio_from_channel_meta(analog_meta)

    trigger_time_record = (
        _safe_getattr(record, "trigger_timestamp", None)
        or _safe_getattr(record, "trigger_time", None)
        or trigger_time_cfg
    )

    start_time_record = (
        _safe_getattr(record, "start_timestamp", None)
        or _safe_getattr(record, "start_time", None)
        or start_time_cfg
    )

    metadata = {
        "station_name": _safe_getattr(record, "station_name", None),
        "rec_dev_id": _safe_getattr(record, "rec_dev_id", None),
        "frequency": _safe_getattr(record, "frequency", None),
        "total_samples": len(time),
        "analog_channels": analog_channel_names,
        "analog_channels_raw": analog_channel_names_raw,
        "channel_label_map": channel_label_map,
        "digital_channels": _safe_getattr(record, "status_channel_ids", []),
        "analog_metadata": analog_meta,
        "cfg_start_time": start_time_cfg,
        "cfg_trigger_time": trigger_time_cfg,
        "record_start_time": start_time_record,
        "record_trigger_time": trigger_time_record,
        "vt_ratio_from_cfg": vt_ratio_cfg,
        "ct_ratio_from_cfg": ct_ratio_cfg,
    }

    return df, metadata


def _load_comtrade_with_fallbacks(cfg_path: str, dat_path: str):
    attempts = [
        (cfg_path, False, False, False),
        (cfg_path, True, False, False),
        (cfg_path, False, True, False),
        (cfg_path, True, True, False),
        (cfg_path, False, False, True),
        (cfg_path, True, False, True),
        (cfg_path, False, True, True),
        (cfg_path, True, True, True),
    ]
    last_error = None

    for source_cfg, simplify_station_line, normalize_timestamps, normalize_file_type in attempts:
        try:
            candidate_cfg = source_cfg

            if simplify_station_line or normalize_timestamps or normalize_file_type:
                candidate_cfg = _create_compatible_cfg_copy(
                    source_cfg,
                    dat_path=dat_path,
                    simplify_station_line=simplify_station_line,
                    normalize_timestamps=normalize_timestamps,
                    normalize_file_type=normalize_file_type,
                )

            return comtrade.load(candidate_cfg, dat_path), candidate_cfg

        except (ValueError, comtrade.ComtradeError) as error:
            last_error = error
            message = str(error)

            if (
                "too many values to unpack" not in message
                and "month must be in 1..12" not in message
                and "Not supported data file format" not in message
            ):
                raise

    raise last_error


def _create_compatible_cfg_copy(
    cfg_path: str,
    dat_path: str | None = None,
    simplify_station_line: bool = False,
    normalize_timestamps: bool = False,
    normalize_file_type: bool = False,
):
    """
    Beberapa export relay menulis baris pertama CFG lebih dari format yang
    didukung library comtrade terpasang. Library tersebut mengharapkan dua
    field: station_name, rec_dev_id. Ada juga file yang memakai tanggal
    DD/MM/YYYY sementara library membaca MM/DD/YYYY. Fallback ini hanya
    mengubah salinan sementara CFG; file asli user tidak diubah.
    """

    with open(cfg_path, "r", encoding="utf-8", errors="ignore") as source:
        lines = source.readlines()

    if not lines:
        raise ValueError("File CFG kosong.")

    if simplify_station_line:
        first_line = lines[0].strip()
        parts = [part.strip() for part in first_line.split(",")]

        if len(parts) > 2:
            station_name = parts[0] or "UNKNOWN_STATION"
            rec_dev_id = parts[1] or "UNKNOWN_DEVICE"
            lines[0] = f"{station_name},{rec_dev_id}\n"

    if normalize_timestamps:
        lines = [_normalize_cfg_timestamp_line(line) for line in lines]

    if normalize_file_type:
        lines = _normalize_cfg_file_type(lines, dat_path)

    temp_cfg = tempfile.NamedTemporaryFile(delete=False, suffix=".cfg", mode="w", encoding="utf-8")

    with temp_cfg:
        temp_cfg.writelines(lines)

    return temp_cfg.name


def _normalize_cfg_file_type(lines: list[str], dat_path: str | None):
    """
    Beberapa CFG export relay menulis baris tipe DAT sebagai kosong, memakai
    tambahan komentar setelah koma, atau memakai kapitalisasi/whitespace yang
    membuat library gagal mengenali format. Normalisasi ini hanya berlaku pada
    salinan sementara CFG.
    """

    file_type_index = _find_cfg_file_type_line_index(lines)

    if file_type_index is None:
        return lines

    normalized_lines = list(lines)
    current_line = normalized_lines[file_type_index] if file_type_index < len(normalized_lines) else ""
    current_token = current_line.split(",", 1)[0].strip().upper()
    aliases = {
        "ASCII": "ASCII",
        "A": "ASCII",
        "BINARY": "BINARY",
        "BINARY16": "BINARY",
        "BIN": "BINARY",
        "B": "BINARY",
        "BINARY32": "BINARY32",
        "B32": "BINARY32",
        "FLOAT32": "FLOAT32",
        "FLOAT": "FLOAT32",
        "F32": "FLOAT32",
    }
    file_type = aliases.get(current_token)

    if file_type is None:
        file_type = _infer_dat_file_type(dat_path)

    normalized_lines[file_type_index] = f"{file_type}\n"
    return normalized_lines


def _find_cfg_file_type_line_index(lines: list[str]):
    if len(lines) < 8:
        return None

    try:
        channel_parts = [part.strip().upper() for part in lines[1].split(",")]
        analog_count = 0
        digital_count = 0

        for part in channel_parts:
            if part.endswith("A"):
                analog_count = int(part[:-1] or 0)
            elif part.endswith("D"):
                digital_count = int(part[:-1] or 0)

        index = 2 + analog_count + digital_count

        # Frequency line.
        index += 1

        if index >= len(lines):
            return None

        nrates_text = lines[index].split(",", 1)[0].strip()
        nrates = int(float(nrates_text)) if nrates_text else 0
        if nrates <= 0:
            nrates = 1

        # Nrates line, sample-rate lines, start timestamp, trigger timestamp.
        index += 1 + nrates + 2

        if 0 <= index < len(lines):
            return index
    except Exception:
        return _find_cfg_file_type_line_index_by_heuristic(lines)

    return None


def _find_cfg_file_type_line_index_by_heuristic(lines: list[str]):
    supported = {"ASCII", "BINARY", "BINARY16", "BINARY32", "FLOAT", "FLOAT32", "BIN", "B32", "F32"}

    for index, line in enumerate(lines):
        token = line.split(",", 1)[0].strip().upper()
        if token in supported:
            return index

    return None


def _infer_dat_file_type(dat_path: str | None):
    if not dat_path:
        return "ASCII"

    try:
        with open(dat_path, "rb") as dat_file:
            sample = dat_file.read(512)

        if not sample:
            return "ASCII"

        if b"\x00" in sample:
            return "BINARY"

        text = sample.decode("ascii", errors="strict")
        first_line = text.splitlines()[0] if text.splitlines() else ""
        comma_count = first_line.count(",")

        if comma_count >= 2:
            return "ASCII"
    except Exception:
        return "BINARY"

    return "BINARY"


def _normalize_cfg_timestamp_line(line: str):
    """
    Ubah timestamp DD/MM/YYYY,HH:MM:SS.xxxxxx menjadi MM/DD/YYYY,...
    hanya jika komponen pertama > 12 dan komponen kedua valid sebagai bulan.
    """

    pattern = re.compile(r"^(\s*)(\d{1,2})/(\d{1,2})/(\d{4})(,.*)$")
    match = pattern.match(line)

    if not match:
        return line

    prefix, first, second, year, rest = match.groups()
    first_int = int(first)
    second_int = int(second)

    if first_int > 12 and 1 <= second_int <= 12:
        return f"{prefix}{second}/{first}/{year}{rest}"

    return line
