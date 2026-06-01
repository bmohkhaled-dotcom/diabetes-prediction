
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello World!")
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Diabetes Readmission Prediction")

time_in_hospital = st.number_input("Time in Hospital", 1, 20, 5)
num_lab_procedures = st.number_input("Lab Procedures", 0, 150, 40)
num_procedures = st.number_input("Procedures", 0, 20, 2)
num_medications = st.number_input("Medications", 0, 100, 10)
number_outpatient = st.number_input("Outpatient Visits", 0, 20, 0)
number_emergency = st.number_input("Emergency Visits", 0, 20, 0)
number_inpatient = st.number_input("Inpatient Visits", 0, 20, 0)

if st.button("Predict"):

    total_visits = (
        number_outpatient +
        number_emergency +
        number_inpatient
    )

    data = pd.DataFrame({
        "time_in_hospital":[time_in_hospital],
        "num_lab_procedures":[num_lab_procedures],
        "num_procedures":[num_procedures],
        "num_medications":[num_medications],
        "number_outpatient":[number_outpatient],
        "number_emergency":[number_emergency],
        "number_inpatient":[number_inpatient],
        "total_visits":[total_visits]
    })

    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(f"Prediction = {prediction[0]}")
