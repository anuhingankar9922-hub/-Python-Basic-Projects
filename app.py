import streamlit as st     # Used for creating the web application
import pandas as pd        # Used for DataFrame operations
import joblib              # Used to load saved model and scaler

model = joblib.load("LR_model.pkl")
scaler = joblib.load("scaler.pkl")
encoded_columns = joblib.load("columns.pkl")

st.set_page_config(                         # Configure the Streamlit page.
    page_title="Ford Car Price Predictor",  # page_title sets the title displayed on the browser tab.
    layout="centered"                       # layout="centered" keeps the application centered for a clean and user-friendly interface.
)

st.title("Ford Car Price Predictor")

st.write("Enter the car details below to predict its selling price.")

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2025,
    value=2018
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    value=20000
)

tax = st.number_input(
    "Road Tax",
    min_value=0,
    value=150
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    value=50.0
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0.0,
    value=1.5
)

# selectbox is used because it allows the user to select only one valid option.
transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto"]
)

fuelType = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

model_name = st.text_input("Car Model")

predict = st.button("Predict Price")


if predict:

    input_data = {
        "year": year,
        "mileage": mileage,
        "tax": tax,
        "mpg": mpg,
        "engineSize": engineSize,
        "model": model_name,
        "transmission": transmission,
        "fuelType": fuelType
    }

    input_df = pd.DataFrame([input_data])

    input_df = pd.get_dummies(input_df)

    for col in encoded_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[encoded_columns]


    numerical_columns = [
        "year",
        "mileage",
        "tax",
        "mpg",
        "engineSize"
    ]

    input_df[numerical_columns] = scaler.transform(
        input_df[numerical_columns]
    )


    prediction = model.predict(input_df)

    st.success(f"Estimated Car Price: £ {prediction[0]:,.2f}")