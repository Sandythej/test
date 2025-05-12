from flask import Flask, request, Response,jsonify, render_template, send_file
import pandas as pd
import joblib
import os
import io
import pickle
from io import BytesIO
import streamlit as st
import warnings


@st.cache_resource
def load_model():
    model = joblib.load('./logistic_regression_model.pkl')
    return model

def prediction(input_data, model):
    # Assuming the model expects a list of texts for prediction
    prediction = model.predict(input_data)
    return prediction

def main():
    st.header("Email Prediction App")
    st.write("Model file exists:", os.path.exists("logistic_regression_model.pkl"))
    file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"], key='upload')
    if file:
        df = pd.read_excel(file)
        st.write(df.head())
    model = load_model()
    st.write("Model loaded:", model is not None)

if __name__ == '__main__':
    main()
