# ============================================================
# 02_sql_loader.py
# Customer Churn Analysis — Load Data into MySQL
# SQLAlchemy 2.0 Compatible Version
# ============================================================

import pandas as pd
from sqlalchemy import create_engine, text

# ── Your MySQL Credentials ────────────────────────────────
HOST     = "localhost"
PORT     = 3306
USER     = "root"
PASSWORD = "Sahana@22"
DATABASE = "churn_analysis"

# ── Create Connection ─────────────────────────────────────

engine = create_engine(
    f"mysql+pymysql://root:Sahana%4022@localhost:3306/churn_analysis",
    echo=False
)

print("Connecting to MySQL...")

# ── Test Connection ───────────────────────────────────────
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(" Connected to MySQL successfully!")

# ── Load Cleaned CSV ──────────────────────────────────────
df = pd.read_csv(r"C:\Users\ShwetaPHadimani\OneDrive\Documents\Churn_Analysis\churn_cleaned.csv")
print(f"Loaded {len(df):,} rows from CSV")
print(f"   Columns: {list(df.columns)}")

# ── Push Data to MySQL ────────────────────────────────────
print("\nUploading to MySQL... please wait...")

df.to_sql(
    name="churn",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=500
)

print(" Table churn created in MySQL!")

# ── Verify ────────────────────────────────────────────────
with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT
            COUNT(*)                        AS Total_Customers,
            SUM(Churn_Flag)                 AS Total_Churned,
            ROUND(AVG(Churn_Flag)*100, 2)   AS Churn_Rate_Pct
        FROM churn
    """))
    rows = result.fetchall()
    print("\n=== DATABASE VERIFICATION ===")
    for row in rows:
        print(f"Total Customers : {row[0]}")
        print(f"Total Churned   : {row[1]}")
        print(f"Churn Rate      : {row[2]}%")

print("\n MySQL ready for SQL queries!")