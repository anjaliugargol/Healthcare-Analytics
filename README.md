# Healthcare Analytics: Predicting Emergency Room Overcrowding

## 📌 Project Objective

Analyze hospital emergency room (ER) admission trends to predict overcrowding and recommend strategies to manage patient flow efficiently.

---

## 🏥 Problem Statement

Hospitals frequently face ER overcrowding due to high patient inflow, limited doctor availability, and equipment constraints.  
This project aims to analyze operational data and build a predictive model to identify overcrowding scenarios.

---

## 📊 Dataset Description

The dataset includes:

- Visit_ID
- Hospital_Name
- Arrival_Time
- Day
- Hour
- Season
- Waiting_Time_Min
- Doctor_Available
- Patients_In_ER
- Equipment_Usage_%
- Overcrowded (Target Variable)
- Disposition

Total Records: ~8000+

---

## 🛠 Tools & Technologies Used

- Python (Pandas, NumPy)
- Matplotlib & Seaborn
- Scikit-learn
- MySQL
- Power BI

---

## 🔎 Step 1: Data Cleaning

- Handled missing Visit_ID values
- Verified null values
- Exported cleaned dataset

---

## 📈 Step 2: Exploratory Data Analysis

Performed:

- Distribution analysis of waiting time
- Overcrowding frequency analysis
- Correlation heatmap
- Hour vs Day patient load heatmap
- Doctor availability vs patient inflow study

---

## 🤖 Step 3: Predictive Modeling

### Logistic Regression

Target Variable:
Overcrowded (0 = No, 1 = Yes)

Evaluation Metrics:
- Accuracy
- Confusion Matrix
- Classification Report
- ROC Curve

Objective:
Predict ER overcrowding based on operational factors.

---

## 🗄 Step 4: Database Integration

- Designed MySQL database schema
- Inserted cleaned dataset into database
- Enabled SQL-based peak hour analysis

---

## 📊 Step 5: Power BI Dashboard

Created interactive dashboard including:

- ER patient volume trends
- Capacity utilization graphs
- Overcrowding heatmaps
- Forecast trends

Dashboard File:
Located in `/dashboard/ER_Hospital.pbix`

---

## 📌 Key Insights

- Overcrowding peaks during high patient inflow hours.
- Doctor availability significantly impacts waiting time.
- Equipment usage percentage strongly correlates with ER congestion.
- Seasonal patterns influence overcrowding frequency.

---

## 🚀 Future Enhancements

- Time-series forecasting
- Real-time dashboard integration
- Model deployment as API

---

## 📂 Project Structure

Healthcare-Analytics/
│
├── data/
├── notebooks/
├── database/
├── dashboard/
├── requirements.txt
└── README.md

---

## ▶ How to Run the Project

1. Clone the repository
2. Install required libraries:
   pip install -r requirements.txt
3. Open notebooks/ER_Analysis.ipynb
4. Run all cells
