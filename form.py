# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:32:28 2024

@author: ELCOT
"""


import streamlit as st
import numpy as np
import pandas as pd
from joblib import load


def form():
    # Function to make predictions
    def make_prediction(input_data):
        
        loaded_model=load('credit_trained_model.joblib')
        # Change the input data to a numpy array
        input_data_np_array = np.asarray(input_data)
        
        # Reshape the numpy array as we are predicting for only one instance
        input_data_reshaped = input_data_np_array.reshape(1, -1)
        
        # Make predictions using the trained model
        columns = ['V1', 'V2', 'V3', 'V4', 'normalized_amount']
        input_data_reshaped_df = pd.DataFrame(input_data_reshaped, columns=columns)
        
        prediction = loaded_model.predict(input_data_reshaped_df)
        
        return prediction[0]
    
        # Streamlit input form
        def input_form():
            st.title("Credit Card Fraud Detection")
            st.write("Enter transaction details to check for fraud.")
            
            # Get user input
            v1 = st.number_input("Enter V1:")
            v2 = st.number_input("Enter V2:")
            v3 = st.number_input("Enter V3:")
            v4 = st.number_input("Enter V4:")
            normalized_amount = st.number_input("Enter Normalized Amount:")
            
            input_data = [v1, v2, v3, v4, normalized_amount]
            
            # Make prediction
            if st.button("Check for Fraud"):
                prediction_result = make_prediction(input_data)
                if prediction_result == 0:
                    st.success("The transaction is not fraudulent.")
                else:
                    st.warning("The transaction is fraudulent.")
        
        input_form()

