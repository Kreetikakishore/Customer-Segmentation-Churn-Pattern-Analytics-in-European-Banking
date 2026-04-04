# =============================================
# PHASE 6 - Visualizations
# =============================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

# ── Load cleaned dataset ──────────────────────
df = pd.read_csv('data/European_Bank_Cleaned.csv')
df['Exited'] = df['Exited'].astype(int)

# ── Create output folder for charts ──────────
os.makedirs('charts', exist_ok=True)

# ── Global style ──────────────────────────────
sns.set_theme(style='whitegrid')
COLORS  = ['#2ecc71', '#e74c3c']
PALETTE = 'RdYlGn_r'

print("Building charts... please wait")

# ─────────────────────────────────────────────
# CHART 1 — Overall Churn Distribution (Pie)
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 7))
sizes   = df['Exited'].value_counts()
labels  = ['Retained (79.63%)', 'Churned (20.37%)']
ax.pie(sizes, labels=labels, colors=COLORS,
       autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 13})
ax.set_title('Overall Churn Distribution', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/01_overall_churn.png', dpi=150)
plt.close()
print("Chart 1 done — Overall Churn Distribution")

# ─────────────────────────────────────────────
# CHART 2 — Churn by Geography (Bar)
# ─────────────────────────────────────────────
geo = df.groupby('Geography')['Exited'].mean() * 100
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(geo.index, geo.values,
              color=['#3498db', '#e74c3c', '#2ecc71'],
              edgecolor='white', width=0.5)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, geo.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.5,
            f'{val:.1f}%', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Geography', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Country', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 45)
plt.tight_layout()
plt.savefig('charts/02_churn_by_geography.png', dpi=150)
plt.close()
print("Chart 2 done — Churn by Geography")

# ─────────────────────────────────────────────
# CHART 3 — Churn by Gender (Bar)
# ─────────────────────────────────────────────
gender = df.groupby('Gender')['Exited'].mean() * 100
fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(gender.index, gender.values,
              color=['#e91e8c', '#3498db'],
              edgecolor='white', width=0.4)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, gender.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.4,
            f'{val:.1f}%', ha='center',
            fontsize=13, fontweight='bold')
ax.set_title('Churn Rate by Gender', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Gender', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 35)
plt.tight_layout()
plt.savefig('charts/03_churn_by_gender.png', dpi=150)
plt.close()
print("Chart 3 done — Churn by Gender")

# ─────────────────────────────────────────────
# CHART 4 — Churn by Age Group (Bar)
# ─────────────────────────────────────────────
age_order = ['Under 30', '30-45', '46-60', '60+']
age = df.groupby('AgeGroup')['Exited'].mean() * 100
age = age.reindex(age_order)
fig, ax = plt.subplots(figsize=(9, 5))
bar_colors = ['#2ecc71', '#f39c12', '#e74c3c', '#e67e22']
bars = ax.bar(age.index, age.values,
              color=bar_colors,
              edgecolor='white', width=0.5)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, age.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.8,
            f'{val:.1f}%', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Age Group', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Age Group', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 65)
plt.tight_layout()
plt.savefig('charts/04_churn_by_age.png', dpi=150)
plt.close()
print("Chart 4 done — Churn by Age Group")

# ─────────────────────────────────────────────
# CHART 5 — Churn by Number of Products (Bar)
# ─────────────────────────────────────────────
prod = df.groupby('NumOfProducts')['Exited'].mean() * 100
fig, ax = plt.subplots(figsize=(8, 5))
bar_colors = ['#f39c12', '#2ecc71', '#e74c3c', '#c0392b']
bars = ax.bar(prod.index.astype(str), prod.values,
              color=bar_colors,
              edgecolor='white', width=0.5)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, prod.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 1,
            f'{val:.1f}%', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Number of Products', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Number of Products', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 115)
plt.tight_layout()
plt.savefig('charts/05_churn_by_products.png', dpi=150)
plt.close()
print("Chart 5 done — Churn by Number of Products")

# ─────────────────────────────────────────────
# CHART 6 — Churn by Balance Segment (Bar)
# ─────────────────────────────────────────────
bal_order = ['Zero Balance', 'Low Balance', 'High Balance']
bal = df.groupby('BalanceSegment')['Exited'].mean() * 100
bal = bal.reindex(bal_order)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(bal.index, bal.values,
              color=['#95a5a6', '#f39c12', '#e74c3c'],
              edgecolor='white', width=0.5)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, bal.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.4,
            f'{val:.1f}%', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Balance Segment', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Balance Segment', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 35)
plt.tight_layout()
plt.savefig('charts/06_churn_by_balance.png', dpi=150)
plt.close()
print("Chart 6 done — Churn by Balance Segment")

# ─────────────────────────────────────────────
# CHART 7 — Churn by Active Membership (Bar)
# ─────────────────────────────────────────────
active = df.groupby('IsActiveMember')['Exited'].mean() * 100
active.index = ['Inactive', 'Active']
fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(active.index, active.values,
              color=['#e74c3c', '#2ecc71'],
              edgecolor='white', width=0.4)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, active.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.4,
            f'{val:.1f}%', ha='center',
            fontsize=13, fontweight='bold')
ax.set_title('Churn Rate by Active Membership', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Membership Status', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 38)
plt.tight_layout()
plt.savefig('charts/07_churn_by_active.png', dpi=150)
plt.close()
print("Chart 7 done — Churn by Active Membership")

# ─────────────────────────────────────────────
# CHART 8 — Heatmap: Geography x Age Group
# ─────────────────────────────────────────────
age_order = ['Under 30', '30-45', '46-60', '60+']
pivot = df.pivot_table(values='Exited',
                        index='Geography',
                        columns='AgeGroup',
                        aggfunc='mean') * 100
pivot = pivot[age_order]
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(pivot, annot=True, fmt='.1f',
            cmap='RdYlGn_r', linewidths=0.5,
            linecolor='white', ax=ax,
            annot_kws={'size': 13, 'weight': 'bold'},
            cbar_kws={'label': 'Churn Rate (%)'})
ax.set_title('Churn Rate Heatmap: Geography x Age Group',
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Age Group', fontsize=12)
ax.set_ylabel('Country', fontsize=12)
plt.tight_layout()
plt.savefig('charts/08_heatmap_geo_age.png', dpi=150)
plt.close()
print("Chart 8 done — Heatmap Geography x Age")

# ─────────────────────────────────────────────
# CHART 9 — Heatmap: Geography x Gender
# ─────────────────────────────────────────────
pivot2 = df.pivot_table(values='Exited',
                         index='Geography',
                         columns='Gender',
                         aggfunc='mean') * 100
fig, ax = plt.subplots(figsize=(7, 4))
sns.heatmap(pivot2, annot=True, fmt='.1f',
            cmap='RdYlGn_r', linewidths=0.5,
            linecolor='white', ax=ax,
            annot_kws={'size': 14, 'weight': 'bold'},
            cbar_kws={'label': 'Churn Rate (%)'})
ax.set_title('Churn Rate Heatmap: Geography x Gender',
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Gender', fontsize=12)
ax.set_ylabel('Country', fontsize=12)
plt.tight_layout()
plt.savefig('charts/09_heatmap_geo_gender.png', dpi=150)
plt.close()
print("Chart 9 done — Heatmap Geography x Gender")

# ─────────────────────────────────────────────
# CHART 10 — Churned vs Retained Profile (Bar)
# ─────────────────────────────────────────────
profile = df.groupby('Exited')[['CreditScore', 'Age',
                                  'Tenure', 'Balance',
                                  'EstimatedSalary']].mean()
profile.index = ['Retained', 'Churned']
profile_norm = profile.div(profile.max())
fig, ax = plt.subplots(figsize=(10, 5))
profile_norm.T.plot(kind='bar', ax=ax,
                     color=['#2ecc71', '#e74c3c'],
                     edgecolor='white', width=0.6)
ax.set_title('Churned vs Retained — Normalised Profile',
             fontsize=16, fontweight='bold')
ax.set_ylabel('Relative Score (0–1)', fontsize=12)
ax.set_xlabel('Feature', fontsize=12)
ax.legend(['Retained', 'Churned'], fontsize=11)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
plt.tight_layout()
plt.savefig('charts/10_profile_comparison.png', dpi=150)
plt.close()
print("Chart 10 done — Churned vs Retained Profile")

# ─────────────────────────────────────────────
# CHART 11 — Tenure Group Churn (Bar)
# ─────────────────────────────────────────────
ten_order = ['New (0-2 yrs)', 'Mid (3-6 yrs)', 'Long (7+ yrs)']
tenure = df.groupby('TenureGroup')['Exited'].mean() * 100
tenure = tenure.reindex(ten_order)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(tenure.index, tenure.values,
              color=['#e74c3c', '#f39c12', '#2ecc71'],
              edgecolor='white', width=0.5)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, tenure.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.3,
            f'{val:.1f}%', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Tenure Group', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Tenure Group', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 30)
plt.tight_layout()
plt.savefig('charts/11_churn_by_tenure.png', dpi=150)
plt.close()
print("Chart 11 done — Churn by Tenure Group")

# ─────────────────────────────────────────────
# CHART 12 — Credit Band Churn (Bar)
# ─────────────────────────────────────────────
cred_order = ['Low', 'Medium', 'High']
credit = df.groupby('CreditBand')['Exited'].mean() * 100
credit = credit.reindex(cred_order)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(credit.index, credit.values,
              color=['#e74c3c', '#f39c12', '#2ecc71'],
              edgecolor='white', width=0.5)
ax.axhline(y=20.37, color='gray', linestyle='--',
           linewidth=1.2, label='Avg Churn 20.37%')
for bar, val in zip(bars, credit.values):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.3,
            f'{val:.1f}%', ha='center',
            fontsize=12, fontweight='bold')
ax.set_title('Churn Rate by Credit Band', fontsize=16, fontweight='bold')
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_xlabel('Credit Band', fontsize=12)
ax.legend(fontsize=11)
ax.set_ylim(0, 30)
plt.tight_layout()
plt.savefig('charts/12_churn_by_credit.png', dpi=150)
plt.close()
print("Chart 12 done — Churn by Credit Band")

print("\n" + "=" * 50)
print("ALL 12 CHARTS SAVED TO charts/ FOLDER")
print("=" * 50)