from flask import Flask, request, Response,jsonify, render_template, send_file
import pandas as pd
import joblib
import os
import io
import pickle
from io import BytesIO
import streamlit as st
import warnings


import joblib

model_path = 'model/logistic_regression_model.pkl'
model = joblib.load(model_path)
st.write("Model loaded successfully!")

import sklearn
import sys

st.write("Python version:", sys.version)
st.write("scikit-learn version:", sklearn.__version__)

if __name__ == '__main__':
    main()
