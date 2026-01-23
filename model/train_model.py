import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "dataset", "student_data.csv")

df = pd.read_csv(DATA)

X = df[["attendance", "internal_marks", "behavior_score"]]
y = df["final_result"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(BASE, "model", "model.pkl"))
joblib.dump(scaler, os.path.join(BASE, "model", "scaler.pkl"))

print("✅ Model trained & saved")
