import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Gereja Pentakosta Indonesia", layout="wide")

# Fungsi Header
def tampilkan_header():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://i.imgur.com/LT8gPvK.png", width=80)  # Logo gereja (gunakan URL lain jika ada)
    with col2:
        st.markdown("<h1 style='color:#2E7D32; margin-bottom:0;'>Gereja Pentakosta Indonesia</h1>", unsafe_allow_html=True)
        st.markdown("**Dipenuhi Roh, Melayani dengan Kasih**")
        st.markdown("Selamat datang di sistem informasi digital kami. Temukan informasi pelayanan, ajaran, dan kegiatan rohani kami.")
    st.markdown("---")

# Fungsi Profil Gereja
def tampilkan_profil():
    st.subheader("🏛️ Tentang Kami")
    st.markdown("""
    **Gereja Pentakosta Indonesia** adalah tempat pertumbuhan iman yang bersumber dari pengajaran Alkitabiah, 
    persekutuan yang hangat, dan kuasa Roh Kudus yang nyata.

    Kami adalah gereja lokal yang berdiri dalam aliran **Pentakosta**, terbuka untuk semua kalangan.
    """)
    st.info("💬 Motto: *Dipenuhi Roh, Melayani dengan Kasih*")
    st.markdown("📅 Didirikan sejak tahun 1982 | ✝️ Cabang di 15 kota besar")

# Fungsi Ajaran Iman
def tampilkan_ajaran():
    st.subheader("📜 Pokok-Pokok Iman")
    st.markdown("""
    1. **Alkitab** adalah kebenaran yang absolut dan tidak berubah.  
    2. **Allah Tritunggal**: Bapa, Anak, dan Roh Kudus.  
    3. **Keselamatan** melalui iman kepada Yesus Kristus.  
    4. **Baptisan Roh Kudus** dan manifestasi karunia-Nya.  
    5. **Kesembuhan ilahi** melalui iman dan doa.  
    6. **Kedatangan Kristus** kedua kali yang dinantikan.  
    7. **Persekutuan Kudus** dalam kasih dan kesatuan tubuh Kristus.  
    """)

# Fungsi Jadwal Ibadah
def tampilkan_jadwal():
    st.subheader("📆 Jadwal Ibadah Rutin")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **Ibadah Raya Minggu**: Minggu, 08.00 WIB  
        - **Sekolah Minggu**: Minggu, 08.00 WIB  
        - **Persekutuan Kaum Wanita**: Kamis, 10.00 WIB  
        """)
    with col2:
        st.markdown("""
        - **Doa Tengah Minggu**: Rabu, 19.00 WIB  
        - **Kaum Muda & Remaja**: Sabtu, 17.00 WIB  
        - **Pemuridan & Pelatihan**: Jumat, 18.30 WIB  
        """)
    st.success("📡 Ibadah juga dapat diikuti via Zoom & YouTube Live.")

# Fungsi Kontak dan Doa
def tampilkan_kontak():
    st.subheader("📩 Hubungi & Doa")
    with st.form("kontak_form"):
        nama = st.text_input("Nama Anda")
        email = st.text_input("Email")
        pesan = st.text_area("Pesan / Permohonan Doa")
        kirim = st.form_submit_button("Kirim")
        if kirim:
            if nama and email and pesan:
                st.success("✅ Doa Anda telah diterima. Kami akan segera merespons.")
            else:
                st.warning("⚠️ Harap isi semua kolom!")

    st.markdown("---")
    st.markdown("""
    **🏠 Alamat Gereja**  
    Jl. Kasih Karunia No. 10, Kota Semarang  
    📱 WhatsApp: 0812-6061-6627 
    📧 Email: gerejapentakosta.id@gmail.com  
    📷 Instagram: [@gerejapentakostaindonesia](https://www.instagram.com/gerejapentakostaindonesia/)  
    """)

# Kesaksian Jemaat
def tampilkan_testimoni():
    st.subheader("💬 Kesaksian Jemaat")
    st.markdown("""
    > *"Melalui gereja ini, saya mengalami pemulihan dan pertumbuhan iman yang luar biasa."*  
    — **Kevin, 18 tahun**

    > *"Pemuridan dan persekutuan di sini sangat membangun hidup rohaniku."*  
    — **Valen calon tentara, 20 tahun**

    > *"Doa bersama jemaat telah menjadi kekuatan besar dalam hidup keluargaku."*  
    — **Dalbo, 30 tahun**
    """)

# Fungsi Live Streaming
def tampilkan_live_stream():
    st.subheader("📺 Live Streaming Ibadah")
    st.markdown("Tonton ibadah secara langsung melalui kanal resmi YouTube kami:")
    st.video("https://www.youtube.com/@gpiujungaspal7178/streams")

# Fungsi FAQ
def tampilkan_faq():
    st.subheader("❓ Pertanyaan Umum (FAQ)")
    with st.expander("Apa itu gereja Pentakosta?"):
        st.markdown("Gereja Pentakosta adalah gereja Kristen yang menekankan pengalaman pribadi dengan Roh Kudus, termasuk tanda-tanda seperti bahasa roh dan penyembuhan.")
    with st.expander("Apakah saya boleh datang walau bukan anggota?"):
        st.markdown("Tentu! Gereja kami terbuka untuk siapa saja yang ingin mengenal Tuhan lebih dalam.")
    with st.expander("Apakah tersedia pelayanan konseling?"):
        st.markdown("Ya, silakan hubungi kami melalui formulir di halaman Kontak.")

# Menampilkan Header
tampilkan_header()

# Navigasi
menu = st.sidebar.selectbox("📌 Navigasi", [
    "Profil Gereja",
    "Ajaran Iman",
    "Jadwal Ibadah",
    "Kontak & Doa",
    "Testimoni Jemaat",
    "Live Streaming",
    "FAQ"
])

# Routing Tampilan
if menu == "Profil Gereja":
    tampilkan_profil()
elif menu == "Ajaran Iman":
    tampilkan_ajaran()
elif menu == "Jadwal Ibadah":
    tampilkan_jadwal()
elif menu == "Kontak & Doa":
    tampilkan_kontak()
elif menu == "Testimoni Jemaat":
    tampilkan_testimoni()
elif menu == "Live Streaming":
    tampilkan_live_stream()
elif menu == "FAQ":
    tampilkan_faq()

# Footer
st.markdown("---")
st.caption("© 2025 Gereja Pentakosta Indonesia | Dipenuhi Roh, Melayani dengan Kasih")
