import streamlit as st
import time
import requests
import json
import os

# ---------------------- Konfigurasi Telegram ----------------------
BOT_TOKEN = "8101821591:AAFoQ7LCEkq7F1XGyxjAhpsUd4P6xI37WhE"
CHAT_ID = "1490556477"

# ---------------------- Konfigurasi Halaman ----------------------
st.set_page_config(page_title="CHEMIGO", page_icon="🧪")

# ---------------------- CSS Gaya Gen Z + WA Floating Button ----------------------
genz_css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');

html, body, [class^="css"]  {
  font-family: 'Montserrat', sans-serif;
}

h1, h2, h3, h4, h5, h6, label, div, p, span {
  font-family: 'Montserrat', sans-serif !important;
}

#wa-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #25D366;
  color: white;
  padding: 10px 14px;
  border-radius: 30px;
  text-decoration: none;
  font-weight: bold;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
#wa-button img {
  height: 24px;
}
</style>
<a id="wa-button" href="https://wa.me/62895609627802" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" />
  Chat jika ada pertanyaan
</a>
'''
st.markdown(genz_css, unsafe_allow_html=True)

# ---------------------- Login & Register ----------------------
USER_DB_FILE = "users.json"

def load_users():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    return {"admin": "chemigo123"}

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f)

if "login" not in st.session_state:
    st.session_state.login = False
if "users" not in st.session_state:
    st.session_state.users = load_users()

if not st.session_state.login:
    st.title("🔐 Login / Register")
    mode = st.radio("Pilih Mode:", ["Login", "Register"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if mode == "Login":
        if st.button("Login"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.login = True
                st.success("Berhasil login!")
                st.rerun()
            else:
                st.error("Username atau password salah")

    elif mode == "Register":
        if st.button("Register"):
            if username in st.session_state.users:
                st.warning("Username sudah terdaftar.")
            else:
                st.session_state.users[username] = password
                save_users(st.session_state.users)
                st.success("Registrasi berhasil! Silakan login.")

    st.stop()

# ---------------------- Header Aplikasi ----------------------
st.title("🧪 CHEMIGO ")
st.markdown("Solusi Pemesanan Barang di POLITEKNIK AKA BOGOR.")

# ---------------------- Data Diri ----------------------
nama = st.text_input("👤 Nama Lengkap")
kelas = st.text_input("🏫 Kelas")
nim = st.text_input("🆔 NIM")
prodi = st.text_input("📚 Program Studi")
wa = st.text_input("📱 Nomor WhatsApp (Contoh: 6281234567890)")

# ---------------------- Daftar Produk ----------------------
st.markdown("---")
st.markdown("### 🧾 Pilih Produk:")
produk_data = [
    {"name": "BEAKER GLASS 100ML", "price": 50000, "image": "https://charlestonscientific.com.sg/wp-content/uploads/2021/10/Glassware-1_beaker-100ml.jpg"},
    {"name": "BEAKER GLASS 250ML", "price": 60000, "image": "https://image.made-in-china.com/2f0j00ihQlwPCcbAfE/Laboratory-Glassware-Beaker-Borosilicate-Pyrex-Glass-Beaker-250ml-500ml-1000ml-Beaker-with-Graduations.jpg"},
    {"name": "PIPET VOLUME 10ML", "price": 95000, "image": "https://www.piwine.com/media/Products/VP10.jpg"},
    {"name": "ERLENMEYER 100ML", "price": 80000, "image": "https://tse2.mm.bing.net/th/id/OIP.T4JuL2Wy5LGHUfnN_Yt64QHaHa?pid=Api&P=0&h=220"}
    {"name": "TABUNG REAKSI", "price": 14000, "image": "https://onemedstore.id/wp-content/uploads/2024/02/5476119_46ab7aaa-078b-4690-8acc-223d20381b15_2000_2000.jpg"}
    {"name": "BATANG PENGADUK", "price": 10000, "image": "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//91/MTA-4338072/mico_batang_pengaduk_kaca_d-7mm_panjang_15cm_full02_qrmziex4.jpg"}
    {"name": "BATANG MOHR", "price": 10000, "image": "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//91/MTA-4338072/mico_batang_pengaduk_kaca_d-7mm_panjang_15cm_full02_qrmziex4.jpg"}
    {"name": "BATANG PENGADUK", "price": 10000, "image": "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//91/MTA-4338072/mico_batang_pengaduk_kaca_d-7mm_panjang_15cm_full02_qrmziex4.jpg"}
    {"name": "LABU TAKAR 25ML", "price": 130000, "image": "https://onemedstore.id/wp-content/uploads/2024/07/whatsapp_image_2024-06-29_at_12.17.23__1_.jpg"}
    {"name": "LABU TAKAR 50ML", "price": 150000, "image": "https://glasswareindonesia.wordpress.com/wp-content/uploads/2018/03/2093-png.gif?w=313&h=313"}
    {"name": "LABU TAKAR 100ML", "price": 170000, "image": "https://gratisongkir-storage.com/products/900x900/w7tAbIYCg4AY.jpg.jpg"}
    {"name": "KACAMATA LAB", "price": 27000, "image": "https://cdn.ruparupa.io/fit-in/400x400/filters:format(webp)/filters:quality(90)/ruparupa-com/image/upload/Products/KW1000326_1.jpg"}
    {"name": "HAND SANITIZER GEL 60ML", "price": 9000, "image": "https://oemahherborist.co.id/images/produk/primary-perawatan-tubuh-hand-sanitizer-herborist-hand-sanitizer-gel-pembersih-tangan-aloe---60ml.jpg"}
    {"name": "HAND SOAP 250ML", "price": 11000, "image": "https://cms.olaif.com/contents/source/images/product/hand-soap-slide01.jpg"}
    {"name": "TABUNG ULIR", "price": 37000, "image": "https://labmart.id/wp-content/uploads/2024/01/image_2024-01-31_152313306.png"}
    {"name": "SARUNT TANGAN LATEX UK M", "price": 2500, "image": "https://images.tokopedia.net/img/cache/700/VqbcmM/2022/4/28/caf2240e-f54c-4dfb-ae27-3301f6381a99.jpg"}
]

# Fitur pencarian produk
query = st.text_input("🔍 Cari produk...").lower()

keranjang = {}
for produk in produk_data:
    if query in produk["name"].lower():
        st.image(produk["image"], width=250)
        qty = st.number_input(f"{produk['name']} (Rp {produk['price']:,})", min_value=0, step=1, key=produk['name'])
        if qty > 0:
            keranjang[produk['name']] = qty

# ---------------------- Metode Pembayaran ----------------------
st.markdown("---")
st.markdown("### 💳 Pilih Metode Pembayaran:")
metode_pembayaran = st.radio("", ["Transfer", "Cash On Delivery"])

bank_tujuan = None
bukti_transfer = None

if metode_pembayaran == "Transfer":
    st.markdown("#### 💳 Informasi Transfer:")
    st.markdown("""
    **GoPay:** 0895-6096-27802  
    a.n. ACHMAD FARREL INDERI  

    **BRI:** 5711-0102-9217-531  
    a.n. ACHMAD FARREL INDERI

    **BNI:** 1884905416
    a.n. MUHAMMAD DZIKRIYANSYAH
    """)

    bank_tujuan = st.selectbox("🏦 Pilih Bank Tujuan Transfer", ["GoPay", "BRI", "BNI"], index=None)
    bukti_transfer = st.file_uploader("📤 Upload Bukti Pembayaran (jpg/png/pdf)", type=["jpg", "jpeg", "png", "pdf"])

# ---------------------- Tombol Kirim ----------------------
st.markdown("---")
kirim = st.button("🚀 Kirim Pesanan")

if kirim:
    if not nama or not kelas or not nim or not prodi or not wa:
        st.warning("⚠️ Mohon lengkapi semua data diri.")
    elif not keranjang:
        st.warning("⚠️ Mohon pilih setidaknya satu produk.")
    elif metode_pembayaran == "Transfer" and (not bank_tujuan or not bukti_transfer):
        st.warning("⚠️ Mohon pilih bank tujuan dan upload bukti pembayaran.")
    else:
        bank_info = f" ({bank_tujuan})" if metode_pembayaran == "Transfer" else ""
        pesan = (
            f"👤 Nama: {nama}\n"
            f"🏫 Kelas: {kelas}\n"
            f"🆔 NIM: {nim}\n"
            f"📚 Prodi: {prodi}\n"
            f"📱 WA: https://wa.me/{wa}\n"
            f"💳 Pembayaran: {metode_pembayaran}{bank_info}\n"
            f"\n📦 Produk:\n"
        )
        for produk, qty in keranjang.items():
            pesan += f"- {produk}: {qty} pcs\n"

        # Kirim pesan teks ke Telegram
        url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        response_text = requests.post(url_text, data={"chat_id": CHAT_ID, "text": pesan})

        # Kirim file bukti transfer ke Telegram jika ada
        if metode_pembayaran == "Transfer" and bukti_transfer is not None:
            files = {"document": (bukti_transfer.name, bukti_transfer.getvalue())}
            url_file = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
            response_file = requests.post(url_file, data={"chat_id": CHAT_ID}, files=files)
        else:
            response_file = None

        time.sleep(1.5)

        if response_text.status_code == 200 and (response_file is None or response_file.status_code == 200):
            st.success("✅ Pesanan dan bukti transfer berhasil dikirim!")
        else:
            st.error("❌ Gagal mengirim pesanan atau bukti transfer.")
