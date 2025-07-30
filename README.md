# 🐱🐶 Cat vs Dog Image Classifier using CNN

A deep learning project that classifies images of cats and dogs using a custom-built Convolutional Neural Network (CNN) in TensorFlow/Keras. Trained on image data flattened into CSV format and reshaped back for model input. A Streamlit web app is included for interactive predictions using a separate grayscale-trained model.

---

## 📂 Dataset

The dataset used in training the CNN model (in `cnn.ipynb`) is structured as follows:

- `input.csv`: Training images (1999 samples, each 100×100×3 = 30,000 pixels flattened)
- `label.csv`: Binary labels (0 = Cat, 1 = Dog)
- `input_test.csv` & `label_test.csv`: Reserved for future use

Images are normalized and reshaped to `(100, 100, 3)` before training.

---

## 🛠️ Preprocessing

- Loaded CSV data using **pandas**
- Normalized pixel values to range `[0, 1]`
- Reshaped flattened arrays into image format
- Split into training and validation sets (80/20)

---

## 🧠 Model Architecture

The CNN model (from `cnn.ipynb`) was built using the Keras Sequential API:


- **Loss Function**: Binary Crossentropy  
- **Optimizer**: Adam  
- **Metric**: Accuracy

---

## 🏋️ Training

- **Epochs**: 45  
- **Batch Size**: 32  
- **Validation Split**: 0.2  
- **Runtime Environment**: Google Colab (T4 GPU)

---

## 🌐 Web App (Streamlit)

A separate web interface is available via `app.py`, using a grayscale model stored in `cats_vs_dogs_cnn.keras`.

- **Framework**: Streamlit  
- **Input Shape**: (100, 100, 1) grayscale  
- **Upload Types**: `.jpg`, `.jpeg`, `.png`  
- **Output**: Cat 🐱 or Dog 🐶 with confidence score

### 🔧 How to Run

```bash
git clone https://github.com/yourusername/cat-vs-dog-classifier.git
cd cat-vs-dog-classifier
pip install -r requirements.txt
streamlit run app.py
