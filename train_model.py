import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data.csv")

df = df.drop(["date", "street"], axis=1)

le_city = LabelEncoder()
le_state = LabelEncoder()
le_country = LabelEncoder()

df["city"] = le_city.fit_transform(df["city"])
df["statezip"] = le_state.fit_transform(df["statezip"])
df["country"] = le_country.fit_transform(df["country"])

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()

model.fit(X_train, y_train)

joblib.dump(model, "house_price_model.pkl")

joblib.dump(le_city, "city_encoder.pkl")
joblib.dump(le_state, "state_encoder.pkl")
joblib.dump(le_country, "country_encoder.pkl")

print("Model Saved Successfully!")