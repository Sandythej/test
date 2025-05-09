import streamlit as st

# Dummy prediction function (replace with your actual model)
def predict(input_value):
    # For example, a simple model that doubles the input
    return input_value * 2

def main():
    st.title("Simple Prediction App")

    # Input widget
    user_input = st.number_input("Enter a number", value=0)

    # Button to trigger prediction
    if st.button("Predict"):
        prediction = predict(user_input)
        st.success(f"Prediction result: {prediction}")

if __name__ == "__main__":
    main()
