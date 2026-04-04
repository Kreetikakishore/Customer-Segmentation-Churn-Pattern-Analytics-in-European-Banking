# 🏦 Customer Segmentation & Churn Pattern Analytics in European Banking

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green) ![Plotly](https://img.shields.io/badge/Plotly-Visualizations-orange)

## 📋 Project Overview

This project provides a segmentation-driven analysis of customer churn across three European countries — **France**, **Germany**, and **Spain**. Built for the **European Central Bank**, it uncovers churn patterns across geography, demographics, and financial profiles to help decision-makers design targeted retention strategies.

---

## 🎯 Key Findings

| Metric | Value |
|---|---|
| Overall Churn Rate | 20.37% |
| Highest Risk Country | Germany (32.44%) |
| Highest Risk Age Group | 46–60 years (51.12%) |
| High Value Customer Churn | 25.23% |
| Balance at Risk | €159,489,691 |
| Engagement Gap | 12.58% (Inactive vs Active) |

---

## 📁 Project Structure

```
bank_churn_project/
├── data/
│   ├── European_Bank.csv             # Original dataset
│   ├── European_Bank_Cleaned.csv     # Cleaned & segmented dataset
│   └── KPI_Summary.csv               # All KPIs saved
├── charts/
│   ├── 01_overall_churn.png
│   ├── 02_churn_by_geography.png
│   ├── 03_churn_by_gender.png
│   ├── 04_churn_by_age.png
│   ├── 05_churn_by_products.png
│   ├── 06_churn_by_balance.png
│   ├── 07_churn_by_active.png
│   ├── 08_heatmap_geo_age.png
│   ├── 09_heatmap_geo_gender.png
│   ├── 10_profile_comparison.png
│   ├── 11_churn_by_tenure.png
│   └── 12_churn_by_credit.png
├── notebooks/
├── analysis.py                       # EDA & KPI calculations
├── charts.py                         # Static chart generation
├── app.py                            # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## 🗂️ Dataset Description

| Column | Description |
|---|---|
| CreditScore | Customer creditworthiness |
| Geography | France, Spain, Germany |
| Gender | Male / Female |
| Age | Customer age |
| Tenure | Years with the bank |
| Balance | Account balance |
| NumOfProducts | Number of bank products |
| HasCrCard | Credit card ownership (0/1) |
| IsActiveMember | Activity indicator (0/1) |
| EstimatedSalary | Estimated annual salary |
| Exited | Churn indicator — target variable (0/1) |

---

## 📊 Customer Segments Created

| Segment | Groups |
|---|---|
| Age Group | Under 30, 30–45, 46–60, 60+ |
| Credit Band | Low, Medium, High |
| Tenure Group | New (0–2 yrs), Mid (3–6 yrs), Long (7+ yrs) |
| Balance Segment | Zero Balance, Low Balance, High Balance |

---

## 📈 KPIs Tracked

- **Overall Churn Rate** — % of customers who exited
- **Segment Churn Rate** — Churn % by each segment
- **High Value Churn Ratio** — Churn among premium customers
- **Geographic Risk Index** — Regional churn exposure vs average
- **Engagement Drop Indicator** — Inactivity vs churn correlation

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/bank-churn-project.git
cd bank-churn-project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analysis
```bash
python analysis.py
```

### 4. Generate charts
```bash
python charts.py
```

### 5. Launch the dashboard
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🖥️ Dashboard Features

| Module | Description |
|---|---|
| KPI Summary Cards | Live metric cards updating with filters |
| Geography-wise Churn | Bar charts and stacked charts by country |
| Age & Tenure Comparison | Side-by-side churn analysis |
| High Value Explorer | Premium customer churn with balance at risk |
| Segment Deep Dive | Gender, products, balance, active membership |
| Churn Heatmaps | Geography × Age and Geography × Gender |
| Raw Data Explorer | Filterable table of all 10,000 customers |

### Sidebar Filters
- Country (France / Germany / Spain)
- Gender (Male / Female)
- Age Group (Under 30 / 30–45 / 46–60 / 60+)
- Balance Segment (Zero / Low / High)

---

## 🔍 Key Insights

1. **Germany is the highest risk country** with a 32.44% churn rate — nearly double France and Spain
2. **Age group 46–60 is critically at risk** with over 51% churn rate
3. **Customers with 3–4 products churn at 83–100%** suggesting over-selling is a major problem
4. **Inactive members churn at 1.9× the rate** of active members
5. **High balance customers churn more** — €159M in balance is at risk
6. **German women have the highest combined churn** at 37.55%

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical calculations |
| Matplotlib | Static chart generation |
| Seaborn | Statistical visualizations |
| Plotly | Interactive dashboard charts |
| Streamlit | Web dashboard framework |

---

## 📄 Deliverables

- ✅ Cleaned and segmented dataset
- ✅ 12 static visualizations
- ✅ KPI summary CSV
- ✅ Interactive Streamlit dashboard
- ✅ Research paper with insights and recommendations

---

## 👤 Author

**Kreetika**
European Central Bank — Customer Segmentation & Churn Analytics Project
2026
