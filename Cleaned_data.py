

import pandas as pd
import numpy as np

# ── Load ──────────────────────────────────────────
df = pd.read_csv("C:\\Users\\ShwetaPHadimani\\OneDrive\\Documents\\Churn_Analysis\\data\\churn_data.csv")

print("Shape:", df.shape)
print("\nColumn Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# ── Fix TotalCharges (spaces → NaN → fill median) ─
df['TotalCharges'] = pd.to_numeric(
    df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(
    df['TotalCharges'].median(), inplace=True)

# ── Drop CustomerID for analysis ──────────────────
# (keep it only for reference)

# ── Churn as number (for calculations) ────────────
df['Churn_Flag'] = df['Churn'].map({'Yes': 1, 'No': 0})

# ── New Columns (Feature Engineering) ────────────

# Tenure Groups
df['Tenure_Group'] = pd.cut(
    df['tenure'],
    bins=[0, 12, 24, 48, 72],
    labels=['New (0-1yr)', 'Growing (1-2yr)',
            'Mature (2-4yr)', 'Loyal (4+yr)'])

# Monthly Charge Segments
df['Charge_Segment'] = pd.cut(
    df['MonthlyCharges'],
    bins=[0, 35, 65, 100],
    labels=['Low (<$35)', 'Medium ($35-$65)', 'High (>$65)'])

# Revenue at Risk (monthly revenue from churned customers)
df['Revenue_At_Risk'] = (
    df['Churn_Flag'] * df['MonthlyCharges'])

# Customer Value Score
df['Customer_Value'] = (
    df['tenure'] * df['MonthlyCharges'])

# Save cleaned file
df.to_csv("churn_cleaned.csv", index=False)
print("\n Cleaned file saved!")
print("Final Shape:", df.shape)

#database connection

import pandas as pd
from sqlalchemy import create_engine

# ── Step 1: Your MySQL Credentials ───────────────────────
HOST     = "localhost"       # Usually localhost
PORT     = 3306              # Default MySQL port
USER     = "root"            # Your MySQL username
PASSWORD = "Sahana@22"   # Your MySQL password
DATABASE = "CHURN_ANALYSIS"  # Database you created

# ── Step 2: Create Connection ─────────────────────────────
engine = create_engine(
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

print("Connecting to MySQL...")

# ── Step 3: Load Cleaned CSV ──────────────────────────────
df = pd.read_csv("C:\\Users\\ShwetaPHadimani\\OneDrive\\Documents\\Churn_Analysis\\Cleaned_data.py")
print(f"Loaded {len(df):,} rows from CSV")

# ── Step 4: Push Data to MySQL Table ─────────────────────
df.to_sql(
    name="churn",           # Table name in MySQL
    con=engine,
    if_exists="replace",    # Replace table if already exists
    index=False,
    chunksize=500           # Upload 500 rows at a time
)

print(" Table 'churn' created in MySQL!")

# ── Step 5: Verify with Quick Query ───────────────────────
result = pd.read_sql("""
    SELECT
        COUNT(*)                        AS Total_Customers,
        SUM(Churn_Flag)                 AS Total_Churned,
        ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct
    FROM churn
""", con=engine)

print("\n=== DATABASE VERIFICATION ===")
print(result.to_string(index=False))
print("\n MySQL ready for SQL queries!")


