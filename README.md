📊 A Data-Driven Framework for Student Retention & Academic Risk Analytics

An educational data analytics platform designed to analyze institutional student data and identify students at risk of academic underperformance or dropout using machine learning and interactive dashboards.

🧠 Project Overview

Educational institutions frequently face challenges related to:

Student dropouts

Declining academic performance

Delayed intervention strategies

Traditional monitoring approaches rely heavily on fragmented academic records and manual supervision, making it difficult to detect systemic risk patterns across large student populations.

This project introduces a data-driven academic intelligence framework that analyzes student academic indicators and detects risk levels through machine learning models and analytical visualization.

The system combines:

Educational Data Mining

Machine Learning Risk Prediction

Institutional Analytics Dashboards

Academic Engagement Analysis

By automating risk identification, the framework enables institutions to proactively detect vulnerable students and support data-driven academic decision-making.

🎯 Project Objectives

The framework aims to:

• Analyze institutional student data using academic indicators
• Detect students at risk of academic underperformance
• Provide institution-level retention analytics
• Visualize attendance and engagement patterns
• Support early academic intervention strategies
• Demonstrate the role of data analytics in education systems

🧠 Core Concept

Student success is influenced by multiple academic and behavioral factors.
This framework evaluates these indicators collectively to determine academic risk levels.

Key Academic Indicators
Indicator	Description
Attendance	Student attendance percentage
Internal Marks	Academic assessment scores
Behavior Score	Classroom engagement indicator
Study Hours	Self-reported study effort
Final Outcome	Academic performance result

Using these features, the system predicts whether a student belongs to:

🟢 Low Risk

🟠 Medium Risk

🔴 High Risk

The predictions are aggregated to generate institution-level analytics.

🤖 Machine Learning Pipeline

The project implements a machine learning pipeline for academic risk prediction.
````
Student Dataset
        │
        ▼
Data Preprocessing
(Cleaning & Feature Selection)
        │
        ▼
Feature Scaling
(Standardization)
        │
        ▼
Model Training
(Supervised Learning)
        │
        ▼
Risk Prediction
        │
        ▼
Analytics Dashboard
Model Components
File	Purpose
train_model.py	Trains the machine learning model
model.pkl	Serialized trained model
scaler.pkl	Feature scaling model

Saving trained models allows the system to perform predictions efficiently without retraining each time.
````
🖥 Interactive Analytics Dashboard

The platform includes a Flask-based web dashboard that provides institutional insights and risk visualization.

📌 Key Metrics

The dashboard displays:

Total number of students

Academic risk distribution

Institutional engagement patterns

Attendance analytics

Student performance overview

📊 Visual Analytics

The dashboard includes visual components such as:

Risk level distribution charts

Attendance trend analysis

Student performance tables

Academic engagement insights

These visualizations allow administrators to quickly identify patterns and detect students requiring intervention.
````
🏗 System Architecture
Student Dataset
        │
        ▼
Data Processing Layer
(Cleaning & Validation)
        │
        ▼
Machine Learning Model
(Risk Prediction Engine)
        │
        ▼
Analytics Aggregation
(Institutional Metrics)
        │
        ▼
Flask Web Application
        │
        ▼
Interactive Dashboard
        │
        ▼
Academic Decision Support
Architecture Advantages

• Modular system design
• Scalable analytics processing
• Easy integration with institutional systems
• Reproducible educational analytics research
`````
🛠 Technologies Used

Technology	Purpose
Python	Core programming language
Pandas	Data analysis and manipulation
NumPy	Numerical computations
Scikit-Learn	Machine learning implementation
Flask	Web application framework
HTML	Dashboard structure
CSS	Dashboard styling
````
📂 Project Structure
A-Data-Driven-Framework-for-Student-Retention-and-Academic-Risk-Analytics
│
├── dataset/
│   └── student_dataset.csv
│
├── model/
│   ├── train_model.py
│   ├── model.pkl
│   └── scaler.pkl
│
├── templates/
│   └── dashboard.html
│
├── static/
│   └── css/
│       └── style.css
│
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
`````
⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/yourusername/A-Data-Driven-Framework-for-Student-Retention-and-Academic-Risk-Analytics.git
2️⃣ Navigate to the Project Directory
cd A-Data-Driven-Framework-for-Student-Retention-and-Academic-Risk-Analytics
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py
5️⃣ Open the Dashboard
http://127.0.0.1:5000

📷 Output Screenshots

🔹 Institutional Overview Dashboard

<img width="1366" height="768" alt="Screenshot (109)" src="https://github.com/user-attachments/assets/3ec0a72e-6fbe-4d26-b163-aab99ee88ee0" />

🔹 Risk Distribution & Attendance Trend

<img width="1366" height="768" alt="Screenshot (110)" src="https://github.com/user-attachments/assets/19618c77-07d4-4bc4-9f82-67c95d065133" />

🔹 Student Risk Overview Table

<img width="1366" height="768" alt="Screenshot (111)" src="https://github.com/user-attachments/assets/1fe4bcea-eca7-4466-a4c9-f3312a12d718" />

These visualizations demonstrate how institutions can quickly identify risk patterns and engagement trends.


🏆 Hackathon Recognition

This project was presented and demonstrated during HACKELITE’2026, a 24-hour hackathon organized by the Developer Network Space (DNS), Department of Computer Science and Engineering at SRM Institute of Science and Technology, Vadapalani Campus in Chennai.

The hackathon involved multiple elimination rounds where participants developed innovative solutions within a strict 24-hour development cycle.

During the hackathon, this framework focused on:

Designing a data-driven student retention analytics system

Developing risk classification logic for academic performance analysis

Creating interactive dashboards for institutional insights

Demonstrating a scalable decision-support system for education analytics

The project advanced through competitive rounds, and I was honored to receive the Certificate of Merit as a Finalist.

Skills Demonstrated

Rapid prototyping

Data analytics pipeline design

Dashboard development

System architecture planning

Collaborative problem solving under pressure

Hackathons like HackElite encourage innovation, technical execution, and real-world problem solving in compressed development environments.

🔗 LinkedIn Post

The hackathon recognition and certificate can be viewed here:

https://www.linkedin.com/posts/m-v-karthikeya-b26a2131b_hackelite2026-hackathon-innovation-activity-7428108728744284160-mRH3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFEhlw4BT-6V0rnLIZSzBIoK7YvV2QlbHLc


🚀 Future Enhancements

Potential extensions of the system include:

• Explainable AI for risk prediction
• Personalized intervention recommendations
• Semester-wise performance forecasting
• Real-time academic monitoring systems
• Integration with institutional databases

📚 Keywords

Educational Data Mining • Learning Analytics • Student Retention Analytics • Academic Risk Prediction • Educational AI

📜 License

This project is released under the MIT License and is intended for academic, research, and educational use.

👨‍💻 Author

M V Karthikeya

⭐ If you find this project useful, consider starring the repository.
