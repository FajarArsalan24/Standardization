import streamlit as st
from typing import Dict

def tampil():
    
    REAGENT_DATA: Dict[str, Dict] = {
        "Alkalimetri (NaOH)": {
            "nama": "Natrium Hidroksida",
            "rumus": r"$\text{NaOH}$",
            "berat_molar": 40.0,
            "metode": "Alkalimetri",
            "satuan": "N"
        },
        "Asidimetri (HCl)": {
            "nama": "Asam Klorida",
            "rumus": r"$\text{HCl}$",
            "berat_molar": 36.46,
            "metode": "Asidimetri",
            "satuan": "N"
        },
        "Permanganometri (KMnO4)": {
            "nama": "Kalium Permanganat",
            "rumus": r"$\text{KMnO}_4$",
            "berat_molar": 158.03,
            "metode": "Permanganometri",
            "satuan": "N"
        },
        "Iodometri (KI)": {
            "nama": "Kalium Iodida",
            "rumus": r"$\text{KI}$",
            "berat_molar": 166.0,
            "metode": "Iodometri",
            "satuan": "N"
        },
        "Kompleksometri (EDTA)": {
            "nama": "EDTA",
            "rumus": r"$\text{C}_{10}\text{H}_{14}\text{N}_2\text{O}_8\text{Na}_2$",
            "berat_molar": 372.24,
            "metode": "Kompleksometri",
            "satuan": "M"
        }
    }

    def hitung_pengenceran(C1: float, V2: float, C2: float) -> float:
        return (C2 * V2) / C1
    
    st.markdown("""
        <div class="header">
            <h1>Kalkulator Pengenceran Larutan Titrasi</h1>
            <p>Hitung volume yang perlu diambil dari larutan stok untuk membuat larutan dengan konsentrasi dan volume tertentu</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="height: 3px; background-color: rgba(255, 255, 255, 0.1); margin-top: 0px; margin-bottom: 20px;"></div>
        """, unsafe_allow_html=True)

    selected_reagent = st.selectbox(
        "Pilih larutan yang akan diencerkan:",
        options=list(REAGENT_DATA.keys()),
        index=0  
    )

    reagent = REAGENT_DATA[selected_reagent]
    expander_title = f"Properti {selected_reagent}"
    with st.expander(expander_title, expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<span class='property-label'>Nama Senyawa:</span>", unsafe_allow_html=True)
            st.markdown(f"<span class='property-value'>{reagent['nama']}</span>", unsafe_allow_html=True)
            st.markdown("<span class='property-label'>Rumus Kimia: </span>", unsafe_allow_html=True)
            st.markdown(f"<span class='property-value'>{reagent['rumus']}</span>", unsafe_allow_html=True)
        with col2:
            st.markdown("<span class='property-label'>Berat Molar:</span>", unsafe_allow_html=True)
            st.markdown(f"<span class='property-value'>{reagent['berat_molar']} g/mol</span>", unsafe_allow_html=True)
            st.markdown("<span class='property-label'>Satuan:</span>", unsafe_allow_html=True)
            st.markdown(f"<span class='property-value'>{reagent['satuan']}</span>", unsafe_allow_html=True)

    st.subheader("Parameter Pengenceran")
    col1, col2, col3 = st.columns(3)

    with col1:
        C1 = st.number_input(
            f"Konsentrasi stok ({reagent['satuan']}):",
            min_value=0.001,
            value=19.4, 
            step=0.01,
            key="c1"
        )

    with col2:
        C2 = st.number_input(
            f"Konsentrasi target ({reagent['satuan']}):",
            min_value=0.0001,
            value=0.1,
            step=0.001,
            key="c2"
        )

    with col3:
        V2 = st.number_input(
            "Volume target (mL):",
            min_value=1,
            value=100,
            step=1,
            key="v2"
        )

    if st.button("Hitung Volume Stok yang Diperlukan"):
        if C2 > C1:
            st.error("Error: Konsentrasi target tidak boleh lebih besar dari konsentrasi stok!")
        else:
            V1 = hitung_pengenceran(C1, V2, C2)
            
            st.markdown(f"""
            <div class="result-card">
                <h3 style="color: #c8dee8; margin-top: 0;">Hasil Perhitungan</h3>
                <p style="font-size: 1.2rem; margin-bottom: 0.5rem; color: #c8dee8">
                    <strong>Ambil:</strong> <span style="color: orange;">{V1:.2f} mL</span> larutan {selected_reagent} {C1} {reagent['satuan']}<br>
                    <strong>Encerkan:</strong> <span style="color: blue;">{V2} mL</span> dengan aquades
                </p>
                <h4 style="margin-bottom: 0.5rem; color: #c8dee8;">Langkah Kerja:</h4>
                <ol style="margin-top: 0; color: #c8dee8;">
                    <li>Pipet tepat {V1:.2f} mL larutan stok menggunakan pipet volumetrik</li>
                    <li>Pindahkan ke labu takar {V2} mL</li>
                    <li>Tambahkan aquades hingga 2/3 volume, kocok merata</li>
                    <li>Encerkan sampai tanda batas</li>
                    <li>Homogenkan dengan membalik labu 7 kali</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

