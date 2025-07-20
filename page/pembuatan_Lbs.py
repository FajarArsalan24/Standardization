import streamlit as st
import pandas as pd
from typing import Dict

PRIMARY_STANDARDS: Dict[str, Dict] = {
    "H2C2O4.2H2O": {
        "nama": "Asam oksalat dihidrat",
        "metode": ["Alkalimetri (NaOH)", "Permanganometri (KMnO4)"],
        "berat_ekivalen": 63.03,
        "berat_molar": 126.07,
        "satuan": "N",
    },
    "Na2B4O7.10H2O": {
        "nama": "Boraks dekahidrat",
        "metode": ["Asidimetri (HCl)"],
        "berat_ekivalen": 190.7,
        "berat_molar": 381.4,
        "satuan": "N",
    },
    "K2Cr2O7": {
        "nama": "Kalium dikromat",
        "metode": ["Iodometri (KI)"],
        "berat_ekivalen": 49.03,
        "berat_molar": 294.18,
        "satuan": "N",
    },
    "CaCO3": {
        "nama": "Kalsium karbonat",
        "metode": ["Kompleksometri (EDTA)"],
        "berat_ekivalen": 50.04,
        "berat_molar": 100.09,
        "satuan": "M",
    }
}

def tampil():
    def hitung_massa(konsentrasi: float, volume_ml: int, berat: float) -> float:
        """Menghitung massa yang harus ditimbang"""
        return konsentrasi * (volume_ml / 1000) * berat

    st.markdown("""
        <style>
            [data-testid="stHeader"] {
                background-color: rgba(0, 0, 0, 0);    
            }
            [data-testid="stAppViewContainer"] {
                background:
                    radial-gradient(circle at top left, #182438 20%, transparent 80%),
                    radial-gradient(circle at bottom right, #182438 3%, transparent 90%),
                    radial-gradient(circle at top right, #00948a 10%, transparent 80%),
                    linear-gradient(to left, #00948a, #6884a1);
                color: #c8dee8;
            }      

            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');
            
            html, body, [class*="css"] {
                font-family: 'Poppins', sans-serif;
            }   
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Space Grotesk', sans-serif;
                color: #c8dee8;
            }     
            .header {
                text-align: center;
                padding: 2rem;
                margin-bottom: 2.5rem;
                color: #c8dee8;
            }
            .header h1 {
                margin-bottom: 5px;
            }
            .header p {
                font-style: italic;
                opacity: 0.9;
            }    
            .container {
                background-color: #c8dee8;
                padding: 2rem;
                border-radius: 16px;
                box-shadow: 0 4px 30px rgba(0,0,0,0.05);
                margin-bottom: 2rem;
            }          
            .result-card {
                background-color: rgba(0, 0, 0, 0.1);
                border-radius: 12px;
                padding: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.3), 0 0 20px rgba(0,0,0,0.3)
            }          
            .select-box {
                margin-bottom: 2rem;
                background-color: #203245 !important;
            }           
            .input-group {
                margin-bottom: 1.5rem;
            }      
          .data-card {
                background-color: rgba(255, 255, 255, 0.15);
                border-radius: 8px;
                padding: 1rem;
                box-shadow: 0 4px 15px rgba(0,0,0,0.05);
                margin-top: 2rem;
            }
            input, select, textarea {
                background-color: #142830 !important;
                color: #c8dee8 !important;
                border-radius: 8px !important;
                backdrop-filter: blur(6px);
                -webkit-backdrop-filter: blur(6px);
            }
            ::placeholder {
                color: #e0e0e0;
                opacity: 0.7;
            }               
            button {
                background-color: rgba(0, 0, 0, 0.3) !important;
                color: #c8dee8 !important;
                border: 1px solid #203245 !important;
                border-radius: 8px !important;
                font-weight: bold;
                padding: 8px 16px;
                backdrop-filter: blur(6px);
                -webkit-backdrop-filter: blur(6px);
            }                
            input:focus, select:focus, textarea:focus {
                outline: none !important;
                border-color: #72f5ff !important;
                box-shadow: 0 0 10px #72f5ff;
            }            
            div[data-baseweb="select"] * {
                color: #c8dee8 !important;
                background-color: rgba(0, 0, 0, 0.1);
            }
        </styl>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="header">
            <h1>Kalkulator Preparasi Larutan Standar</h1>
            <p>Menghitung massa yang harus ditimbang</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="height: 3px; background-color: rgba(255, 255, 255, 0.1); margin-top: 0px; margin-bottom: 20px;"></div>
        """, unsafe_allow_html=True)
    
    with st.container():
        st.subheader("Pilih Metode Standarisasi")
        metode = st.selectbox(
            "Pilih metode:",
            options=[
                "Alkalimetri (NaOH)",
                "Asidimetri (HCl)", 
                "Permanganometri (KMnO4)",
                "Iodometri (KI)",
                "Kompleksometri (EDTA)"
            ],
            key="metode_select"
        )

        standar = next((k for k, v in PRIMARY_STANDARDS.items() if metode in v["metode"]), None)

        if standar:
            data = PRIMARY_STANDARDS[standar]
            
            st.subheader(f"Standar Primer: {data['nama']} ({standar})")
            
            col1, col2 = st.columns(2)
            
            with col1:
                konsentrasi = st.number_input(
                    f"Konsentrasi target ({data['satuan']}):",
                    min_value=0.001,
                    value=0.1,
                    step=0.001,
                    format="%.3f",
                    key="konsentrasi_input"
                )
                
            with col2:
                volume = st.number_input(
                    "Volume larutan (mL):",
                    min_value=1,
                    value=100,
                    step=1,
                    key="volume_input"
                )

            if st.button("Hitung Massa", key="hitung_button"):
                if data["satuan"] == "N":
                    massa = hitung_massa(konsentrasi, volume, data["berat_ekivalen"])
                else:
                    massa = hitung_massa(konsentrasi, volume, data["berat_molar"])
                
                st.markdown(f"""
                <div class="result-card">
                    <h3 style="color: #c8dee8; margin-top: 0;">Hasil Perhitungan</h3>
                    <p style="font-size: 1.2rem; margin-bottom: 0.5rem;">
                        <strong>Massa yang harus ditimbang:</strong><br>
                        <span style="font-size: 1.5rem; color: #c8dee8;">⚖️ {massa:.4f} gram {standar}</span>
                    </p>
                    <div style="margin-top: 1.5rem;">
                        <h4 style="margin-bottom: 0.5rem; color: #c8dee8;">Prosedur Preparasi:</h4>
                        <ol style="margin-top: 0;">
                            <li>Timbang dengan akurat {massa:.4f} g (±0.0002 g)</li>
                            <li>Pindahkan ke labu takar {volume} mL</li>
                            <li>Larutkan dalam sedikit Aquadest</li>
                            <li>Encerkan sampai tanda batas</li>
                            <li>Homogenkan dengan baik</li>
                        </ol>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    with st.container():
        st.subheader("📋 Data Standar Primer")
        st.markdown("<div class='data-card'>", unsafe_allow_html=True)
        
        df = pd.DataFrame.from_dict({
            k: {
                "Rumus Kimia": k,
                "Nama": v["nama"],
                "Metode": ", ".join(v["metode"]),
                "Berat (g)": f"{v['berat_ekivalen'] if v['satuan']=='N' else v['berat_molar']:.2f}",
                "Satuan": v["satuan"]
            }
            for k, v in PRIMARY_STANDARDS.items()
        }, orient='index')

        st.dataframe(
            df,
            column_config={
                "Rumus Kimia": "Rumus",
                "Nama": st.column_config.TextColumn(width="medium"),
                "Metode": st.column_config.TextColumn(width="large"),
                "Berat (g)": "Berat",
                "Satuan": "Satuan"
            },
            hide_index=True,
            use_container_width=True
        )
        
        st.markdown("</div>", unsafe_allow_html=True)