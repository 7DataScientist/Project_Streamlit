# Framework Library
import streamlit as st


# Core Libraries
import pandas as pd
import numpy as np


# Fxns

def run_eda_app():
    st.header("EDA")
    
    submenu = ["Descriptive",'Plot']
    st.sidebar.selectbox("Memu",submenu)
    
if __name__ == "__main__":
    run_eda_app()