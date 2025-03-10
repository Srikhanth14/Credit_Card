import streamlit as st
from streamlit_option_menu import option_menu
import home,Dataset,Visualization,form

st.set_page_config(page_title="Credit Card Fraud Detection",page_icon="💳",layout="wide")
selected = option_menu(
                        menu_title="Credit Card Fraud",
                        options=["Home", "Data Overview", "Visualization","Fraud Detection"],
                        icons=["house-slash-fill", "database-slash", "radioactive","building-fill-check"],
                        menu_icon="credit-card-2-front",
                        default_index=0,
                        orientation="horizontal"
                      )

if selected == "Home":
    home.home()
if selected == "Data Overview":
    Dataset.data_overview()
if selected == "Visualization":
    Visualization.charts()
if selected == "Fraud Detection":
   form.input_form()
