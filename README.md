# 🚀 Model Deployment with FastAPI & MLflow

Halo! 👋 Repo ini aku buat sebagai latihan **deployment model machine learning** pake **FastAPI**, **MLflow**, dan **Streamlit**. Strukturnya sengaja dibikin **modular** biar gampang dipahami, di-maintain, dan dikembangin.

---

## 📂 Struktur Folder

```
POST-TEST_MODEL-DEPLOYMENT/
├── api/                     # Folder utama untuk API
│   ├── fe/                  # Bagian Front-End API (endpoint untuk user/client)
│   │   ├── api/            
│   │   │   └── prediction.py  # Endpoint untuk melakukan prediksi
│   │   └── index.py           # Entry point untuk FE API
│   └── predict/             # Bagian Back-End API (logika prediksi)
│       ├── models/          # Model ML atau schema database yang dipakai
│       ├── schema.py        # Pydantic schema untuk request/response
│       ├── service.py       # Logika bisnis/layanan prediksi
│       └── views.py         # Routing dan endpoint untuk back-end API
│
├── scheduler/               # Folder untuk task scheduler (misal cron jobs)
├── mlartifacts/             # Menyimpan model, logs, atau artifacts ML
├── mlflow/                  # Pipeline dan utilitas MLflow
│   ├── load_model/         
│   │   └── load_model.py     # Fungsi untuk memuat model dari MLflow
│   └── train_pipeline/     
│       └── train_pipeline.py # Pipeline training model ML
│
├── .dev.env                 # Environment variables untuk development
├── .prod.env                # Environment variables untuk production
├── .gitignore               # File untuk mengecualikan file/folder di git
├── main.py                  # Entry point aplikasi FastAPI
├── README.md                # Dokumentasi project
└── requirements.txt         # Daftar dependencies Python
```
---

## ⚙️ Cara Jalanin

1. **Clone repository ini:**

   ```bash
   git clone https://github.com/rzknra/btj-academy-2_post-test_model-deployment.git
   cd btj-academy-2_post-test_model-deployment
   ```

2. **Buat virtual environment & aktifin:**

   ```bash
   python -m venv venv
   
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Buat file .env** (sesuaikan untuk dev atau prod):

5. **Jalanin backend FastAPI :**

   ```bash
   uvicorn main:app --reload
   ```

6. **Jalankan frontend dengan Streamlit:**

   ```bash
   streamlit run api/fe/index.py
   ```

7. **Jalankan server MLflow:**

   ```bash
   mlflow server --host [host ip] --port [port]
   ```

---

## 🌐 Endpoint Utama

* `GET /` → Cek API, balikin "Hello World"
* `GET /docs` → Swagger UI (buat eksplorasi API)
* `POST /api/fe/api/prediction` → Prediksi dari sisi frontend
* `POST /api/predict/views` → Prediksi backend

---
## 🖥️ Contoh Hasil Prediksi
<img src="https://github.com/user-attachments/assets/6864f660-b2a6-444a-b727-4bf56e3e8613" alt="Screenshot 2025-08-29 105848" style="max-width: 100%; height: auto;" />


---

🎉 Itu aja! Repo ini mostly buat latihan, tapi bisa banget dikembangin jadi project beneran.
