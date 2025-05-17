import streamlit as st
import joblib
import numpy as np

# Load model dan scaler
model = joblib.load('models/model_random_forest.joblib')
scaler = joblib.load('models/model_random_forest.pkl')


# Fungsi prediksi
def predict_attrition(inputs):
    input_array = np.array(inputs).reshape(1, -1)
#     input_array = scaler.transform(input_array)
    prediction = model.predict(input_array)
    return prediction[0]  # ambil hasil prediksi langsung


# Streamlit UI
st.title('Employee Attrition Prediction')

# Input data user
age = st.number_input('Age',
                      min_value=18,
                      max_value=65,
                      value=30)
daily_rate = st.number_input('Daily Rate',
                             min_value=0,
                             max_value=2000,
                             value=800)
distance_from_home = st.number_input('Distance From Home (km)',
                                     min_value=0,
                                     max_value=50,
                                     value=10)
environment_satisfaction = st.selectbox('Environment Satisfaction',
                                        [1, 2, 3, 4],
                                        format_func=lambda x: f'Level {x}')
hourly_rate = st.number_input('Hourly Rate',
                              min_value=0,
                              max_value=300,
                              value=60)
monthly_income = st.number_input('Monthly Income',
                                 min_value=1000,
                                 max_value=20000,
                                 value=5000)
monthly_rate = st.number_input('Monthly Rate',
                               min_value=0,
                               max_value=30000,
                               value=10000)
overtime = st.selectbox('OverTime',
                        [0, 1],
                        format_func=lambda x: 'Yes' if x == 1 else 'No')
total_working_years = st.number_input('Total Working Years',
                                      min_value=0,
                                      max_value=40,
                                      value=10)
years_at_company = st.number_input('Years at Company',
                                   min_value=0,
                                   max_value=40,
                                   value=5)

# Masukkan input ke list sesuai urutan fitur model
input_data = [
    age,
    daily_rate,
    distance_from_home,
    environment_satisfaction,
    hourly_rate,
    monthly_income,
    monthly_rate,
    overtime,
    total_working_years,
    years_at_company
]

# Tombol prediksi
if st.button('Predict Attrition'):
    with st.spinner('Predicting...'):
        prediction = predict_attrition(input_data)

    result = 'Resign' if prediction == 1 else 'Tidak Resign'
    st.success(f"The model predicts: **{result}**")
