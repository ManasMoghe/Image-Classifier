# 🐱🐶 Cat vs Dog Image Classifier

This project is a simple web application built with [Streamlit](https://streamlit.io/) that uses a Convolutional Neural Network (CNN) model trained in TensorFlow/Keras to classify uploaded images as either **Cat** or **Dog**.

## 🚀 Demo

Upload any `.jpg`, `.jpeg`, or `.png` image of a cat or dog, and the app will predict the correct category with a confidence score.

<p align="center">
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-orange" alt="Streamlit Badge"/>
  <img src="https://img.shields.io/badge/Model-Keras|TensorFlow-blue" alt="Keras Badge"/>
</p>

---

## 📁 Project Structure


---

## 🧠 Model Overview

- **Architecture**: CNN trained on grayscale images resized to 100x100 pixels.
- **Output**: Binary classification with sigmoid activation (Cat = 0, Dog = 1).
- **Input Shape**: (100, 100, 1) — single-channel grayscale.

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/cat-vs-dog-classifier.git
   cd cat-vs-dog-classifier
