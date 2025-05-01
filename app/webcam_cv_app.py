# app/webcam_cv_app.py

import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Webcam Emotion Detection", page_icon="📷")

st.title("📷 Webcam Live Feed for Emotion Detection (Prototype)")

run = st.checkbox('Start Webcam')
FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.warning("Failed to access webcam. Please check your camera permissions.")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Webcam stopped.')

camera.release()
