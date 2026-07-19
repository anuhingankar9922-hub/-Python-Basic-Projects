import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_model.pkl")

city_encoder = joblib.load("city_encoder.pkl")
state_encoder = joblib.load("state_encoder.pkl")
country_encoder = joblib.load("country_encoder.pkl")

st.title("House Price Prediction")

st.write("Enter House Details")

bedrooms = st.number_input("Bedrooms", 1, 10, 3)

bathrooms = st.number_input("Bathrooms", 1.0, 10.0, 2.0)

sqft_living = st.number_input("Sqft Living", 500, 15000, 2000)

sqft_lot = st.number_input("Sqft Lot", 1000, 1000000, 5000)

floors = st.number_input("Floors", 1.0, 5.0, 1.0)

waterfront = st.selectbox("Waterfront", [0,1])

view = st.selectbox("View", [0,1,2,3,4])

condition = st.slider("Condition",1,5,3)

sqft_above = st.number_input("Sqft Above",500,10000,1500)

sqft_basement = st.number_input("Sqft Basement",0,5000,500)

yr_built = st.number_input("Year Built",1900,2024,2000)

yr_renovated = st.number_input("Year Renovated",0,2024,0)

city = st.selectbox(
    "City",
    city_encoder.classes_
)

statezip = st.selectbox(
    "State Zip",
    state_encoder.classes_
)

country = st.selectbox(
    "Country",
    country_encoder.classes_
)

if st.button("Predict Price"):

    city = city_encoder.transform([city])[0]
    statezip = state_encoder.transform([statezip])[0]
    country = country_encoder.transform([country])[0]

    data = pd.DataFrame([[

        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated,
        city,
        statezip,
        country

    ]], columns=[

        'bedrooms',
        'bathrooms',
        'sqft_living',
        'sqft_lot',
        'floors',
        'waterfront',
        'view',
        'condition',
        'sqft_above',
        'sqft_basement',
        'yr_built',
        'yr_renovated',
        'city',
        'statezip',
        'country'

    ])

    prediction = model.predict(data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")