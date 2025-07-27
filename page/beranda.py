import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/png;base64,{encoded}"
def tampil():
    img_data = get_base64_image("logo/logot.png")

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
        <div style="color: #ff6b63; font-size: 20px; line-height: 1.8; text-align: center; width: 100%;">
            <i><b>HARAP GANTI TEMA KE MODE GELAP (DARK)</b></i>
        </div>
    """, unsafe_allow_html=True)
    tombol = st.button("📓 Cara Mengaktifkan Mode Gelap (Dark Mode)")
    if tombol():
        st.markdown("""
        <div style="border: 2px solid #555; border-radius: 10px; padding: 15px; background-color: rgba(0, 0, 0, 0.2); color: #c8dee8;">
            <h4>Cara Mengubah Tema ke Mode Gelap:</h4>
            <ol>
                <li>Klik ikon titik tiga atau <b>☰</b> di kanan atas (pojok kanan Streamlit).</li>
                <li>Pilih menu <b>Settings</b>.</li>
                <li>Pada bagian <b>Theme</b>, pilih <b>Dark</b>.</li>
                <li>Perubahan akan otomatis diterapkan.</li>
            </ol>
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
