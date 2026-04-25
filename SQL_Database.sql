CREATE DATABASE Churn_Analysis;

ALTER USER 'root'@'localhost' 
IDENTIFIED WITH mysql_native_password 
BY 'Sahana@22';

FLUSH PRIVILEGES;

show tables;

-- =============================================
-- CUSTOMER CHURN ANALYSIS — ALL SQL QUERIES
-- =============================================

USE churn_analysis;

-- ── Q1: OVERALL CHURN KPIs ───────────────────
SELECT
  COUNT(*)                        AS Total_Customers,
  SUM(Churn_Flag)                 AS Total_Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct,
  ROUND(SUM(MonthlyCharges), 2)   AS Total_Monthly_Revenue,
  ROUND(SUM(Revenue_At_Risk), 2)  AS Revenue_At_Risk
FROM churn;

-- ── Q2: CHURN BY CONTRACT TYPE ───────────────
SELECT
  Contract,
  COUNT(*)                        AS Total_Customers,
  SUM(Churn_Flag)                 AS Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct
FROM churn
GROUP BY Contract
ORDER BY Churn_Rate_Pct DESC;

-- ── Q3: CHURN BY TENURE GROUP ────────────────
SELECT
  Tenure_Group,
  COUNT(*)                        AS Customers,
  SUM(Churn_Flag)                 AS Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct
FROM churn
GROUP BY Tenure_Group
ORDER BY Churn_Rate_Pct DESC;

-- ── Q4: CHURN BY INTERNET SERVICE ────────────
SELECT
  InternetService,
  COUNT(*)                        AS Customers,
  SUM(Churn_Flag)                 AS Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct,
  ROUND(SUM(Revenue_At_Risk), 2)  AS Revenue_Lost
FROM churn
GROUP BY InternetService
ORDER BY Revenue_Lost DESC;

-- ── Q5: CHURN BY PAYMENT METHOD ──────────────
SELECT
  PaymentMethod,
  COUNT(*)                        AS Customers,
  SUM(Churn_Flag)                 AS Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct
FROM churn
GROUP BY PaymentMethod
ORDER BY Churn_Rate_Pct DESC;

-- ── Q6: CHURN BY CHARGE SEGMENT ──────────────
SELECT
  Charge_Segment,
  COUNT(*)                        AS Customers,
  SUM(Churn_Flag)                 AS Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct
FROM churn
GROUP BY Charge_Segment
ORDER BY Churn_Rate_Pct DESC;

-- ── Q7: SENIOR CITIZEN ANALYSIS ──────────────
SELECT
  CASE WHEN SeniorCitizen = 1
    THEN 'Senior' ELSE 'Non-Senior'
  END                             AS Customer_Type,
  COUNT(*)                        AS Customers,
  SUM(Churn_Flag)                 AS Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct,
  ROUND(AVG(MonthlyCharges), 2)   AS Avg_Monthly_Charges
FROM churn
GROUP BY SeniorCitizen;

-- ── Q8: HIGH RISK CUSTOMERS ──────────────────
SELECT
  customerID,
  tenure,
  MonthlyCharges,
  TotalCharges,
  Contract,
  InternetService,
  PaymentMethod
FROM churn
WHERE Churn_Flag = 1
  AND MonthlyCharges > 65
  AND Contract = 'Month-to-month'
  AND tenure < 12
ORDER BY MonthlyCharges DESC
LIMIT 20;

-- ── Q9: CHURNED VS RETAINED PROFILE ──────────
SELECT
  Churn,
  ROUND(AVG(tenure), 1)           AS Avg_Tenure_Months,
  ROUND(AVG(MonthlyCharges), 2)   AS Avg_Monthly_Charges,
  ROUND(AVG(TotalCharges), 2)     AS Avg_Total_Spend
FROM churn
GROUP BY Churn;

-- ── Q10: CHURN BY GENDER ─────────────────────
SELECT
  gender,
  COUNT(*)                        AS Customers,
  SUM(Churn_Flag)                 AS Churned,
  ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct
FROM churn
GROUP BY gender;
