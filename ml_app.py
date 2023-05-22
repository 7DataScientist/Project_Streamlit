# Framework Library
import streamlit as st


# Core Libraries
import pandas as pd
import numpy as np


def run_ml_app():
    st.header("ML")
    
    submenu = ["Logistic Regression",'Decision Tree']
    st.sidebar.selectbox("Memu",submenu)
    
if __name__ == "__main__":
    run_ml_app()