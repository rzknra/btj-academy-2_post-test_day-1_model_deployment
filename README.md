# Test Project 1

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-brightgreen?logo=fastapi)](https://fastapi.tiangolo.com/)

Repository latihan untuk membuat struktur project rapi dan men-deploy model Machine Learning (ML) menggunakan **FastAPI**.

---

## Endpoint

| Endpoint               | Method | Deskripsi                                   |
|------------------------|--------|--------------------------------------------|
| `/`                    | GET    | Cek API, mengembalikan “Hello World”       |
| `/items/{item_id}`     | GET    | Ambil item berdasarkan ID, query opsional `q` |
| `/predict/`            | GET    | Dummy endpoint untuk prediksi model ML     |
