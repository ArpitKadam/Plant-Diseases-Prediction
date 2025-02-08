# 🌿 Plant Diseases Prediction using Deep Learning 🔥

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

## 🌟 Overview
This project is a **Plant Diseases Prediction App** built using **Streamlit** and **TensorFlow**. The app allows users to upload plant leaf images and get a disease prediction using a pre-trained deep learning model.

## 🚀 Features
✅ Interactive **Streamlit** web app 🖥️
✅ Uses a **pre-trained CNN model** (`trained_cnn_model.keras`) 🧠
✅ Accepts **leaf images** for disease classification 🌱
✅ Provides **real-time disease detection** 🏥

## 🛠️ Technologies Used
- 🐍 **Python**
- 🔥 **TensorFlow/Keras** (Deep Learning Model)
- 🎨 **Streamlit** (Web App Framework)
- 📊 **Pandas, NumPy** (Data Processing)
- 📈 **Matplotlib, Seaborn** (Visualization)

## 📂 Directory Structure
```
📁 arpitkadam-plant-diseases-prediction/
├── 📝 main.py                  # Streamlit application
├── 📜 requirements.txt        # Dependencies
├── 🧪 test.ipynb              # Testing and validation script
├── 🎯 train.ipynb             # Model training script
├── 🤖 trained_cnn_model.keras # Pre-trained deep learning model
├── 📄 training_hist.json       # Training history file
├── 🖼️ Visualization_images/    # Training performance images
│   ├── Epochs vs. Training Accuracy.JPG
│   ├── Training Accuracy and Validation Accuracy vs. No. of Epochs.JPG
│   └── Validation Accuracy vs. No. of Epochs.JPG
└── 📂 static/                 # Static assets (if any)
```

## ⚡ Installation & Setup

### 🏗️ 1. Clone the Repository
```bash
git clone https://github.com/your-username/arpitkadam-plant-diseases-prediction.git
cd arpitkadam-plant-diseases-prediction
```

### 📦 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ 3. Run the Application
```bash
streamlit run main.py
```

## 🎯 How to Use
1. 📸 Upload an image of the **plant leaf**.
2. 🎯 Click on **Predict Disease**.
3. 📢 The app will display the **predicted disease** along with confidence scores.

## 🔢 Example Output
```
Predicted Disease: Powdery Mildew
Confidence: 92.5%
```

## 📊 Model Performance
The following graphs illustrate the model's training performance:

![Training Accuracy](https://github.com/ArpitKadam/Plant-Diseases-Prediction/blob/main/Visualization_images/Training%20Accuracy%20and%20Validation%20Accuracy%20vs.%20No.%20of%20Epochs.JPG)

## 🔖 Notes
- 📊 The model is trained on **plant disease datasets**.
- ⚙️ Predictions depend on the **quality and resolution of the uploaded image**.
- 🛠️ This is a **basic prototype** and may require further tuning for better accuracy.

## 📜 License
This project is open-source and available under the **MIT License**.

---
### 🚀 Developed by **Arpit Kadam**
📧 Contact: [📩 arpitkadam922@gmail.com](mailto:arpitkadam922@gmail.com)

