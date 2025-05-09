from flask import Flask, request, Response,jsonify, render_template, send_file
import pandas as pd
import joblib
import os
import io
import pickle
from io import BytesIO
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

import subprocess
import streamlit as st

def upgrade_streamlit():
    result = subprocess.run(['pip', 'install', '--upgrade', 'streamlit'], capture_output=True, text=True)
    st.write(result.stdout)
    st.write(result.stderr)

st.button('Upgrade Streamlit', on_click=upgrade_streamlit)


@st.cache_resource
def load_model():
    model = joblib.load('./logistic_regression_model.pkl')
    return model



def prediction(input_data, model):
    # Assuming the model expects a list of texts for prediction
    prediction = model.predict(input_data)
    return prediction

def main():
    st.header("C2P Prediction App")
    st.write("Model file exists:", os.path.exists("logistic_regression_model.pkl"))
    st.subheader("Assessing alerts relevant for our products or business")
    st.write("Upload a Excel file for prediction:")
    file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"], key ='upload')
    
    if file is not None:
        try:
            df = pd.read_excel(file)
                                  
            df = df[['Name','Summary']]
            
            df.rename(columns={'Name':'C2P Alerts_mod'},inplace=True)
            
                      
            model =load_model()
            input_data = df[['C2P Alerts_mod','Summary']]
            
            # Combine the two inputs
            predictions = prediction(input_data, model)

            st.write(predictions.tolist())

            # Add predictions to DataFrame
            
            df['Predictions'] = predictions
            
            dataset = pd.DataFrame({})
            
            dataset = df
            pd.set_option('display.max_colwidth', None)
            
            excel_buffer = io.BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    dataset.to_excel(writer, index=False, sheet_name='Predictions')
                
            excel_buffer.seek(0)  # Move to the beginning of the buffer
            
            st.write("Prediction Results:")
            
            st.dataframe(df.style.applymap(lambda x: 'background-color: green' if x == 'YES' else 'background-color: red', subset=['Predictions']))

                
                # Provide a download button for the Excel file
            st.download_button(
                    label="Download Predictions as Excel",
                    data=excel_buffer, key ='three',
                    file_name='predictions.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
