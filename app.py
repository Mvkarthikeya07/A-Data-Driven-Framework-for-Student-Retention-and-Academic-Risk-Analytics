from flask import Flask, render_template
import pandas as pd
import json
import calendar

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Load dataset
    df = pd.read_csv("dataset/student_data.csv")

    # ===============================
    # KPI METRICS (INSTITUTION LEVEL)
    # ===============================
    total_students = len(df)
    retention_rate = round(df["final_result"].mean() * 100, 2)
    avg_attendance = round(df["attendance"].mean(), 2)

    low_risk = len(df[df["risk_level"] == "Low"])
    medium_risk = len(df[df["risk_level"] == "Medium"])
    high_risk = len(df[df["risk_level"] == "High"])

    # ===============================
    # STUDENT TABLE (SAMPLED VIEW)
    # ===============================
    students = df.sample(25).to_dict(orient="records")

    # ===============================
    # MONTH-WISE ATTENDANCE TREND
    # ===============================
    labels = list(calendar.month_abbr)[1:]   # ['Jan', 'Feb', ..., 'Dec']
    values = df.groupby(df.index % 12)["attendance"].mean().tolist()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        retention_rate=retention_rate,
        avg_attendance=avg_attendance,
        low_risk=low_risk,
        medium_risk=medium_risk,
        high_risk=high_risk,
        students=students,
        labels=json.dumps(labels),
        values=json.dumps(values)
    )

if __name__ == "__main__":
    app.run(debug=True)
