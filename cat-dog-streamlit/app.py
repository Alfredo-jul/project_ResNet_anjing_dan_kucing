import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from pathlib import Path

# --- Konfigurasi sesuai notebook kamu ---
IMG_SIZE = (128, 128)  # dari notebook: image_size = (128, 128)
CLASS_NAMES = ["cat", "dog"]  # label_mode=binary: 0=cat, 1=dog

st.set_page_config(page_title="Cat vs Dog Classifier", page_icon="🐾", layout="centered")

@st.cache_resource
def load_model():
    model_path = Path("models") / "cat_dog_resnet101.h5"  # sesuaikan nama file
    if not model_path.exists():
        raise FileNotFoundError(f"Model tidak ditemukan: {model_path.resolve()}")
    return tf.keras.models.load_model(model_path)

def preprocess_image(pil_img: Image.Image) -> np.ndarray:
    # Convert ke RGB (jaga-jaga kalau png transparan / grayscale)
    img = pil_img.convert("RGB")
    img = img.resize(IMG_SIZE)
    arr = np.array(img).astype(np.float32)

    # Penting: di notebook kamu tidak terlihat ada rescaling/preprocess_input.
    # Jadi default kita biarkan 0..255 seperti data mentah.
    # Kalau ternyata training kamu pakai /255, tinggal aktifkan baris ini:
    # arr = arr / 255.0

    arr = np.expand_dims(arr, axis=0)  # (1, H, W, C)
    return arr

st.title("🐾 Cat vs Dog Classifier")
st.write("Upload gambar, lalu model akan memprediksi apakah itu **cat** atau **dog**.")

with st.sidebar:
    st.header("Pengaturan")
    st.caption("Model: `.h5` (Keras/TensorFlow)")
    use_rescale = st.toggle("Rescale /255 (aktifkan jika training pakai normalisasi)", value=False)

uploaded = st.file_uploader("Upload gambar (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Gambar yang diupload", width=300)

    if st.button("Predict", type="primary"):
        try:
            model = load_model()
            x = preprocess_image(img)

            if use_rescale:
                x = x / 255.0

            pred = model.predict(x, verbose=0)

            st.write("Pred raw:", pred)
            prob = float(np.squeeze(pred))
            st.write("Prob (dog=1):", prob)

            # pred biasanya shape (1,1) untuk binary sigmoid
            prob = float(pred[0][0]) if pred.ndim == 2 else float(pred[0])
            label_idx = 1 if prob >= 0.5 else 0
            label = CLASS_NAMES[label_idx]
            confidence = prob if label_idx == 1 else (1.0 - prob)

            st.success(f"Prediksi: **{label.upper()}**")
            st.metric("Confidence", f"{confidence*100:.2f}%")
            st.caption(f"Raw probability (dog=1): {prob:.4f}")

        except Exception as e:
            st.error(f"Gagal prediksi: {e}")
else:
    st.info("Silakan upload gambar untuk mulai.")
