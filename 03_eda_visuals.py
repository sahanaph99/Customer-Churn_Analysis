# ============================================================
# 03_eda_visuals.py
# Customer Churn Analysis — EDA & Visualisations
# ============================================================

import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Setup ─────────────────────────────────────────────────
df = pd.read_csv(r"C:\Users\ShwetaPHadimani\OneDrive\Documents\Churn_Analysis\churn_cleaned.csv")
os.makedirs('charts', exist_ok=True)

sns.set_theme(style='whitegrid')
plt.rcParams['figure.dpi'] = 150
print("Data loaded!", df.shape)

# ── Chart 1: Churn Distribution ───────────────────────────
fig, ax = plt.subplots(figsize=(7, 7))
df['Churn'].value_counts().plot(
    kind='pie', autopct='%1.1f%%',
    colors=['#E53935', '#2E7D32'],
    explode=[0.05, 0],
    wedgeprops=dict(width=0.55), ax=ax)
ax.set_title('Customer Churn Distribution',
             fontsize=16, fontweight='bold')
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('charts/01_churn_distribution.png')
plt.close()
print("Chart 1 saved!")

# ── Chart 2: Churn by Contract ────────────────────────────
contract = (df.groupby('Contract')['Churn_Flag']
              .mean() * 100).sort_values()
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(contract.index, contract.values,
               color=['#2E7D32', '#1565C0', '#E53935'],
               edgecolor='white', height=0.55)
for bar, val in zip(bars, contract.values):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2,
            f'{val:.1f}%', va='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Contract Type',
             fontsize=16, fontweight='bold')
ax.set_xlabel('Churn Rate (%)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/02_churn_by_contract.png')
plt.close()
print("Chart 2 saved!")

# ── Chart 3: Churn by Tenure Group ───────────────────────
tenure = (df.groupby('Tenure_Group', observed=True)
            ['Churn_Flag'].mean() * 100)
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(range(len(tenure)), tenure.values,
              color=['#E53935', '#F57F17',
                     '#1565C0', '#2E7D32'],
              edgecolor='white', width=0.6)
ax.set_xticks(range(len(tenure)))
ax.set_xticklabels(tenure.index, fontsize=11)
for bar, val in zip(bars, tenure.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.5,
            f'{val:.1f}%', ha='center',
            fontsize=11, fontweight='bold')
ax.set_title('Churn Rate by Tenure Group',
             fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/03_churn_by_tenure.png')
plt.close()
print("Chart 3 saved!")

# ── Chart 4: Monthly Charges ──────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
df[df['Churn']=='No']['MonthlyCharges'].hist(
    bins=30, alpha=0.7, color='#2E7D32',
    label='Retained', ax=ax)
df[df['Churn']=='Yes']['MonthlyCharges'].hist(
    bins=30, alpha=0.7, color='#E53935',
    label='Churned', ax=ax)
ax.set_title('Monthly Charges: Churned vs Retained',
             fontsize=16, fontweight='bold')
ax.set_xlabel('Monthly Charges ($)')
ax.set_ylabel('Number of Customers')
ax.legend(fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/04_monthly_charges.png')
plt.close()
print(" Chart 4 saved!")

# ── Chart 5: Churn by Internet Service ───────────────────
internet = (df.groupby('InternetService')['Churn_Flag']
              .mean() * 100).sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(internet.index, internet.values,
              color=['#E53935', '#1565C0', '#2E7D32'],
              edgecolor='white', width=0.5)
for bar, val in zip(bars, internet.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.5,
            f'{val:.1f}%', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Internet Service',
             fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/05_churn_by_internet.png')
plt.close()
print(" Chart 5 saved!")

# ── Chart 6: Heatmap ──────────────────────────────────────
pivot = df.pivot_table(
    values='Churn_Flag',
    index='Tenure_Group',
    columns='Contract',
    aggfunc='mean',
    observed=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(pivot, annot=True, fmt='.0%',
            cmap='Reds', ax=ax,
            linewidths=0.5, linecolor='white')
ax.set_title('Churn Rate: Tenure Group vs Contract Type',
             fontsize=16, fontweight='bold')
ax.tick_params(axis='x', rotation=0)
ax.tick_params(axis='y', rotation=0)
plt.tight_layout()
plt.savefig('charts/06_heatmap.png')
plt.close()
print(" Chart 6 saved!")

print("\n All 6 charts saved to charts/ folder!")