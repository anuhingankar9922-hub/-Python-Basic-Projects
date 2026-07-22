import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

df = pd.read_csv("heart.csv")

print(df.head())

X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

X = pd.get_dummies(X, drop_first=True)

columns = X.columns

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nActual Values")
print(y_test.head(10).values)

print("\nPredicted Values")
print(y_pred[:10])

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

print("TN =", TN)
print("FP =", FP)
print("FN =", FN)
print("TP =", TP)

print("\nAccuracy :", accuracy_score(y_test, y_pred))
print("Precision :", precision_score(y_test, y_pred))
print("Recall :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

joblib.dump(model, "heart_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(columns, "columns.pkl")

print("\nModel Saved Successfully!")

model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

print("Model Loaded Successfully!")

sample = {
    "Age":55,
    "Sex":"M",
    "ChestPainType":"ATA",
    "RestingBP":140,
    "Cholesterol":250,
    "FastingBS":0,
    "RestingECG":"Normal",
    "MaxHR":150,
    "ExerciseAngina":"N",
    "Oldpeak":1.5,
    "ST_Slope":"Up"
}

sample_df = pd.DataFrame([sample])

sample_df = pd.get_dummies(sample_df, drop_first=True)

sample_df = sample_df.reindex(columns=columns, fill_value=0)

sample_scaled = scaler.transform(sample_df)

prediction = model.predict(sample_scaled)

if prediction[0] == 1:
    print("Heart Disease : Yes")
else:
    print("Heart Disease : No")