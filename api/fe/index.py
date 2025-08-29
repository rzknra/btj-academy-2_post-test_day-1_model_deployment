# Import library
import streamlit as st
from api.prediction import get_pred, get_pred_mlflow
from dotenv import load_dotenv
import time

# Load environment variable
load_dotenv(dotenv_path=".dev.env")

# Judul aplikasi dengan emoji dan warna
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🌸 Aplikasi Prediksi Iris 🌸</h1>", unsafe_allow_html=True)
st.markdown("---")

# Deskripsi aplikasi
st.markdown(
    """
    Aplikasi ini digunakan untuk memprediksi jenis bunga Iris berdasarkan ukuran sepal dan petal.
    """,
    unsafe_allow_html=True
)

# Pembatas garis
st.divider()

# Membungkus pilihan mode prediksi dengan form
with st.form("prediction_mode_form"):
    st.markdown("### Pilih Mode Prediksi:")
    mode = st.radio(
        "Mode Prediksi", 
        ("Manual", "MLflow"), 
        horizontal=True
    )
    st.form_submit_button("Pilih")

st.divider()

# Pemetaan kelas hasil prediksi
CLASS_MAP = {
    0: "Iris-setosa 🌱",
    1: "Iris-versicolor 🌿",
    2: "Iris-virginica 🌺"
}

# Form input dengan kolom agar rapi dan compact
with st.form("predict_form"):
    st.markdown("### Masukkan Nilai Data:")
    kol1, kol2 = st.columns(2)
    with kol1:
        sepal_length = st.number_input("Panjang Sepal", min_value=0.0)
        sepal_width = st.number_input("Lebar Sepal", min_value=0.0)
    with kol2:
        petal_length = st.number_input("Panjang Petal", min_value=0.0)
        petal_width = st.number_input("Lebar Petal", min_value=0.0)

    tombol_submit = st.form_submit_button("🌟 Prediksi")

    if tombol_submit:
        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        # Spinner saat menunggu prediksi
        with st.spinner("Sedang memprediksi... ⏳"):
            time.sleep(0.3)  # simulasi delay
            if mode == "Manual":
                pesan, hasil = get_pred(data=data)
            else:
                pesan, hasil = get_pred_mlflow(data=data)

        # Tampilkan hasil prediksi
        if not hasil:
            st.error(f"❌ Prediksi gagal! {pesan}")
        else:
            try:
                pred_class = int(hasil[0])
                label = CLASS_MAP.get(pred_class, "Tidak diketahui")
                st.success(f"✅ Hasil prediksi: **{label}**")
                st.caption(f"Berhasil diprediksi dengan mode {mode}")
            except (IndexError, ValueError, TypeError):
                st.error(f"⚠️ Format hasil prediksi tidak valid! {hasil}")