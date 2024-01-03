# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 19:01:39 2024

@author: ELCOT
"""


import streamlit as st
from PIL import Image

def charts():
    # Page Title
    st.title("Model Comparison Visualizations")

    # Introduction
    st.write("Explore visualizations highlighting model comparison and performance metrics for Credit Card Fraud Detection.")

    # Image 1: Class Distribution Countplot
    st.header("1. Class Distribution Countplot")
    image1 = Image.open("Distribution.png")  # Replace with your image file
    st.image(image1, caption="Fraud and Genuine Transaction Distribution", use_column_width=True)

    # Model Comparison Subplot
    st.header("2. Model Comparison Metrics")

    # Load model comparison subplot image
    model_comparison_image = Image.open("Metrices.png")  # Replace with your image file
    st.image(model_comparison_image, caption="Model Comparison Metrics", use_column_width=True)

    # Call to Action
    st.write("Ready to explore more or make predictions? Head to the **Fraud Prediction** page for detailed insights and predictions based on the visualizations.")
