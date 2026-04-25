# 📊 Customer Churn Analysis
### Data Analyst Portfolio Project

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql)
![PowerBI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![Status](https://img.shields.io/badge/Status-Completed-green?style=for-the-badge)

---

## 📌 Project Overview

End-to-end **Data Analyst** project analyzing customer churn for a telecom company using the **IBM Telco Customer Churn** dataset (7,043 customer records, 21 features).

The goal is to identify **WHO** is churning, **WHY** they are leaving, and which customer segments represent the **highest revenue risk** — enabling the business to take targeted retention action.

---

## 🎯 Business Problem

A telecom company is experiencing high customer churn, resulting in significant monthly revenue loss. The retention team needs data-driven answers to:

- Which customer segments have the highest churn rates?
- What contract, service, and payment factors drive churn?
- How much monthly revenue is at risk from churned customers?
- Which specific customers need urgent retention action?

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.13 | Data cleaning & feature engineering |
| Pandas | Data manipulation & analysis |
| Matplotlib & Seaborn | EDA charts & visualizations |
| MySQL | Database & business SQL queries |
| SQLAlchemy + PyMySQL | Python to MySQL connection |
| Power BI | Interactive 4-page dashboard |

---

## 📂 Project Structure

```
customer-churn-analysis/
├── data/
│   ├── churn_data.csv              # Raw dataset from Kaggle
│   └── churn_cleaned.csv           # Cleaned & engineered dataset
├── charts/
│   ├── 01_churn_distribution.png   # Overall churn donut chart
│   ├── 02_churn_by_contract.png    # Churn by contract type
│   ├── 03_churn_by_tenure.png      # Churn by tenure group
│   ├── 04_monthly_charges.png      # Monthly charges distribution
│   ├── 05_churn_by_internet.png    # Churn by internet service
│   └── 06_heatmap.png              # Tenure vs contract heatmap
├── Cleaned_data.py                 # Phase 1 - Data cleaning script
├── 02_sql_loader.py                # Phase 2 - MySQL data loader
├── 03_eda_visuals.py               # Phase 3 - EDA & charts
├── SQL_Database.sql                # All 10 SQL business queries
├── churn_dashboard.pbix            # Power BI dashboard (4 pages)
├── SQL_Queries_Documentation.docx  # SQL queries documentation
├── Python_Code_Documentation.docx  # Python code documentation
├── Customer_Churn_Analysis.pptx    # Project presentation (11 slides)
└── README.md
```

---

## 🔧 How to Run

### Step 1 — Install Required Libraries
```bash
pip install pandas numpy matplotlib seaborn sqlalchemy pymysql
```

### Step 2 — Download Dataset
Download from Kaggle:
[IBM Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

Place the CSV file in the `data/` folder and rename it to `churn_data.csv`

### Step 3 — Run Data Cleaning
```bash
python Cleaned_data.py
```
Output: `data/churn_cleaned.csv`

### Step 4 — Load into MySQL
Create database in MySQL first:
```sql
CREATE DATABASE churn_analysis;
```
Then run:
```bash
python 02_sql_loader.py
```
Output: `churn` table in MySQL

### Step 5 — Run EDA Charts
```bash
python 03_eda_visuals.py
```
Output: 6 PNG charts in `charts/` folder

### Step 6 — Run SQL Queries
Open `SQL_Database.sql` in MySQL Workbench and run all 10 queries.

### Step 7 — Open Power BI Dashboard
Open `churn_dashboard.pbix` in Power BI Desktop.
Connect to your MySQL database:
- Server: localhost
- Database: churn_analysis

---

## 📈 Key Findings

| # | Finding | Impact |
|---|---------|--------|
| 1 | Month-to-month customers churn at **42.71%** vs 2.83% for 2-year contracts | High |
| 2 | New customers (0-12 months) churn at **47.4%** — highest risk group | High |
| 3 | Fiber optic users churn at **41.89%** despite paying highest charges | High |
| 4 | Electronic check users churn at **45.29%** — 3x credit card auto-pay | Medium |
| 5 | Churned customers pay **$13 MORE** per month than retained customers | Medium |
| 6 | Gender shows no significant difference in churn rate (26.9% vs 26.2%) | Low |

---

## 💡 Business Recommendations

| Priority | Recommendation | Expected Outcome |
|----------|---------------|-----------------|
| 1 | Offer 10-15% discount to upgrade to annual contracts | Reduce churn from 42.7% to 25% |
| 2 | Launch new customer onboarding program for first 12 months | Reduce new customer churn by 15-20% |
| 3 | Audit fiber optic service quality and customer satisfaction | Reduce fiber churn from 41.9% to 30% |
| 4 | Incentivize switch from electronic check to auto-payment | Reduce payment-related churn by 10% |

---

## 📊 SQL Queries Overview

| Query | Business Question |
|-------|------------------|
| Q1 | Overall churn KPIs — rate, revenue at risk |
| Q2 | Churn rate by contract type |
| Q3 | Churn rate by tenure group |
| Q4 | Churn rate and revenue loss by internet service |
| Q5 | Churn rate by payment method |
| Q6 | Churn rate by monthly charge segment |
| Q7 | Senior citizen churn analysis |
| Q8 | Top 20 high-risk customer list |
| Q9 | Churned vs retained customer profile |
| Q10 | Churn by gender |

---

## 📉 Power BI Dashboard Pages

| Page | Content |
|------|---------|
| Page 1 — Home | KPI cards, donut chart, churn by contract & internet |
| Page 2 — Customer Segments | Tenure, payment, charge segment, matrix heatmap |
| Page 3 — Revenue Impact | Revenue at risk cards, revenue by service & contract, high-risk table |
| Page 4 — Business Insights | 6 key findings + 4 business recommendations |

---

## 📊 Dataset Information

| Field | Value |
|-------|-------|
| Source | IBM Watson Analytics / Kaggle |
| Records | 7,043 customers |
| Features | 21 columns |
| Target | Churn (Yes/No) |
| Overall Churn Rate | 26.54% |

---

## 🆕 Engineered Features

| Feature | Description |
|---------|-------------|
| Churn_Flag | Numeric churn (1=Yes, 0=No) |
| Tenure_Group | New / Growing / Mature / Loyal |
| Charge_Segment | Low / Medium / High charges |
| Revenue_At_Risk | MonthlyCharges × Churn_Flag |
| Customer_Value | tenure × MonthlyCharges |

---

## 👩‍💻 About

**Sahana** — Data Analyst | BCA Graduate  
Government First Grade College, Navanagar, Bagalkot  
Internship: BDreamz Global Solutions Pvt. Ltd.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this project helpful, please give it a star!
