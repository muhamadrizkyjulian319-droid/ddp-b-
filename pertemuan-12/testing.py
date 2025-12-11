import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Bangun Datar", page_icon="📝")

st.title("Aplikasi Perhitungan Bangun Datar")
st.write("Silahkan pilih menu disamping untuk memulai")

def luas_persegi(sisi):
    return sisi * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

# Sidebar
with st.sidebar:
    menu = option_menu("Menu", ["Infomasi", "Luas Persegi", "Luas Segitiga", "Luas Lingkaran"], 
        icons=["house", "square", "triangle", "circle"], menu_icon="list", default_index=0)
    menu

# menu = st.sidebar.selectbox("Menu", ["Pilih bangun datar", "Luas Persegi", "Luas Segitiga", "Luas Lingkaran"])

if menu == "Luas Persegi":
    st.header("Luas Persegi")

    # Image
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVlFBO8LM3diq71WxoJjU3581SrrFNt6F4qA&s", caption = "Rumus Luas Persegi", width=300)

    # Input
    sisi = st.number_input("Masukkan panjang sisi persegi", min_value=0)
    if st.button("Hitung"):
        luas = luas_persegi(sisi)
        st.success(f"Luas persegi dengan sisi {sisi} adalah {luas}")

elif menu == "Luas Segitiga":
    st.header("Luas Segitiga")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvnU93yw54EG4p3cL7lMuWFeCGlkPv0co7cA&s", caption = "Rumus Luas Segitiga", width=300)
    alas = st.number_input("Masukkan panjang alas segitiga", min_value=0)
    tinggi = st.number_input("Masukkan panjang tinggi segitiga", min_value=0)
    if st.button("Hitung"):
        luas = luas_segitiga(alas, tinggi)
        st.success(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")

elif menu == "Luas Lingkaran":
    st.header("Luas Lingkaran")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqE7zcAuial5S7kKzPFlfHbDLH-alugkaqYg&s", caption="Rumus Luas Lingkaran", width=300)
    jari_jari = st.number_input("Masukkan panjang jari-jari lingkaran", min_value=0)
    if st.button("Hitung"):
        luas = luas_lingkaran(jari_jari)
        st.success(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")