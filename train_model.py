import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("ford_car_dataset.csv")

X = df.drop("price", axis=1)
y = df["price"]

X = pd.get_dummies(X)

encoded_columns = X.columns

numerical_columns = [
    "year",
    "mileage",
    "tax",
    "mpg",
    "engineSize"
]

scaler = StandardScaler()

X[numerical_columns] = scaler.fit_transform(X[numerical_columns])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "LR_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoded_columns, "columns.pkl")

print("Model Saved Successfully!")