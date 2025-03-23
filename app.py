import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from cnn import predict_waste  # Using dummy model
from PIL import Image

st.title("Waste Classification Dashboard (Dummy)")

# File uploader
uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save uploaded image temporarily
    img_path = "temp.jpg"
    image.save(img_path)

    # Get dummy prediction
    predicted_class, confidence = predict_waste(img_path)

    # Display prediction result
    st.subheader(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")

    # Generate Pie Chart
    labels = ["Organic", "Recyclable"]
    sizes = [confidence if predicted_class == "Organic" else 1-confidence, 
             confidence if predicted_class == "Recyclable" else 1-confidence]
    colors = ["green", "blue"]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")  # Equal aspect ratio ensures pie is circular.
    
    st.pyplot(fig)

    #
