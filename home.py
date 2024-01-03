# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:54:16 2024

@author: ELCOT
"""
import streamlit as st
def home():
    # Introduction
    st.title("Credit Card Fraud Detection App")
    st.write("Welcome to the Credit Card Fraud Detection App, where advanced machine learning techniques help identify fraudulent transactions.")
    
    # Key Features
    st.subheader("Key Features:")
    st.write("1. **Predictive Analytics:** Uncover the power of predictive analytics in identifying potential credit card fraud. The model analyzes transaction features to make accurate predictions.")

    st.write("2. **User-Friendly Interface:** Navigate effortlessly through the app. Input transaction details and receive predictions on the authenticity of the transaction.")

    st.write("3. **Data Insights:** Gain insights into the dataset with interactive charts. Explore patterns and understand the factors that contribute to fraud detection.")

    # About the Project
    st.subheader("About the Project:")
    st.write("The Credit Card Fraud Detection project focuses on leveraging machine learning to enhance security in financial transactions. Explore the features that aid in distinguishing between genuine and fraudulent transactions.")

    # About You
    st.subheader("About You:")
    st.write("Curious about the mind behind the project? I'm SRIKHANTH R, a data enthusiast dedicated to unraveling insights from complex datasets.")
    st.write("Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/srikhanth-r) or explore more projects on my [portfolio](https://www.datascienceportfol.io/srikhanth_r). Let's together create a safer financial environment!")

    # Call to Action
    st.write("Ready to explore the world of credit card fraud detection? Head over to the **Fraud Prediction** page to input transaction details and get predictions!")
