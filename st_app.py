import streamlit as st
from streamlit_option_menu import option_menu
from page import beranda, Pembuatan_Ls, pembuatan_Lbs, Menghitung_s

def style(path_css):
    with open(path_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
style("style.css")

st.set_page_config(page_title="Calculator of Standardization", page_icon="🧪", layout="wide")

st.markdown("""
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
""", unsafe_allow_html=True)
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=[
            "Beranda",
            "Pembuatan Larutan Standar",
            "Pengenceran Larutan Standar",
            "Perhitungan Standarisasi"
        ],
        icons=["house", "eyedropper", "droplet", "calculator"],
        default_index=0
    )
st.sidebar.markdown("""
    <div style="height: 3px; background-color: rgba(255, 255, 255, 0.15); margin-top: 0px; margin-bottom: 20px;"></div>
    """, unsafe_allow_html=True)
st.sidebar.markdown("""
    <div>
        <i class="material-icons">error</i>
        <span class="sidebar"><b><i>tentang Kami</i></b></span>
    </div>
    <div class="sidebar">
        <p>Kelompok 7</p>
        <ol style="margin-top: 0; color: #c8dee8; font-size: 13px;">
            <li>Aqila Olivia (2460311)</li>
            <li>Fajar Arsalan Naufal (2460366)</li>
            <li>Millata Aruzi Yaqinal Haqqi (2460421)</li>
            <li>Nazwa Salsabilla (2460468)</li>
            <li>Tiur Elvionita (2460527)</li>
        </ol>
    </div>
""", unsafe_allow_html=True)

if selected == "Beranda":
    beranda.tampil()
elif selected == "Pembuatan Larutan Standar":
    pembuatan_Lbs.tampil()
elif selected == "Pengenceran Larutan Standar":
    Pembuatan_Ls.tampil()
elif selected == "Perhitungan Standarisasi":
    Menghitung_s.tampil()
