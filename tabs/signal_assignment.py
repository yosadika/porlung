import math

import streamlit as st

from signal_assignment import get_cached_signal_assignment


def render(df):
    st.subheader("Signal Assignment")

    st.write(
        "Pilih channel asli dari file COMTRADE, lalu mapping ke variabel standar aplikasi."
    )

    channel_options = [col for col in df.columns if col != "time"]
    ground_options = ["None"] + channel_options

    channel_sets = st.session_state.get("channel_sets", {})
    voltage_sets = channel_sets.get("voltage_sets", [])
    current_sets = channel_sets.get("current_sets", [])
    ground_candidates = channel_sets.get("ground_candidates", [])

    auto_assignment = st.session_state.get("auto_assignment", {})
    auto_transformer_data = st.session_state.get("auto_transformer_data", {})
    auto_recorded_side = st.session_state.get("auto_recorded_side", "secondary")

    if voltage_sets:
        voltage_set_labels = [item["label"] for item in voltage_sets]
    else:
        voltage_set_labels = ["Manual Selection"]

    if current_sets:
        current_set_labels = [item["label"] for item in current_sets]
    else:
        current_set_labels = ["Manual Selection"]

    def get_selected_set_by_label(channel_set_list, selected_label):
        for item in channel_set_list:
            if item["label"] == selected_label:
                return item
        return None

    def get_channel_index(channel_name, options, default_index=0):
        if channel_name in options:
            return options.index(channel_name)
        return default_index

    def get_ground_index(channel_name, options):
        if channel_name in options:
            return options.index(channel_name)
        return 0

    def seed_choice(key, options, preferred, fallback_index=0):
        if st.session_state.get(key) not in options:
            fallback_index = min(max(int(fallback_index), 0), max(len(options) - 1, 0))
            st.session_state[key] = preferred if preferred in options else options[fallback_index]

    def seed_value(key, value):
        if key not in st.session_state:
            st.session_state[key] = value

    with st.form("local_signal_assignment_form"):
        st.markdown("### Auto Detected Channel Sets")
        col_set1, col_set2 = st.columns(2)

        seed_choice(
            "selected_voltage_set_label",
            ["Manual Selection"] + voltage_set_labels,
            voltage_set_labels[0] if voltage_sets else "Manual Selection",
            1 if voltage_sets else 0,
        )
        seed_choice(
            "selected_current_set_label",
            ["Manual Selection"] + current_set_labels,
            current_set_labels[0] if current_sets else "Manual Selection",
            1 if current_sets else 0,
        )

        with col_set1:
            selected_voltage_set_label = st.selectbox(
                "Pilih Set Tegangan 3 Fasa",
                ["Manual Selection"] + voltage_set_labels,
                key="selected_voltage_set_label",
            )

        with col_set2:
            selected_current_set_label = st.selectbox(
                "Pilih Set Arus 3 Fasa",
                ["Manual Selection"] + current_set_labels,
                key="selected_current_set_label",
            )

        selected_voltage_set = get_selected_set_by_label(
            voltage_sets,
            selected_voltage_set_label,
        )
        selected_current_set = get_selected_set_by_label(
            current_sets,
            selected_current_set_label,
        )

        if selected_voltage_set:
            default_va = selected_voltage_set["A"]
            default_vb = selected_voltage_set["B"]
            default_vc = selected_voltage_set["C"]
        else:
            default_va = auto_assignment.get("Va")
            default_vb = auto_assignment.get("Vb")
            default_vc = auto_assignment.get("Vc")

        if selected_current_set:
            default_ia = selected_current_set["A"]
            default_ib = selected_current_set["B"]
            default_ic = selected_current_set["C"]
        else:
            default_ia = auto_assignment.get("Ia")
            default_ib = auto_assignment.get("Ib")
            default_ic = auto_assignment.get("Ic")

        if ground_candidates:
            default_ie = ground_candidates[0]["channel"]
        else:
            default_ie = auto_assignment.get("IE")

        seed_choice("local_signal_va", channel_options, default_va, 0)
        seed_choice("local_signal_vb", channel_options, default_vb, 1 if len(channel_options) > 1 else 0)
        seed_choice("local_signal_vc", channel_options, default_vc, 2 if len(channel_options) > 2 else 0)
        seed_choice("local_signal_ia", channel_options, default_ia, 3 if len(channel_options) > 3 else 0)
        seed_choice("local_signal_ib", channel_options, default_ib, 4 if len(channel_options) > 4 else 0)
        seed_choice("local_signal_ic", channel_options, default_ic, 5 if len(channel_options) > 5 else 0)
        seed_choice("local_signal_ie", ground_options, default_ie, 0)
        seed_choice("local_signal_recorded_side", ["secondary", "primary"], auto_recorded_side, 0)
        seed_value("local_signal_ct_primary", float(auto_transformer_data.get("ct_primary", 800.0)))
        seed_value("local_signal_ct_secondary", float(auto_transformer_data.get("ct_secondary", 1.0)))
        seed_value("local_signal_vt_primary", float(auto_transformer_data.get("vt_primary", 150000.0)))
        seed_value("local_signal_vt_secondary", float(auto_transformer_data.get("vt_secondary", 100.0)))

        st.markdown("### Voltage Channel Assignment")
        col_v1, col_v2, col_v3 = st.columns(3)

        with col_v1:
            va_channel = st.selectbox(
                "Va / VL1",
                channel_options,
                key="local_signal_va",
            )

        with col_v2:
            vb_channel = st.selectbox(
                "Vb / VL2",
                channel_options,
                key="local_signal_vb",
            )

        with col_v3:
            vc_channel = st.selectbox(
                "Vc / VL3",
                channel_options,
                key="local_signal_vc",
            )

        st.markdown("### Current Channel Assignment")
        col_i1, col_i2, col_i3 = st.columns(3)

        default_ia_index = 3 if len(channel_options) > 3 else 0
        default_ib_index = 4 if len(channel_options) > 4 else 0
        default_ic_index = 5 if len(channel_options) > 5 else 0

        with col_i1:
            ia_channel = st.selectbox(
                "Ia / IL1",
                channel_options,
                key="local_signal_ia",
            )

        with col_i2:
            ib_channel = st.selectbox(
                "Ib / IL2",
                channel_options,
                key="local_signal_ib",
            )

        with col_i3:
            ic_channel = st.selectbox(
                "Ic / IL3",
                channel_options,
                key="local_signal_ic",
            )

        st.markdown("### Ground Current Assignment")
        ie_channel = st.selectbox(
            "IE / IN / 3I0 jika tersedia",
            ground_options,
            key="local_signal_ie",
        )

        if ie_channel != "None":
            st.success(f"Channel arus netral/ground terdeteksi dan dipakai: {ie_channel}")
        else:
            st.info("Channel IE/IN/3I0 tidak dipilih. Aplikasi akan menghitung IE residual dari Ia + Ib + Ic.")

        st.markdown("### Koreksi Polaritas")
        st.caption(
            "Aktifkan bila polaritas VT atau CT terpasang terbalik pada perekam (P/N tertukar). "
            "Perubahan diterapkan setelah tombol Apply ditekan."
        )
        col_pol1, col_pol2 = st.columns(2)
        with col_pol1:
            invert_voltage = st.checkbox(
                "Balik Polaritas Tegangan (Va, Vb, Vc) x -1",
                key="local_invert_voltage",
            )
        with col_pol2:
            invert_current = st.checkbox(
                "Balik Polaritas Arus (Ia, Ib, Ic, IE) x -1",
                key="local_invert_current",
            )

        st.markdown("### Transformer Data")
        recorded_side_options = ["secondary", "primary"]
        recorded_side_default_index = (
            recorded_side_options.index(auto_recorded_side)
            if auto_recorded_side in recorded_side_options
            else 0
        )

        recorded_side = st.radio(
            "Nilai pada file COMTRADE direkam sebagai:",
            recorded_side_options,
            horizontal=True,
            key="local_signal_recorded_side",
        )

        col_ct1, col_ct2, col_vt1, col_vt2 = st.columns(4)

        with col_ct1:
            ct_primary = st.number_input(
                "CT Primary (A)",
                step=0.001,
                format="%.5f",
                key="local_signal_ct_primary",
            )

        with col_ct2:
            ct_secondary = st.number_input(
                "CT Secondary (A)",
                step=0.001,
                format="%.5f",
                key="local_signal_ct_secondary",
            )

        with col_vt1:
            vt_primary = st.number_input(
                "VT/CVT Primary (V)",
                step=0.001,
                format="%.5f",
                key="local_signal_vt_primary",
            )

        with col_vt2:
            vt_secondary = st.number_input(
                "VT/CVT Secondary (V)",
                step=0.001,
                format="%.5f",
                key="local_signal_vt_secondary",
            )

        st.caption(
            f"Auto ratio source: CT = {auto_transformer_data.get('ct_ratio_source', '-')}, "
            f"VT = {auto_transformer_data.get('vt_ratio_source', '-')}. "
            "Tetap validasi manual karena tidak semua file CFG menyimpan primary/secondary dengan benar."
        )

        if recorded_side == "primary":
            st.info(
                "Mode primary aktif: nilai COMTRADE dianggap sudah dalam satuan primer, sehingga rasio CT/VT "
                "tidak dikalikan lagi pada waveform. Field CT/VT tetap ditampilkan untuk dokumentasi dan validasi."
            )
        else:
            st.info(
                "Mode secondary aktif: waveform akan dikalikan rasio CT/VT agar menjadi nilai primer. "
                "Pastikan VT/CVT Primary memakai tegangan primer nominal, misalnya 150000 V untuk sistem 150 kV, "
                "bukan 1500 jika yang dimaksud adalah rasio 1500:1."
            )

        apply_clicked = st.form_submit_button(
            "Apply Signal Assignment",
            width="stretch",
        )

    selected_assignment_channels = [
        va_channel,
        vb_channel,
        vc_channel,
        ia_channel,
        ib_channel,
        ic_channel,
    ]
    duplicate_channels = [
        ch for ch in selected_assignment_channels
        if selected_assignment_channels.count(ch) > 1
    ]

    if duplicate_channels:
        st.error(
            "Ada channel yang dipilih lebih dari satu kali pada Va/Vb/Vc/Ia/Ib/Ic: "
            + ", ".join(sorted(set(duplicate_channels)))
            + ". Periksa kembali Signal Assignment."
        )
        return

    st.success("Signal Assignment Va/Vb/Vc/Ia/Ib/Ic tidak memiliki duplikasi channel.")
    st.info(
        "Jika IE/IN tidak dipilih, aplikasi akan menghitung residual current: "
        "IE = Ia + Ib + Ic, lalu I0 = IE / 3."
    )

    should_apply = apply_clicked or "assigned_df" not in st.session_state
    if should_apply:
        assigned_df, rebuilt = get_cached_signal_assignment(
            "local_signal_assignment_cache_key",
            "assigned_df",
            df,
            va_channel=va_channel,
            vb_channel=vb_channel,
            vc_channel=vc_channel,
            ia_channel=ia_channel,
            ib_channel=ib_channel,
            ic_channel=ic_channel,
            ie_channel=ie_channel,
            recorded_side=recorded_side,
            ct_primary=ct_primary,
            ct_secondary=ct_secondary,
            vt_primary=vt_primary,
            vt_secondary=vt_secondary,
            invert_voltage=invert_voltage,
            invert_current=invert_current,
        )
        st.session_state["local_transformer_data"] = {
            "recorded_side": recorded_side,
            "ct_primary": ct_primary,
            "ct_secondary": ct_secondary,
            "vt_primary": vt_primary,
            "vt_secondary": vt_secondary,
            "invert_voltage": invert_voltage,
            "invert_current": invert_current,
            "nominal_phase_voltage_rms": vt_primary / math.sqrt(3.0),
            "nominal_current_rms": ct_primary,
        }
        st.session_state["local_ie_channel"] = ie_channel if ie_channel != "None" else None
        st.session_state["local_ie_source"] = (
            "measured" if ie_channel != "None" else "calculated_from_3_phase_currents"
        )
        st.success("Signal assignment berhasil diterapkan." if rebuilt else "Signal assignment memakai cache.")
    else:
        assigned_df = st.session_state.get("assigned_df")
        st.caption("Perubahan form belum diterapkan. Tekan Apply Signal Assignment untuk memperbarui waveform dan hasil downstream.")

    if assigned_df is None:
        return

    st.subheader("Preview Data Setelah Mapping")
    st.dataframe(assigned_df.head(20), width="stretch")

    st.subheader("Ringkasan Mapping Aktif")
    active_transformer = st.session_state.get("local_transformer_data", {})
    mapping_summary = {
        "Voltage Set": selected_voltage_set_label,
        "Current Set": selected_current_set_label,
        "Va": va_channel,
        "Vb": vb_channel,
        "Vc": vc_channel,
        "Ia": ia_channel,
        "Ib": ib_channel,
        "Ic": ic_channel,
        "IE": ie_channel if ie_channel != "None" else "Calculated: Ia + Ib + Ic",
        "Recorded Side": active_transformer.get("recorded_side", recorded_side),
        "CT Ratio": f"{active_transformer.get('ct_primary', ct_primary)}/{active_transformer.get('ct_secondary', ct_secondary)}",
        "VT Ratio": f"{active_transformer.get('vt_primary', vt_primary)}/{active_transformer.get('vt_secondary', vt_secondary)}",
        "Invert Voltage": active_transformer.get("invert_voltage", invert_voltage),
        "Invert Current": active_transformer.get("invert_current", invert_current),
    }
    st.json(mapping_summary)
