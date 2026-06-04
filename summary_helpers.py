import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from app_helpers import downsample_xy
from line_analysis_helpers import build_remote_single_signed_position
from waveform_helpers import fault_phase_to_current_channel, fault_phase_to_voltage_channel


def choose_summary_fault_signals(local_fault_type_result, remote_fault_type_result):
    fault_type = (
        (local_fault_type_result or {}).get("fault_type")
        or (remote_fault_type_result or {}).get("fault_type")
        or ""
    )

    voltage_channel = fault_phase_to_voltage_channel(fault_type) or "Va"
    current_channel = fault_phase_to_current_channel(fault_type) or "Ia"

    return fault_type, voltage_channel, current_channel


def build_summary_focus_waveform(
    local_df,
    remote_df,
    local_fault_window,
    remote_fault_window,
    channel,
    title,
    seconds_before=0.08,
    seconds_after=0.12,
    remote_time_shift_s=0.0,
):
    fig = go.Figure()

    if local_df is not None and local_fault_window is not None and channel in local_df.columns:
        local_time = local_df["time"] - local_fault_window["fault_time"]
        local_mask = (local_time >= -seconds_before) & (local_time <= seconds_after)
        local_x, local_y = downsample_xy(local_time[local_mask], local_df.loc[local_mask, channel])
        fig.add_trace(
            go.Scatter(
                x=local_x,
                y=local_y,
                mode="lines",
                name=f"Local {channel}",
                line=dict(width=1.4),
            )
        )

    if remote_df is not None and remote_fault_window is not None and channel in remote_df.columns:
        remote_time = remote_df["time"] - remote_fault_window["fault_time"] + remote_time_shift_s
        remote_mask = (remote_time >= -seconds_before) & (remote_time <= seconds_after)
        remote_x, remote_y = downsample_xy(remote_time[remote_mask], remote_df.loc[remote_mask, channel])
        fig.add_trace(
            go.Scatter(
                x=remote_x,
                y=remote_y,
                mode="lines",
                name=f"Remote {channel}",
                line=dict(width=1.4, dash="dash"),
            )
        )

    fig.add_vline(
        x=0.0,
        line_dash="solid",
        annotation_text="Fault",
        annotation_position="top",
    )

    fig.update_layout(
        title=title,
        xaxis_title="Aligned Time from Fault (s)",
        yaxis_title="Instantaneous Primary Magnitude",
        legend_title="Signal",
        xaxis=dict(range=[-seconds_before, seconds_after], autorange=False),
    )

    return fig


def estimate_summary_disturbance_cause(
    fault_type_result,
    high_resistance_result,
    phasors=None,
    prefault_phasors=None,
    single_result=None,
    two_result=None,
    two_quality=None,
    line_param=None,
):
    # single_result, two_result, two_quality, line_param reserved for future use
    """Kembalikan (cause_label: str, detail: dict) berisi basis, penjelasan, referensi, dan catatan."""
    fault_type   = str((fault_type_result or {}).get("fault_type", "")).upper()
    hr_suspected = bool((high_resistance_result or {}).get("high_resistance_suspected"))
    rf_est       = float((high_resistance_result or {}).get("Rf_est_ohm") or 0.0)
    ft_metrics   = (fault_type_result or {}).get("metrics", {}) or {}
    ft_conf      = float((fault_type_result or {}).get("confidence", 0.0))
    line_len     = float((line_param or {}).get("length_km") or 0.0)

    # ── helper: ambil magnitude phasor ────────────────────────────────
    def _mag(d, key):
        return float((d or {}).get(key, {}).get("magnitude") or 0.0)

    def _num_basis(extra: list) -> list:
        """Tambah data numerik fault ke basis jika tersedia."""
        def _row(p, v):
            return {"Parameter": p, "Nilai": v}

        rows = list(extra)  # extra sudah berupa list of {"Parameter", "Nilai"}

        if ft_conf > 0:
            rows.append(_row("Keyakinan Klasifikasi Fault Type", f"{ft_conf:.1f} / 10"))

        # Arus dan tegangan fasa terganggu vs pre-fault
        faulted_phases = (fault_type_result or {}).get("faulted_phases", [])
        for ph in faulted_phases[:2]:
            i_key = f"I{ph.lower()}" if ph in "ABC" else None
            v_key = f"V{ph.lower()}" if ph in "ABC" else None
            if i_key:
                i_fault = _mag(phasors, i_key)
                i_pre   = _mag(prefault_phasors, i_key)
                v_fault = _mag(phasors, v_key) if v_key else 0.0
                v_pre   = _mag(prefault_phasors, v_key) if v_key else 0.0
                if i_fault > 0:
                    i_ratio = (i_fault / i_pre * 100 - 100) if i_pre > 0 else 0.0
                    i_str = f"{i_fault:,.1f} A (fault)"
                    if i_pre > 0:
                        i_str += f"  ←  {i_pre:,.1f} A (pre-fault),  naik +{i_ratio:.0f}%"
                    rows.append(_row(f"Arus Fasa {ph}", i_str))
                if v_fault > 0 and v_pre > 0:
                    v_drop = (1 - v_fault / v_pre) * 100
                    rows.append(_row(
                        f"Tegangan Fasa {ph}",
                        f"{v_fault / 1000:.2f} kV (fault)  ←  {v_pre / 1000:.2f} kV (pre-fault),  turun {v_drop:.1f}%",
                    ))

        # IE / arus netral
        ie_fault = _mag(phasors, "IE")
        ie_pre   = _mag(prefault_phasors, "IE")
        if ie_fault > 0:
            ie_str = f"{ie_fault:,.1f} A (fault)"
            if ie_pre > 0:
                ie_str += f"  ←  {ie_pre:,.1f} A (pre-fault)"
            rows.append(_row("Arus Netral IE", ie_str))

        return rows

    if hr_suspected:
        _hr_angle = float((high_resistance_result or {}).get("angle_deviation_deg") or 0.0)
        _hr_conf  = float((high_resistance_result or {}).get("analysis_confidence") or 0.0)
        return (
            "Pohon / Benda Asing",
            {
                "basis": _num_basis([
                    {"Parameter": "Fault Type Terdeteksi", "Nilai": fault_type or "tidak terdeteksi"},
                    {"Parameter": "Resistansi Gangguan (Rf)", "Nilai": f"{rf_est:.1f} Ω — melewati threshold high-resistance"},
                    {"Parameter": "Deviasi Sudut Impedansi vs Z₁", "Nilai": f"{_hr_angle:.1f}°"},
                    {"Parameter": "Keyakinan Analisis HR", "Nilai": f"{_hr_conf:.1f} / 10"},
                ]),
                "explanation": (
                    "Gangguan dengan resistansi tinggi umumnya disebabkan kontak pohon, benda asing konduktif, "
                    "atau tanah kering/berpasir di titik gangguan. Busur api yang panjang juga dapat menghasilkan "
                    "Rf yang tinggi pada gangguan fase-ke-tanah."
                ),
                "references": (
                    "Saha et al. (2010) Ch. 6 — high-resistance fault analysis; "
                    "IEEE Std C37.114-2014 Sec. 5.4 — resistive fault detection"
                ),
                "note": (
                    "Validasi dengan inspeksi lapangan dan data cuaca. "
                    "Rf tinggi bukan bukti mutlak pohon — bisa juga benda asing, busur api panjang, atau kondisi tanah."
                ),
            },
        )

    if fault_type in ["ABC", "ABCG", "3PH", "3P"]:
        return (
            "Power Swing / Gangguan 3 Fasa",
            {
                "basis": _num_basis([
                    {"Parameter": "Fault Type Terdeteksi", "Nilai": f"{fault_type} — ketiga fasa terganggu bersamaan"},
                    {"Parameter": "Karakteristik", "Nilai": "Gangguan simetris 3 fasa jarang disebabkan petir — lebih sering akibat power swing atau eskalasi fault"},
                ]),
                "explanation": (
                    "Gangguan tiga fasa simetris dapat disebabkan oleh power swing yang berujung kehilangan sinkronisasi, "
                    "atau ground fault satu fasa yang berkembang menjadi 3 fasa. "
                    "Perlu diverifikasi dengan event relay, catatan osilasi daya, dan riwayat pembebanan sistem."
                ),
                "references": (
                    "Anderson (1995) Analysis of Faulted Power Systems Ch. 10; "
                    "IEEE Std C37.114-2014 Sec. 5.5"
                ),
                "note": (
                    "Bandingkan dengan event CB (Circuit Breaker / pemutus tenaga), SOE (Sequence of Events / log urutan kejadian relay), "
                    "dan kondisi sistem saat kejadian untuk memastikan penyebab."
                ),
            },
        )

    if "G" in fault_type and any(phase in fault_type for phase in ["A", "B", "C"]):
        _n_phases = sum(1 for c in fault_type if c in "ABC")
        if _n_phases == 1:
            return (
                "Petir / Flashover Satu Fasa ke Tanah",
                {
                    "basis": _num_basis([
                        {"Parameter": "Fault Type Terdeteksi", "Nilai": f"{fault_type} — gangguan satu fasa ke tanah"},
                        {"Parameter": "Resistansi Gangguan (Rf)", "Nilai": f"{'≈ ' + str(round(rf_est, 1)) + ' Ω — ' if rf_est > 0 else ''}rendah/normal, tidak ada indikasi high-resistance"},
                        {"Parameter": "Statistik", "Nilai": "SLG (Single Line-to-Ground) ≈ 70–80% dari total gangguan transmisi"},
                    ]),
                    "explanation": (
                        "Gangguan satu fasa ke tanah dengan impedansi rendah paling sering disebabkan flashover "
                        "akibat sambaran petir langsung atau induksi, atau kontak benda asing konduktif yang singkat. "
                        "Durasi gangguan singkat dan reclosing berhasil mendukung hipotesis flashover petir."
                    ),
                    "references": (
                        "IEEE Std C37.114-2014 Sec. 3.1 — fault classification; "
                        "Saha et al. (2010) Ch. 2 — SLG (Single Line-to-Ground) fault statistics and characteristics"
                    ),
                    "note": (
                        "Konfirmasi dengan data sambaran petir (lightning arrester counter, BMKG/weather data) "
                        "dan hasil inspeksi tower di titik gangguan."
                    ),
                },
            )
        else:
            return (
                "Gangguan Multi-Fasa ke Tanah",
                {
                    "basis": _num_basis([
                        {"Parameter": "Fault Type Terdeteksi", "Nilai": f"{fault_type} — lebih dari satu fasa terganggu ke tanah"},
                        {"Parameter": "Kemungkinan Skenario", "Nilai": "SLG yang berkembang, flashover multi-fasa, atau dua gangguan bersamaan"},
                    ]),
                    "explanation": (
                        "Gangguan dua fasa ke tanah lebih jarang dari SLG (Single Line-to-Ground) dan bisa merupakan eskalasi dari gangguan satu fasa, "
                        "atau akibat sambaran petir yang memengaruhi lebih dari satu konduktor bersamaan."
                    ),
                    "references": (
                        "IEEE Std C37.114-2014 Sec. 3.1; "
                        "Anderson (1995) Analysis of Faulted Power Systems Ch. 9"
                    ),
                    "note": "Periksa apakah ada dua titik gangguan terpisah atau satu lokasi gangguan multi-fasa.",
                },
            )

    return (
        "Belum Dapat Ditentukan",
        {
            "basis": _num_basis([
                {"Parameter": "Fault Type", "Nilai": fault_type or "tidak terdeteksi"},
                {"Parameter": "Status", "Nilai": "Pola impedansi dan fault type belum cukup untuk klasifikasi otomatis"},
            ]),
            "explanation": (
                "Data yang tersedia belum memberikan pola yang kuat untuk menentukan penyebab gangguan secara otomatis."
            ),
            "references": "",
            "note": (
                "Lakukan analisis manual dengan mempertimbangkan data cuaca, riwayat gangguan, dan inspeksi lapangan."
            ),
        },
    )


def single_ended_plot_score(single_result):
    if not single_result:
        return 0.0
    base_score = {
        "VALID": 9.0,
        "CHECK": 6.0,
        "UNCERTAIN": 3.0,
    }.get(str(single_result.get("status", "")).upper(), 5.0)
    warning_count = len(single_result.get("warnings", []) or [])
    return max(0.0, min(10.0, base_score - 0.4 * warning_count))


def build_summary_location_plot(
    line_param,
    local_gi_label,
    remote_gi_label,
    single_result,
    remote_single_result,
    two_result,
    reverse_two_result,
):
    if not line_param:
        return None

    line_length = float(line_param.get("length_km", 0.0) or 0.0)
    if line_length <= 0:
        return None

    points = []

    if single_result:
        points.append(
            {
                "label": f"SE {local_gi_label}",
                "distance": float(single_result.get("recommended_distance_km", 0.0)),
                "score": single_ended_plot_score(single_result),
                "symbol": "circle",
                "color": "#009e73",
            }
        )

    if remote_single_result:
        remote_position = build_remote_single_signed_position(
            line_length_km=line_length,
            remote_single_result=remote_single_result,
            scenario=st.session_state.get("two_ended_fault_scenario", "normal_internal_line_fault"),
            two_result=two_result,
        )
        points.append(
            {
                "label": f"SE {remote_gi_label}",
                "distance": remote_position["distance_from_local_km"],
                "score": single_ended_plot_score(remote_single_result),
                "symbol": "circle",
                "color": "#e67300",
            }
        )

    if two_result:
        points.append(
            {
                "label": f"DE {line_param.get('line_name', 'Original')}",
                "distance": float(two_result.get("distance_from_original_local_km", two_result.get("distance_km", 0.0))),
                "score": float(st.session_state.get("two_ended_quality", {}).get("quality_score", 10.0)),
                "symbol": "diamond",
                "color": "#2563eb",
            }
        )

    if reverse_two_result:
        points.append(
            {
                "label": f"DE {remote_gi_label}-{local_gi_label}",
                "distance": float(reverse_two_result.get("distance_from_original_local_km", reverse_two_result.get("distance_km", 0.0))),
                "score": float(st.session_state.get("two_ended_reverse_quality", {}).get("quality_score", 10.0)),
                "symbol": "diamond",
                "color": "#7c3aed",
            }
        )

    if not points:
        return None

    point_distances = [float(point["distance"]) for point in points]
    external_padding = max(0.05 * line_length, 1.0)
    x_min = min(0.0, min(point_distances) - external_padding)
    x_max = max(line_length, max(point_distances) + external_padding)

    marker_rows = []
    for point in points:
        distance = float(point["distance"])
        score = max(0.0, min(10.0, float(point["score"])))
        track = "Double-ended" if str(point["label"]).startswith("DE ") else "Single-ended"
        marker_rows.append(
            {
                "Point": point["label"],
                "Distance km": distance,
                "Distance %": 100.0 * distance / line_length,
                "Score": score,
                "Track": track,
                "Color": point["color"],
                "Symbol": point["symbol"],
                "Legend Name": point["label"],
            }
        )

    sorted_marker_rows = sorted(marker_rows, key=lambda item: float(item["Distance km"]))
    min_gap_km = max(0.02 * line_length, 0.75)
    grouped_marker_rows = []

    for row in sorted_marker_rows:
        if (
            not grouped_marker_rows
            or abs(
                float(row["Distance km"])
                - float(grouped_marker_rows[-1][-1]["Distance km"])
            )
            >= min_gap_km
        ):
            grouped_marker_rows.append([row])
        else:
            grouped_marker_rows[-1].append(row)

    label_layout = {}
    double_slots = [
        (-64, -160),
        (-64, 160),
        (-100, -160),
        (-100, 160),
    ]
    single_slots = [
        (96, -190),
        (96, 190),
        (150, -190),
        (150, 190),
    ]

    for group in grouped_marker_rows:
        double_rows = [row for row in group if row["Track"] == "Double-ended"]
        single_rows = [row for row in group if row["Track"] == "Single-ended"]

        if len(group) == 1:
            row = group[0]
            label_layout[id(row)] = (
                (-64, 0) if row["Track"] == "Double-ended" else (108, 0)
            )
        else:
            for index, row in enumerate(double_rows):
                label_layout[id(row)] = double_slots[index % len(double_slots)]

            for index, row in enumerate(single_rows):
                label_layout[id(row)] = single_slots[index % len(single_slots)]

    for row in marker_rows:
        _d_remote = line_length - row["Distance km"]
        _p_remote = _d_remote / line_length * 100.0 if line_length > 0 else 0.0
        row["Label"] = (
            f"<b>{row['Point']}</b><br>"
            f"{row['Distance km']:.2f} km ({row['Distance %']:.1f}%) dari {local_gi_label}<br>"
            f"{_d_remote:.2f} km ({_p_remote:.1f}%) dari {remote_gi_label}<br>"
            f"{row['Score']:.1f}/10"
        )
        row["Annotation Ay"], row["Annotation Ax"] = label_layout.get(
            id(row),
            (-64, 0) if row["Track"] == "Double-ended" else (108, 0),
        )

    marker_df = pd.DataFrame(marker_rows)
    x_profile = [
        x_min + i * (x_max - x_min) / 300.0
        for i in range(301)
    ]

    theme_base = st.get_option("theme.base")
    theme_background = st.get_option("theme.backgroundColor")
    if theme_base is None and theme_background:
        bg = str(theme_background).lstrip("#")
        if len(bg) >= 6:
            r = int(bg[0:2], 16)
            g = int(bg[2:4], 16)
            b = int(bg[4:6], 16)
            is_dark_theme = (0.2126 * r + 0.7152 * g + 0.0722 * b) < 128
        else:
            is_dark_theme = False
    else:
        is_dark_theme = theme_base == "dark"

    plot_template = "plotly_dark" if is_dark_theme else "plotly_white"
    plot_bg = "#0b1220" if is_dark_theme else "#ffffff"
    text_color = "#f8fafc" if is_dark_theme else "#111827"
    muted_text_color = "#cbd5e1" if is_dark_theme else "#475569"
    axis_title_color = "#f8fafc" if is_dark_theme else "#0f172a"
    annotation_bg = "rgba(15,23,42,0.92)" if is_dark_theme else "rgba(255,255,255,0.96)"
    annotation_border = "#94a3b8" if is_dark_theme else "#cbd5e1"
    terminal_color = "#f8fafc" if is_dark_theme else "#111827"

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.18, 0.82],
        vertical_spacing=0.08,
    )

    fig.add_shape(
        type="line",
        x0=0,
        x1=line_length,
        y0=0.5,
        y1=0.5,
        line=dict(color=muted_text_color, width=2),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=[0, line_length],
            y=[0.5, 0.5],
            mode="markers",
            marker=dict(size=12, color=[terminal_color, terminal_color], symbol="square"),
            hoverinfo="skip",
            showlegend=False,
        ),
        row=1,
        col=1,
    )
    fig.add_annotation(
        x=0,
        y=0.5,
        text=local_gi_label,
        showarrow=False,
        xanchor="left",
        yanchor="bottom",
        xshift=8,
        yshift=12,
        font=dict(color=text_color, size=13),
        row=1,
        col=1,
    )
    fig.add_annotation(
        x=line_length,
        y=0.5,
        text=remote_gi_label,
        showarrow=False,
        xanchor="right",
        yanchor="bottom",
        xshift=-8,
        yshift=12,
        font=dict(color=text_color, size=13),
        row=1,
        col=1,
    )

    for _, row in marker_df.sort_values(["Distance km", "Track"]).iterrows():
        fig.add_trace(
            go.Scatter(
                x=[row["Distance km"]],
                y=[0.5],
                mode="markers",
                marker=dict(
                    size=13,
                    color=row["Color"],
                    symbol=row["Symbol"],
                    line=dict(width=2, color=terminal_color),
                ),
                name=row["Legend Name"],
                legendgroup=row["Point"],
                showlegend=True,
                hovertemplate=(
                    f"{row['Point']}<br>"
                    f"{row['Distance km']:.2f} km ({row['Distance %']:.1f}%)<br>"
                    f"Score {row['Score']:.1f}/10"
                    "<extra></extra>"
                ),
            ),
            row=1,
            col=1,
        )

    for _, row in marker_df.iterrows():
        center = float(row["Distance km"])
        score = float(row["Score"])
        curve_width = max(line_length * (0.09 if row["Track"] == "Double-ended" else 0.06), 2.5)
        curve_y = [
            score / (1.0 + abs(x - center) / curve_width)
            for x in x_profile
        ]

        fig.add_trace(
            go.Scatter(
                x=x_profile,
                y=curve_y,
                mode="lines",
                line=dict(color=row["Color"], width=1.5),
                opacity=0.9,
                hoverinfo="skip",
                legendgroup=row["Point"],
                showlegend=False,
            ),
            row=2,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=[row["Distance km"]],
                y=[score],
                mode="markers",
                marker=dict(
                    size=16,
                    color=row["Color"],
                    symbol=row["Symbol"],
                    line=dict(width=2, color=terminal_color),
                ),
                name=row["Legend Name"],
                showlegend=False,
                legendgroup=row["Point"],
                customdata=[[row["Point"], row["Distance km"], row["Distance %"], row["Score"]]],
                hovertemplate=(
                    "%{customdata[0]}<br>"
                    "%{customdata[1]:.2f} km (%{customdata[2]:.1f}%)<br>"
                    "Score %{customdata[3]:.1f}/10"
                    "<extra></extra>"
                ),
            ),
            row=2,
            col=1,
        )
        fig.add_shape(
            type="line",
            x0=row["Distance km"],
            x1=row["Distance km"],
            y0=0,
            y1=score,
            line=dict(color=row["Color"], width=1.4),
            row=2,
            col=1,
        )

        fig.add_annotation(
            x=row["Distance km"],
            y=score,
            text=row["Label"],
            showarrow=True,
            arrowhead=2,
            arrowsize=0.8,
            arrowwidth=1.4,
            arrowcolor=row["Color"],
            ax=row["Annotation Ax"],
            ay=row["Annotation Ay"],
            bgcolor=annotation_bg,
            bordercolor=annotation_border,
            borderwidth=1,
            borderpad=4,
            font=dict(color=text_color, size=11),
            row=2,
            col=1,
        )

    fig.update_layout(
        title=f"Grafik SE dan DE - {line_param.get('line_name', '')}",
        template=plot_template,
        paper_bgcolor=plot_bg,
        plot_bgcolor=plot_bg,
        font=dict(color=text_color),
        height=800,
        margin=dict(l=58, r=34, t=118, b=92),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.12,
            xanchor="right",
            x=1,
            bgcolor="rgba(15,23,42,0.85)" if is_dark_theme else "rgba(255,255,255,0.90)",
            bordercolor="#475569" if is_dark_theme else "#cbd5e1",
            borderwidth=1,
            font=dict(color=text_color),
        ),
    )
    fig.update_xaxes(
        range=[x_min, x_max],
        autorange=False,
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        color=text_color,
        row=1,
        col=1,
    )
    fig.update_yaxes(
        range=[0.0, 1.0],
        autorange=False,
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        color=text_color,
        row=1,
        col=1,
    )
    fig.update_xaxes(
        title=dict(
            text=f"Distance from {local_gi_label} (km)",
            font=dict(color=axis_title_color),
        ),
        range=[x_min, x_max],
        autorange=False,
        zeroline=False,
        color=text_color,
        tickfont=dict(color=muted_text_color),
        gridcolor="rgba(148,163,184,0.22)" if is_dark_theme else "rgba(148,163,184,0.35)",
        row=2,
        col=1,
    )
    fig.update_yaxes(
        title=dict(
            text="Quality / Confidence (0-10)",
            font=dict(color=axis_title_color),
        ),
        range=[-0.4, 11.4],
        showgrid=True,
        gridcolor="rgba(148,163,184,0.14)" if is_dark_theme else "rgba(148,163,184,0.22)",
        zeroline=False,
        color=text_color,
        tickfont=dict(color=muted_text_color),
        row=2,
        col=1,
    )

    return fig
