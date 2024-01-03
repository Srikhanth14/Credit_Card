# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:57:40 2024

@author: ELCOT
"""

import streamlit as st
import pandas as pd
def data_overview():
    # Dataset Information
    st.title("Dataset Overview:")
    st.write("The predictive model is trained on a dataset containing credit card transactions, with features including Time, Amount, and principal components (V1 to V28). The 'Class' column indicates whether the transaction is fraudulent (1) or genuine (0).")

    # Data Source
    st.header("Data Source:")
    st.write("For more details, you can explore the dataset on [here](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)")

    # Sample Data
    st.header("Sample Data:")
    st.write("Here's a glimpse of the credit card transaction dataset:")
    data = pd.read_csv("creditcard.csv")  # Update with the actual file name
    st.dataframe(data.head())

    # Display your sample data here
    st.subheader("Download Dataset")
    st.write("You can download the full Credit Card Fraud Detection dataset for further exploration:")

    def data_read(data):
        return data.to_csv().encode('utf-8')

    csv = data_read(data)

    st.download_button(
        label='Download Sample Data',
        data=csv,
        file_name='credit_card_dataset.csv',
        mime='text/csv'
    )

    # Input Your Data
    st.header("Input Your Data:")
    st.write("Want predictions for your specific transaction details? Enter your data in the input form and discover the forecasted fraud or genuineness.")

    # Guidance on Data Format
    st.header("Guidance on Data Format:")
    st.write("To ensure successful predictions, enter your data with the same features as the sample data. Include columns for Time, Amount, and principal components (V1 to V28).")

    # GitHub Link
    st.header("GitHub Repository:")
    st.write("Explore the code and details of this project on my GitHub repository:")
    st.write("[Credit Card Fraud Detection GitHub Repository](https://colab.research.google.com/github/Srikhanth14/CODSOFT/blob/main/Project_2_Credit_Card_Fraud_Detection.ipynb)")

    # Conclusion
    st.write("Ready to get predictions for your data? Input your transaction details in the form, and let the Credit Card Fraud Detection app work its magic!")
