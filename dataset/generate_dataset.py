import pandas as pd
import numpy as np

# ===============================
# Configuration
# ===============================
np.random.seed(42)
ROWS = 10000   # number of students

# ===============================
# Generate base student features
# ===============================
df = pd.DataFrame({
    "attendance": np.random.randint(40, 100, ROWS),        # percentage
    "internal_marks": np.random.randint(30, 100, ROWS),    # marks
    "behavior_score": np.random.randint(1, 10, ROWS),      # 1 (worst) to 9 (best)
    "study_hours": np.round(np.random.uniform(0.5, 6, ROWS), 1)
})

# ===============================
# Final academic outcome (ML target)
# ===============================
df["final_result"] = (
    (df["attendance"] >= 70) &
    (df["internal_marks"] >= 55) &
    (df["behavior_score"] >= 4)
).astype(int)

# ===============================
# Academic Risk Classification
# ===============================
def classify_risk(row):
    # Severe behavioral issues → always high risk
    if row["behavior_score"] <= 2:
        return "High"

    # Strong academic risk
    if row["attendance"] < 60 or row["internal_marks"] < 45:
        return "High"

    # Borderline / watchlist students
    if row["attendance"] < 75 or row["internal_marks"] < 60:
        return "Medium"

    # Academically stable students
    return "Low"

df["risk_level"] = df.apply(classify_risk, axis=1)

# ===============================
# Save dataset
# ===============================
df.to_csv("student_data.csv", index=False)

print("✅ Dataset generated successfully")
print("Total students:", len(df))
print(df.head())
