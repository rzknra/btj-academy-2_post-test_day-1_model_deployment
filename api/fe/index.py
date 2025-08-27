# Import library yang dibutuhkan
import streamlit as st
from api.prediction import get_pred
from dotenv import load_dotenv

# Load environment variabel
load_dotenv(dotenv_path=".dev.env")

# Judul aplikasi
st.title("🌸 Iris Prediction App")

# Deskripsi aplikasi
st.write(
    "Masukkan nilai panjang & lebar sepal/petal untuk memprediksi jenis bunga Iris "
    "(Setosa, Versicolor, Virginica)."
)

# Divider
st.divider()

# Mapping class hasil prediksi
CLASS_MAP = {
    0: "Iris-setosa 🌱",
    1: "Iris-versicolor 🌿",
    2: "Iris-virginica 🌺"
}

# Form input
with st.form("predict_form"):
    sepal_length = st.number_input("Sepal Length", min_value=0.0)
    sepal_width = st.number_input("Sepal Width", min_value=0.0)
    petal_length = st.number_input("Petal Length", min_value=0.0)
    petal_width = st.number_input("Petal Width", min_value=0.0)

    submitted = st.form_submit_button("Predict")

    if submitted:
        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        # Panggil fungsi prediksi
        message, result = get_pred(data=data)

        # Tampilkan hasil
        if not result:  # Kalau error atau kosong
            st.error(f"Prediction failed! {message}")
        else:
            pred_class = result[0]
            label = CLASS_MAP.get(pred_class, "Unknown")
            st.success(f"✅ Predicted class: **{label}**")
            st.caption(f"Message: {message}")
