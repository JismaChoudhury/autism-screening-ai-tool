# app/main_app.py

import streamlit as st

st.set_page_config(page_title="Autism Screening Tool", page_icon="🧠")

st.title("🧠 Autism Screening Tool (Questionnaire-Based)")

st.write("""
This tool uses a machine learning model to screen for early signs of Autism Spectrum Disorder (ASD) based on simple questionnaire inputs.
""")

# Example input fields (you'll replace/expand later)
age = st.number_input("Age", min_value=1, max_value=100)
gender = st.selectbox("Gender", ("Male", "Female", "Other"))
family_history = st.radio("Family history of ASD?", ("Yes", "No"))
communication_skill = st.slider("Communication Skill Level", 0, 10)

if st.button("Predict ASD Risk"):
    st.success("Model prediction placeholder: (Prediction will appear here after integration)")

st.markdown("---")
st.caption("Disclaimer: This tool is for educational purposes only. Always consult a healthcare provider.")
