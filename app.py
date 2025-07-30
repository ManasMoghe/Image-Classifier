import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("cats_vs_dogs_cnn.keras")

# Set image size
IMG_SIZE = 100  # Match your model input size

st.set_page_config(page_title="Cat vs Dog Classifier", page_icon="🐾")
st.title("🐱🐶 Cat vs Dog Image Classifier")
st.write("Upload an image and I'll predict if it's a **Cat** or a **Dog**!")

# File uploader
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

def preprocess(image):
    # Convert to grayscale first
    image = image.convert('L')  # 'L' mode = grayscale
    img = np.array(image)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = img.reshape(1, IMG_SIZE, IMG_SIZE, 1)  # Add grayscale channel
    return img

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)


    with st.spinner("Predicting..."):
        processed_image = preprocess(image)
        prediction = model.predict(processed_image)[0][0]

        label = "Dog 🐶" if prediction > 0.5 else "Cat 🐱"
        confidence = prediction if prediction > 0.5 else 1 - prediction
        confidence_percent = round(confidence * 100, 2)

        st.success(f"Prediction: **{label}**")
        st.info(f"Confidence: **{confidence_percent}%**")
