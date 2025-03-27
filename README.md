# ❤️ Heart Disease Prediction with Machine Learning

This project is a complete machine learning pipeline that analyzes and predicts heart disease risk using the UCI Cleveland dataset. It includes preprocessing, feature selection, supervised and unsupervised learning, model optimization, and deployment with a Streamlit app.

---

## 📊 Dataset
- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Used File:** `cleveland.data`
- **Target:** Presence of heart disease (binary classification)

---

## 🚀 Project Features

### ✅ Data Preprocessing
- Handle missing values
- Data cleaning and conversion
- Feature scaling using StandardScaler and MinMaxScaler

### ✅ Dimensionality Reduction
- PCA (Principal Component Analysis) to retain essential features

### ✅ Feature Selection
- Random Forest feature importance
- Recursive Feature Elimination (RFE)
- Chi-Square test (Chi2)

### ✅ Supervised Learning Models
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

### ✅ Unsupervised Learning
- K-Means Clustering
- Hierarchical Clustering (Dendrogram visualization)
- ARI Score Evaluation

### ✅ Hyperparameter Tuning
- GridSearchCV for best Logistic Regression parameters

### ✅ Deployment
- Export final model as `.pkl` using `joblib`
- Build and deploy Streamlit App for real-time user input and prediction

---

## 📂 Project Structure

```
Heart-Disease-UCI/
├── cleveland.data
├── heart_disease_cleaned.csv
├── final_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── Heart_Disease_Full_ML_Project_Pipeline.ipynb
```

---

## ▶️ How to Run

### 🔹 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 🔹 2. Run Streamlit App
```bash
streamlit run app.py
```

---

## 📈 Model Performance (Best Model: Logistic Regression)
- Accuracy: ~78-80%
- ROC AUC: ~0.84
- Precision, Recall, and F1 balanced

---

## 🌐 Optional: Deploy Publicly with Ngrok
```bash
ngrok http 8501
```

---

## 👤 Author
- **Name:** Marwan Yasser Hassan
- **Project Type:** ML Capstone / Health Prediction Tool
- **Language:** Python
