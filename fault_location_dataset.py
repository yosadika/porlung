"""Dataset kalibrasi lokasi gangguan untuk koreksi hasil SE/DE di masa depan.

Sheet `fault_location` menyimpan hasil kalkulasi aplikasi, parameter line yang
dipakai, dan label lapangan berupa jarak/tower/span aktual. Target ML tahap awal
adalah residual correction: actual_distance_km - de_distance_km.
"""

from fault_cause_dataset import make_case_id, upsert_row_to_gsheet


LOCATION_DATASET_SHEET_NAME = "fault_location"

LOCATION_DATASET_COLUMNS = [
    "case_id",
    "timestamp_analyzed",
    "fault_time_cfg",
    "line_name",
    "gi_local",
    "gi_remote",
    "upt_local",
    "ultg_local",
    "upt_remote",
    "ultg_remote",
    "segment",
    "fault_type_local",
    "fault_type_remote",
    "line_length_km",
    "line_length_source",
    "z1_r_ohm_per_km",
    "z1_x_ohm_per_km",
    "z0_r_ohm_per_km",
    "z0_x_ohm_per_km",
    "mixed_conductor_used",
    "mixed_conductor_sections",
    "se_local_km",
    "se_remote_from_remote_km",
    "se_remote_from_local_km",
    "de_raw_km",
    "de_raw_pct",
    "de_quality",
    "de_status",
    "tower_length_km",
    "tower_length_source",
    "actual_distance_km",
    "actual_distance_pct",
    "de_calculated_tower",
    "actual_tower_inspected",
    "actual_source",
    "field_notes",
    "de_error_km",
    "de_abs_error_km",
    "de_error_pct",
    "ml_ready",
]


def _f(value, default=0.0):
    try:
        return float(value if value not in (None, "") else default)
    except (TypeError, ValueError):
        return default


def _complex_parts(value):
    if value is None:
        return 0.0, 0.0
    try:
        return float(value.real), float(value.imag)
    except AttributeError:
        if isinstance(value, dict):
            return _f(value.get("real")), _f(value.get("imag"))
    return 0.0, 0.0


def _status_text(value):
    if isinstance(value, dict):
        return (
            value.get("primary_status")
            or value.get("scenario")
            or value.get("recommendation")
            or str(value)
        )
    return str(value or "")


def build_fault_location_feature_row(
    *,
    timestamp_analyzed: str,
    fault_time_cfg,
    line_param: dict,
    excel_impedance_data: dict,
    gi_local: str,
    gi_remote: str,
    upt_local: str,
    ultg_local: str,
    upt_remote: str,
    ultg_remote: str,
    segment: str,
    fault_type_local: str,
    fault_type_remote: str,
    single_result: dict,
    remote_single_result: dict,
    two_result: dict,
    two_quality: dict,
    two_status: str,
    tower_length_km,
    tower_length_source: str,
    actual_distance_km,
    de_calculated_tower: str,
    actual_tower_inspected: str,
    actual_source: str,
    field_notes: str,
) -> dict:
    lp = line_param or {}
    line_length = _f(lp.get("length_km"))
    z1_r, z1_x = _complex_parts(lp.get("Z1_per_km"))
    z0_r, z0_x = _complex_parts(lp.get("Z0_per_km"))
    actual_km = _f(actual_distance_km, None) if actual_distance_km not in (None, "") else ""
    de_km = (
        _f((two_result or {}).get("distance_from_original_local_km"))
        or _f((two_result or {}).get("distance_km"))
    )
    de_pct = (de_km / line_length * 100.0) if line_length > 0 else ""
    actual_pct = (float(actual_km) / line_length * 100.0) if actual_km != "" and line_length > 0 else ""
    de_error = (de_km - float(actual_km)) if actual_km != "" else ""
    mixed_sections = (excel_impedance_data or {}).get("mixed_conductor_sections") or []

    remote_se = _f((remote_single_result or {}).get("recommended_distance_km"))
    se_remote_from_local = (line_length - remote_se) if remote_single_result and line_length > 0 else ""

    return {
        "case_id": make_case_id(lp.get("line_name", ""), fault_time_cfg),
        "timestamp_analyzed": timestamp_analyzed,
        "fault_time_cfg": str(fault_time_cfg or ""),
        "line_name": lp.get("line_name", ""),
        "gi_local": gi_local or "",
        "gi_remote": gi_remote or "",
        "upt_local": upt_local or "",
        "ultg_local": ultg_local or "",
        "upt_remote": upt_remote or "",
        "ultg_remote": ultg_remote or "",
        "segment": segment or "",
        "fault_type_local": fault_type_local or "",
        "fault_type_remote": fault_type_remote or "",
        "line_length_km": round(line_length, 6) if line_length else "",
        "line_length_source": lp.get("length_source", ""),
        "z1_r_ohm_per_km": round(z1_r, 8),
        "z1_x_ohm_per_km": round(z1_x, 8),
        "z0_r_ohm_per_km": round(z0_r, 8),
        "z0_x_ohm_per_km": round(z0_x, 8),
        "mixed_conductor_used": int(bool(mixed_sections)),
        "mixed_conductor_sections": str(mixed_sections),
        "se_local_km": round(_f((single_result or {}).get("recommended_distance_km")), 6) if single_result else "",
        "se_remote_from_remote_km": round(remote_se, 6) if remote_single_result else "",
        "se_remote_from_local_km": round(se_remote_from_local, 6) if se_remote_from_local != "" else "",
        "de_raw_km": round(de_km, 6) if two_result else "",
        "de_raw_pct": round(de_pct, 4) if de_pct != "" else "",
        "de_quality": round(_f((two_quality or {}).get("quality_score")), 3) if two_quality else "",
        "de_status": _status_text(two_status),
        "tower_length_km": round(_f(tower_length_km), 6) if tower_length_km not in (None, "") else "",
        "tower_length_source": tower_length_source or "",
        "actual_distance_km": round(float(actual_km), 6) if actual_km != "" else "",
        "actual_distance_pct": round(actual_pct, 4) if actual_pct != "" else "",
        "de_calculated_tower": de_calculated_tower or "",
        "actual_tower_inspected": actual_tower_inspected or "",
        "actual_source": actual_source or "",
        "field_notes": field_notes or "",
        "de_error_km": round(de_error, 6) if de_error != "" else "",
        "de_abs_error_km": round(abs(de_error), 6) if de_error != "" else "",
        "de_error_pct": round(de_error / line_length * 100.0, 4) if de_error != "" and line_length > 0 else "",
        "ml_ready": int(actual_km != "" and bool(two_result)),
    }


def append_fault_location_row_to_gsheet(
    spreadsheet_url: str,
    row: dict,
    sheet_name: str = LOCATION_DATASET_SHEET_NAME,
):
    ok, msg, _ = upsert_row_to_gsheet(spreadsheet_url, row, LOCATION_DATASET_COLUMNS, sheet_name)
    return ok, msg
