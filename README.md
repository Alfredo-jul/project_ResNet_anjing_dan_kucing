# 🐶🐱 Klasifikasi Gambar Anjing dan Kucing (Cat vs Dog)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/username/cat-dog-streamlit)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](#)

Aplikasi berbasis **Streamlit** untuk mengklasifikasikan gambar **Anjing** dan **Kucing** menggunakan **Deep Learning (CNN – ResNet)**.  
Pengguna dapat mengunggah gambar, lalu sistem akan menampilkan **hasil prediksi** beserta **confidence score**.

---

## 📌 Fitur Utama
- Upload gambar format **.jpg / .jpeg / .png**
- Preview gambar langsung di aplikasi
- Prediksi kelas:
  - 🐱 Cat (Kucing)
  - 🐶 Dog (Anjing)
- Menampilkan **confidence score**
- Antarmuka sederhana, responsif, dan interaktif
- Berjalan di **GitHub Codespaces** dan lokal

---

## 🖼️ Tampilan Aplikasi

### Halaman Upload Gambar
![Upload Image](screenshots/upload.png)

### Hasil Prediksi
![Prediction Result](screenshots/prediction.png)

---

## ⚙️ Teknologi yang Digunakan
- **Python**
- **Streamlit**
- **TensorFlow / Keras**
- **NumPy**
- **Pillow (PIL)**

---

## 🧠 Alur Kerja Sistem
1. Pengguna mengunggah gambar anjing atau kucing
2. Gambar di-*resize* ke ukuran **128 × 128**
3. Preprocessing gambar disesuaikan dengan model
4. Model CNN (ResNet) melakukan prediksi
5. Sistem menampilkan:
   - Hasil klasifikasi (**Cat / Dog**)
   - Confidence score
   - Nilai probabilitas mentah

---

## 🧪 Preprocessing Gambar
- Convert gambar ke **RGB**
- Resize ke **128 × 128**
- Ekspansi dimensi menjadi `(1, 128, 128, 3)`
- Normalisasi / preprocessing sesuai training model

---

## 🚀 Cara Menjalankan Aplikasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/cat-dog-streamlit.git
cd cat-dog-streamlit


### 2️⃣ Install Dependensi

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Jalankan Streamlit

```bash
streamlit run app.py
```

Jika menggunakan **GitHub Codespaces**:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Buka aplikasi di browser:

```
http://localhost:8501
```

atau melalui **Ports → Open in Browser** (Codespaces)

---

## 📂 Struktur Folder

```text
cat-dog-streamlit/
├── app.py
├── requirements.txt
├── models/
│   └── cat_dog_resnet101.h5
├── screenshots/
│   ├── upload.png
│   └── prediction.png
└── README.md
```

---

## 📦 Model

* Format: **`.h5`**
* Framework: **TensorFlow / Keras**
* Arsitektur: **CNN (ResNet-based)**
* Output: **Binary Classification (Cat vs Dog)**

---

## 👤 Identitas Mahasiswa

* **Nama**: Alfredo Juliandro Etawulang
* **NIM**: 202211420027

---

## 📄 Lisensi

Project ini dibuat untuk keperluan **pembelajaran dan akademik**.
```md
https://github.com/username/cat-dog-streamlit

