# app.py
import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('final_model.pkl')

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction App")

st.markdown("أدخل بياناتك الصحية وشوف هل في خطر محتمل لأمراض القلب؟")

# Input fields
age = st.slider("السن", 20, 100, 50)
trestbps = st.slider("ضغط الدم أثناء الراحة", 80, 200, 120)
chol = st.slider("الكوليسترول", 100, 400, 200)
thalach = st.slider("أقصى معدل نبض", 60, 210, 150)
oldpeak = st.slider("ST depression", 0.0, 6.0, 1.0)

# Predict
if st.button("🔍 تنبؤ"):
    user_input = np.array([[age, trestbps, chol, thalach, oldpeak]])
    prediction = model.predict(user_input)[0]
    probability = model.predict_proba(user_input)[0][1]

    if prediction == 1:
        st.error(f"⚠️ خطر محتمل لمرض القلب - الاحتمالية: {probability:.2f}")
    else:
        st.success(f"✅ لا يوجد خطر ظاهر - الاحتمالية: {probability:.2f}")
