import streamlit as st
import pandas as pd
import numpy as np

def tampil():

    st.markdown("""
    <div class="header">
        <h1>Perhitungan Standarisasi Titrimetri</h1>
        <p>Presisi Perhitungan Berdasarkan Larutan Standar</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="height: 3px; background-color: rgba(255, 255, 255, 0.1); margin-top: 0px; margin-bottom: 20px;"></div>
        """, unsafe_allow_html=True)

    methods = {
        "Asidimetri (HCl)": {
            "titrant": "HCl",
            "standar": "Na₂B₄O₇·10H₂O",
            "be": 190.69
        },
        "Alkalimetri (NaOH)": {
            "titrant": "NaOH",
            "standar": "H₂C₂O₄·2H₂O",
            "be": 63.03
        },
        "Permanganometri (KMnO₄)": {
            "titrant": "KMnO₄",
            "standar": "H₂C₂O₄·2H₂O",
            "be": 63.03
        },
        "Iodometri (Tiosulfat)": {
            "titrant": "Na₂S₂O₃",
            "standar": "K₂Cr₂O₇",
            "be": 49.03
        },
        "Kompleksometri (EDTA)": {
            "titrant": "EDTA",
            "standar": "CaCO₃",
            "be": 100.09 
        }
    }

    selected_method = st.selectbox("🔍 Pilih Metode Titrasi:", options=list(methods.keys()))
    selected_info = methods[selected_method]
    st.write(f"**Titran:** {selected_info['titrant']}")
    st.write(f"**Standar yang digunakan:** {selected_info['standar']}")

    col1, col2 = st.columns(2)

    with col1:
        std_mass = st.number_input("⚖️ Massa Standar Primer (g):", min_value=0.0, step=0.0001, format="%.4f", value=0.1)

    label_be = "Bobot Molekul (g/mol)" if "Kompleksometri" in selected_method else "Bobot Ekivalen (mg/mgrek)"
    default_be = selected_info["be"]

    with col2:
        be_value = st.number_input(label_be, min_value=0.0, format="%.4f", value=default_be)

    st.subheader("📊 Volume Titrasi Duplo")
    duplo1, duplo2 = st.columns(2)
    with duplo1:
        vol1 = st.number_input("Volume 1 (mL):" , min_value=0.0, value=10.0, step=0.1, format="%.2f")
    with duplo2:
        vol2 = st.number_input("Volume 2 (mL):", min_value=0.0, value=10.2, step=0.1, format="%.2f")

    avg_vol = np.mean([vol1, vol2]) 

    if "Kompleksometri" not in selected_method:
        st.subheader("⚙️ Faktor Koreksi")
        factor_type = st.radio("Pilih jenis faktor:", ["Faktor Pengencer", "Faktor Pengali"])
        factor_value = st.number_input(f"{factor_type}:", min_value=1.0, value=1.0, step=0.1, format="%.4f")
    else:
        factor_value = 1.0 

    st.markdown('<div class="formula-box"><strong>Rumus yang digunakan:</strong></div>', unsafe_allow_html=True)

    if "Kompleksometri" in selected_method:
        st.latex(r"""
        \text{mol/L} = \frac{\text{Massa (g)}}{\text{BM (g/mol)} \times \text{Volume (L)}}
        """)
    else:
        st.latex(r"""
        \text{mgrek/mL} = \frac{\text{Massa Standar (mg)}}{\text{Faktor} \times \text{Rata-rata Volume (mL)} \times \text{BE}}
        """)

    def calculate():
        try:
            if "Kompleksometri" in selected_method:
                vol_L = avg_vol / 1000  
                if be_value > 0 and vol_L > 0:
                    return std_mass / (be_value * vol_L)
            else:
                mass_mg = std_mass * 1000
                denom = factor_value * avg_vol * be_value
                if denom > 0:
                    return mass_mg / denom
        except:
            return None
        return None

    if st.button("📥 Hitung Konsentrasi", type="primary", use_container_width=True):
        result = calculate()

        if result is not None:
            satuan = "mol/L" if "Kompleksometri" in selected_method else "mgrek/mL"

            st.markdown(f"""
            <div class="result-box-dark">
                <h3>📌 Hasil Perhitungan</h3>
                <table>
                    <tr><td><strong>Konsentrasi</strong></td><td>{result:.6f} {satuan}</td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

            st.subheader("📖 Detail Perhitungan")
            if "Kompleksometri" in selected_method:
                calc_data = {
                    "Komponen": [
                        "Massa standar primer",
                        "Bobot Molekul",
                        "Volume rata-rata (L)",
                        "Hasil"
                    ],
                    "Nilai": [
                        f"{std_mass:.4f} g",
                        f"{be_value:.4f} g/mol",
                        f"{avg_vol:.2f} mL = {avg_vol/1000:.4f} L",
                        f"{result:.6f} mol/L"
                    ]
                }
            else:
                calc_data = {
                    "Komponen": [
                        "Massa standar primer", 
                        "Bobot ekivalen",
                        "Rata-rata volume titrasi",
                        "Faktor",
                        "Hasil"
                    ],
                    "Nilai": [
                        f"{std_mass:.4f} g = {std_mass*1000:.2f} mg",
                        f"{be_value:.4f} mg/mgrek",
                        f"({vol1:.2f} + {vol2:.2f})/2 = {avg_vol:.4f} mL",
                        f"{factor_value:.4f}",
                        f"{result:.6f} mgrek/mL"
                    ]
                }

            st.table(pd.DataFrame(calc_data))

            st.markdown('<div class="result-box-dark"><h4>📐 Persamaan:</h4>', unsafe_allow_html=True)
            if "Kompleksometri" in selected_method:
                st.latex(rf"""
                \frac{{ {std_mass:.4f} \, g }}{{ {be_value:.4f} \times {avg_vol/1000:.4f} \, L }} = {result:.6f} \, mol/L
                """)
            else:
                st.latex(rf"""
                \frac{{ {std_mass*1000:.2f} \, mg }}{{ {factor_value:.4f} \times {avg_vol:.2f} \, mL \times {be_value:.4f} }} = {result:.6f} \, mgrek/mL
                """)
            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.error("❗ Perhitungan gagal. Periksa semua input.")

