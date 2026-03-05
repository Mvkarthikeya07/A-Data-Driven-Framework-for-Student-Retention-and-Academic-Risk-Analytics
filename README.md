🎓 A Data-Driven Framework for Student Retention and Academic Risk Analytics

📌 Overview

Educational institutions face increasing challenges related to student dropouts, academic underperformance, and lack of early intervention mechanisms. Traditional approaches rely heavily on manual judgment and fragmented data, making it difficult to identify at-risk students at scale.

This project presents a data-driven academic intelligence framework that analyzes large-scale institutional student data to assess student retention levels and academic risk patterns.
Rather than focusing on individual predictions, the system provides institution-level insights that support data-informed academic decision-making.

🎯 Objectives

The primary objectives of this project are:

To analyze large-scale student data using academic indicators

To identify academic risk levels (Low / Medium / High) across a student population

To compute student retention metrics at the institutional level

To visualize attendance trends and risk distributions

To support early academic intervention and policy decisions

🧠 Core Concept

This project is designed as a Decision Support System (DSS) for educational institutions.

It does not predict outcomes for a single student.
It analyzes patterns across groups of students (class, batch, or institution).

Key Insight:

Academic success and dropout risk are multi-dimensional, influenced by attendance, academic performance, and behavioral factors.

📊 Dataset Description

A synthetic dataset of 10,000 students is used to ensure:

Privacy preservation

Scalability testing

Realistic academic behavior simulation

Dataset Features:

Attendance (%)

Internal Marks

Behavior Score (1–9)

Study Hours

Final Academic Outcome

Derived Academic Risk Level

Synthetic data enables ethical experimentation without exposing real student records.

⚙️ Risk Classification Logic

Academic risk is determined using transparent, rule-based logic:

🔴 High Risk

Attendance < 60

OR Marks < 45

OR Behavior ≤ 2

🟠 Medium Risk

Attendance between 60–74

OR Marks between 45–59

🟢 Low Risk

Attendance ≥ 75

Marks ≥ 60

Behavior ≥ 3

This approach ensures interpretability, aligning with responsible AI principles.

📈 System Architecture

Pipeline Flow:

Student Data → Risk Classification → Aggregation → Analytics → Dashboard Visualization


The framework is modular and extensible, enabling future integration of:

Explainable ML models

Intervention recommendations

Academic policy simulations

🖥️ Dashboard Features

📌 Key Performance Indicators (KPIs)

Total number of students

Student retention rate

High-risk student count

Average institutional attendance

📊 Visual Analytics

Risk distribution (Low / Medium / High)

Month-wise average attendance trends

Sample student risk overview table

📷 Output Screenshots

🔹 Institutional Overview Dashboard

<img width="1366" height="768" alt="Screenshot (109)" src="https://github.com/user-attachments/assets/3ec0a72e-6fbe-4d26-b163-aab99ee88ee0" />

🔹 Risk Distribution & Attendance Trend

<img width="1366" height="768" alt="Screenshot (110)" src="https://github.com/user-attachments/assets/19618c77-07d4-4bc4-9f82-67c95d065133" />

🔹 Student Risk Overview Table

<img width="1366" height="768" alt="Screenshot (111)" src="https://github.com/user-attachments/assets/1fe4bcea-eca7-4466-a4c9-f3312a12d718" />

These visualizations demonstrate how institutions can quickly identify risk patterns and engagement trends.

📅 Attendance Trend Interpretation

The month-wise attendance graph represents aggregated engagement trends across an academic cycle.
Months are used as analytical time segments, enabling institutions to identify:

Declining engagement periods

Seasonal attendance variations

Correlation between attendance and academic risk

🎓 Why Student Retention Matters

Student retention refers to the institution’s ability to ensure that students:

Remain enrolled

Progress academically

Do not drop out prematurely

Low retention rates often indicate:

Academic stress

Poor engagement

Lack of early support mechanisms

This framework enables early identification of such issues.

🌍 Academic & Social Impact

Supports dropout prevention

Encourages data-driven academic planning

Improves student success outcomes

Aligns with educational analytics research

Promotes ethical use of data

🎯 Relevance to Higher Education

This project aligns strongly with research areas valued by German public universities and DAAD, including:

Educational Data Mining

Learning Analytics

Decision Support Systems

Applied Data Science

Responsible AI in Education

The focus on institution-level analytics, transparency, and societal impact makes it academically robust and internationally relevant.

🛠️ Technologies Used

Python

Pandas & NumPy

Flask

Chart.js

HTML, CSS

Synthetic Data Generation

🚀 Future Enhancements

Explainable AI (risk reason attribution)

Student-level drill-down views

Risk-based academic recommendations

Semester-wise analytics

PDF academic report export

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

✅ Conclusion

This project demonstrates how data analytics frameworks can be effectively applied to address real-world educational challenges.
By shifting the focus from individual predictions to institution-level insights, the system provides a scalable and ethical approach to improving student retention and academic outcomes.

📜 License

This project is released under the MIT License and is intended strictly for academic and educational purposes.
