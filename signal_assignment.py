import pandas as pd
import streamlit as st


def apply_signal_assignment(
    df: pd.DataFrame,
    va_channel: str,
    vb_channel: str,
    vc_channel: str,
    ia_channel: str,
    ib_channel: str,
    ic_channel: str,
    ie_channel: str | None = None,
    recorded_side: str = "secondary",
    ct_primary: float = 800.0,
    ct_secondary: float = 1.0,
    vt_primary: float = 150000.0,
    vt_secondary: float = 100.0,
    invert_voltage: bool = False,
    invert_current: bool = False,
):
    """
    Melakukan mapping channel COMTRADE menjadi nama standar:
    Va, Vb, Vc, Ia, Ib, Ic, IE.

    Jika recorded_side = secondary, nilai dikonversi ke primary.
    Jika recorded_side = primary, nilai dipakai langsung.

    invert_voltage=True  → semua Va/Vb/Vc dikali −1 (koreksi polaritas VT terbalik).
    invert_current=True  → semua Ia/Ib/Ic/IE dikali −1 (koreksi polaritas CT terbalik).
    """

    assigned = pd.DataFrame()
    assigned["time"] = df["time"]

    ctr = ct_primary / ct_secondary
    vtr = vt_primary / vt_secondary

    if recorded_side == "secondary":
        voltage_multiplier = vtr
        current_multiplier = ctr
    else:
        voltage_multiplier = 1.0
        current_multiplier = 1.0

    v_sign = -1.0 if invert_voltage else 1.0
    i_sign = -1.0 if invert_current else 1.0

    assigned["Va"] = df[va_channel] * voltage_multiplier * v_sign
    assigned["Vb"] = df[vb_channel] * voltage_multiplier * v_sign
    assigned["Vc"] = df[vc_channel] * voltage_multiplier * v_sign

    assigned["Ia"] = df[ia_channel] * current_multiplier * i_sign
    assigned["Ib"] = df[ib_channel] * current_multiplier * i_sign
    assigned["Ic"] = df[ic_channel] * current_multiplier * i_sign

    if ie_channel and ie_channel != "None":
        assigned["IE"] = df[ie_channel] * current_multiplier * i_sign
        assigned["IE_source"] = "measured"
    else:
        assigned["IE"] = assigned["Ia"] + assigned["Ib"] + assigned["Ic"]
        assigned["IE_source"] = "calculated_from_3_phase_currents"

    assigned["I0"] = assigned["IE"] / 3.0

    return assigned


def make_signal_assignment_cache_key(
    df: pd.DataFrame,
    *,
    va_channel: str,
    vb_channel: str,
    vc_channel: str,
    ia_channel: str,
    ib_channel: str,
    ic_channel: str,
    ie_channel: str | None = None,
    recorded_side: str = "secondary",
    ct_primary: float = 800.0,
    ct_secondary: float = 1.0,
    vt_primary: float = 150000.0,
    vt_secondary: float = 100.0,
    invert_voltage: bool = False,
    invert_current: bool = False,
):
    """Build a compact cache key for assignment settings and record identity."""
    time_series = df["time"] if "time" in df.columns and len(df) else None
    time_first = float(time_series.iloc[0]) if time_series is not None else None
    time_last = float(time_series.iloc[-1]) if time_series is not None else None
    return (
        len(df),
        tuple(df.columns),
        time_first,
        time_last,
        va_channel,
        vb_channel,
        vc_channel,
        ia_channel,
        ib_channel,
        ic_channel,
        ie_channel,
        recorded_side,
        round(float(ct_primary), 9),
        round(float(ct_secondary), 9),
        round(float(vt_primary), 9),
        round(float(vt_secondary), 9),
        bool(invert_voltage),
        bool(invert_current),
    )


def get_cached_signal_assignment(
    cache_key_name: str,
    cache_value_name: str,
    df: pd.DataFrame,
    **assignment_kwargs,
):
    """Reuse mapped waveform in session_state until record/settings change."""
    cache_key = make_signal_assignment_cache_key(df, **assignment_kwargs)
    if st.session_state.get(cache_key_name) == cache_key and cache_value_name in st.session_state:
        return st.session_state[cache_value_name], False

    assigned = apply_signal_assignment(df=df, **assignment_kwargs)
    st.session_state[cache_key_name] = cache_key
    st.session_state[cache_value_name] = assigned
    return assigned, True
