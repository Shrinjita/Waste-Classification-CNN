# Waste-Classification-CNN

This repository contains a **deep learning-based waste classification system** using **CNN and Transfer Learning**. The project includes a **Streamlit dashboard** for real-time waste classification and visualization.

---

## 🚀 Features:
- **CNN-based Classification**: Classifies waste into **Organic (O)** and **Recyclable (R)**.
- **Transfer Learning & Ensemble Learning**: Enhances classification accuracy.
- **Streamlit Dashboard**: Upload an image and get predictions with charts.
- **Data Visualization**: Pie charts and line charts for insights.

---

## 📁 Folder Structure:
```
Waste-Classification-CNN/
│── models/                     # Trained CNN models
│   ├── cnn_model.h5             # Standard CNN model
│   ├── ensemble_model.h5        # Transfer Learning + Ensemble model
│
│── dataset/                     # Waste classification dataset
│   ├── TRAIN/
│   │   ├── O/                   # Organic waste images
│   │   ├── R/                   # Recyclable waste images
│   ├── TEST/
│       ├── O/                   # Test set for Organic
│       ├── R/                   # Test set for Recyclable
│
│── app.py                        # Streamlit dashboard
│── cnn.py                         # Model loading & prediction
│── requirements.txt               # Python dependencies
│── README.md                      # Project documentation
```

---

## ⚙️ Installation:
### 1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/Waste-Classification-CNN.git
cd Waste-Classification-CNN
```

### 2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit Dashboard:
```bash
streamlit run app.py
```

---

## 🎯 Usage:
1. Upload an image of waste.
2. The model predicts **Organic** or **Recyclable**.
3. Confidence scores and **visual analytics (pie & line charts)** are displayed.

---

## 📌 Future Enhancements:
- Integrate **Object Detection** for multi-class waste classification.
- Add **real-time camera-based waste recognition**.
- Deploy as a **web app** or **mobile app**.

---

### **📢 Contributing:**
Feel free to open issues and submit pull requests to enhance the model and dashboard.
