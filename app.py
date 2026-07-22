import streamlit as st
import pandas as pd
import joblib

model=joblib.load("heart_model.pkl")
scaler=joblib.load("scaler.pkl")
columns=joblib.load("columns.pkl")

st.set_page_config(
    page_title="Heart Disease Prediction",
    layout="centered"
)

st.title("Heart Disease Prediction")
st.write("Enter patient Details........")

age=st.number_input("Age",min_value=1,max_value=120,value=40)

sex=st.selectbox(
    "sex",
    ["M","F"]
)

chestpain = st.selectbox(
    "Chest Pain Type",
    ["ATA","NAP","ASY","TA"]
)

bp=st.number_input(
    "Resting Blood Pressure",
    min_value=50,
    max_value=250,
    value=120
)

chol=st.number_input(
    "Cholesterol",
    min_value=0,
    max_value=700,
    value=200
)

fbs=st.selectbox(
    "Fasting Blood Suger",
    [0,1]
)

ecg=st.selectbox(
    "Resting ECG",
    ["Normal","ST","LVH"]
)

maxhr=st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    max_value=250,
    value=150
)

angina=st.selectbox(
    "Exercise Angina",
    ["N","Y"]
)

oldpeak=st.number_input(
    "Old Peak",
    value=1.0
)

slope=st.selectbox(
    "ST Slope",
    ["Up","Flat","Down"]
)

if st.button("Predict"):

    sample = {
        "Age": age,
        "Sex": sex,
        "ChestPainType": chestpain,
        "RestingBP": bp,
        "Cholesterol": chol,
        "FastingBS": fbs,
        "RestingECG": ecg,
        "MaxHR": maxhr,
        "ExerciseAngina": angina,
        "Oldpeak": oldpeak,
        "ST_Slope": slope
    }

    sample_df = pd.DataFrame([sample])

    sample_df = pd.get_dummies(sample_df, drop_first=True)

    sample_df = sample_df.reindex(columns=columns, fill_value=0)

    sample_scaled = scaler.transform(sample_df)

    prediction = model.predict(sample_scaled)

    if prediction[0] == 1:
        st.error("Heart Disease: Yes")
    else:
        st.success("Heart Disease: No")