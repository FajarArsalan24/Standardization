import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/png;base64,{encoded}"
def tampil():
    img_data = get_base64_image("logo/logot.png")

    st.markdown(
        f"""
        <style>
        [data-testid="stHeader"] {{
            background-color: rgba(0, 0, 0, 0);    
        }}
        [data-testid="stToolbar"] {{
            right: 2rem;
        }}
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');
            
        html, body, [class*="css"] {{
            font-family: 'Poppins', sans-serif;
        }}
        .logo-section {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 30px;
        }}
        .logo-title {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #c8dee8;
            margin-bottom: 0px;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5)
        }}
        .logo-wrapper {{
            display: flex;
            justify-content: center;
            margin: auto;
            align-items: center;
        }}
        [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(circle at top left, #182438 20%, transparent 80%),
                radial-gradient(circle at bottom right, #182438 3%, transparent 90%),
                radial-gradient(circle at top right, #00948a 10%, transparent 80%),
                linear-gradient(to left, #00948a, #6884a1);
            color: #c8dee8;
        }}
        @keyframes pulseGlow {{
            0% {{
                filter: drop-shadow(0 0 5px rgba(0, 200, 255, 0.1));
            }}
            50% {{
                filter: drop-shadow(0 0 25px rgba(0, 200, 255, 0.6));
            }}
            100% {{
                filter: drop-shadow(0 0 5px rgba(0, 200, 255, 0.1));
            }}
        }}
        .logo-wrapper img {{
            width: 275px;
            animation: pulseGlow 2s infinite ease-in-out;
            height: 275px;
            border-radius: 50%;
            object-fit: cover;
        }}
        .custom-paragraph {{
            font-size: 18px;
            line-height: 1.8;
            color: #c8dee8;
            text-align: justify;
            background-color: rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="logo-selection">
        <div class="logo-title">Calculator of Standardization</div>
        <div class="logo-wrapper">
            <img src="{img_data}" alt="Logo Bulat">
        </div>
    </div>           
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="height: 3px; background-color: rgba(255, 255, 255, 0.1); margin-top: 0px; margin-bottom: 20px;"></div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="custom-paragraph">
            Calculator of Standaritation adalah web online gratis yang dirancang untuk memudahkan pengguna dalam menghitung konsentrasi larutan standar titrimetri.
            Tujuan dari pembuatan aplikasi ini adalah untuk memudahkan mahasiswa, analis, atau siapa 
            saja yang bekerja di laboratorium dalam melakukan perhitungan dengan cepat, mudah, dan akurat. 
            Dengan adanya aplikasi ini, pengguna hanya perlu memasukkan data seperti massa zat, faktor 
            ekuivalen, dan volume larutan, lalu aplikasi akan menghitung hasilnya secara otomatis. Ini tentu 
            bisa mengurangi risiko kesalahan dan mempercepat proses kerja. Selain itu, aplikasi ini juga bisa menjadi media pembelajaran. 
            Mahasiswa bisa belajar dan memahami proses perhitungan titrimetri 
            dengan lebih mudah karena bisa langsung melihat hasilnya dan mencoba berbagai kombinasi data. 
            Kami berharap aplikasi ini bisa bermanfaat, baik di dunia pendidikan maupun di dunia kerja, 
            khususnya dalam kegiatan laboratorium.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="height: 3px; background-color: rgba(255, 255, 255, 0.1); margin-top: 10px; margin-bottom: 20px;"></div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="custom-paragraph">
            Aplikasi dibuat dengan antarmuka yang sederhana  dan menarik secara 
            visual, sehingga dapat diakses oleh siapa saja tanpa harus memiliki latar belakang 
            teknis. Input pengguna dikemas dalam bentuk aplikasi interaktif yang mudah diisi. 
            Output diberikan dalam bentuk visual (angka dan warna) yang menunjukkan status 
            jawaban mengenai standarisasi yang telah dipilih dengan lengkap. Dengan desain 
            responsif dan aksesibilitas tinggi (bisa dibuka dari HP, tablet, atau komputer), 
            pengguna bisa menghitung kebutuhan standarisasi ketika dibutuhkan di mana saja 
            dan kapan saja.
            <div class="costum-paraagrapg">
                <p>Web ini memiliki fitur: </p>
                <io style"font-size: 18px; color: #c8dee8; margin-top: 0px;">
                    <li>Kalkulator Pembuatan Larutan Standar</li>
                    <li>Kalkulator Pengenceran Larutan Standar</li>
                    <li>Kalkulator Standarisasi</li>
                </io>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="height: 3px; background-color: rgba(255, 255, 255, 0.1); margin-top: 10px; margin-bottom: 20px;"></div>
    """, unsafe_allow_html=True)
