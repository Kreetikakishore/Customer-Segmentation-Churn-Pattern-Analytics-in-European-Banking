# 🏦 European Banking Churn Segmentation Dashboard

> A customer retention intelligence case study designed to identify high-risk churn segments, quantify financial exposure, and generate targeted retention recommendations across a European retail banking portfolio.

---

## 📌 Executive Summary

Customer churn remains one of the most expensive hidden losses for retail banks, directly impacting deposits, product profitability, and long-term customer lifetime value.

This project analyzes **10,000 European banking customers** across France, Germany, and Spain to uncover:

- where churn risk is geographically concentrated,
- which customer demographics are most vulnerable,
- how inactivity and product overload influence exits,
- and how much customer balance is financially exposed.

Using Python, Pandas, Plotly, and Streamlit, the final outcome is an interactive **churn segmentation dashboard** built to support retention-focused decision making.

---

## 🎯 Business Questions Addressed

This project was developed to answer the following strategic banking questions:

- Which geography shows the highest customer attrition risk?
- Which age bands are most likely to leave the bank?
- Are premium high-balance customers churning disproportionately?
- Does inactive membership strongly correlate with exits?
- Is product over-selling contributing to churn?
- Which demographic combinations require urgent retention intervention?
- How much total customer balance is at risk due to churn?

---

## 📊 Core KPI Snapshot

| KPI Metric | Value |
|------------|-------|
| Total Customers Analyzed | 10,000 |
| Overall Churn Rate | 20.37% |
| Highest Risk Geography | Germany |
| Highest Risk Age Group | 46–60 Years |
| High Value Customer Churn | 25.23% |
| Estimated Balance at Risk | €159.4 Million |
| Inactive vs Active Churn Gap | 12.58% |

---

## 🧠 Key Analytical Findings

### 1. Germany Emerges as the Highest Churn Geography
Germany records the highest attrition rate among all three countries, indicating concentrated retention weakness within this customer market.

### 2. Mid-to-Senior Customers Are Most Vulnerable
Customers aged **46–60 show the highest churn propensity**, signaling dissatisfaction among financially mature account holders.

### 3. Product Overload Is Linked to Customer Exit
Customers holding **3 to 4 banking products exhibit extreme churn percentages**, suggesting that aggressive cross-selling may be increasing account fatigue rather than loyalty.

### 4. Inactive Members Show Significantly Higher Churn
Inactive customers churn at nearly **1.9× the rate of active members**, confirming engagement inactivity as a major warning indicator.

### 5. High Balance Accounts Represent Significant Financial Exposure
More than **€159 million in deposits are attached to churn-prone customers**, making retention not just a customer issue but a direct balance sheet concern.

---

## 📈 Strategic Retention Recommendations

Based on the observed churn patterns, the following banking actions are recommended:

- **Launch dedicated retention campaigns in Germany**, where attrition concentration is highest.
- **Introduce re-engagement programs for inactive account holders** before silent churn occurs.
- **Re-evaluate cross-sell strategies for customers with multiple products** to reduce service fatigue.
- **Prioritize premium high-balance customer outreach**, as they represent the largest financial exposure.
- **Design age-personalized loyalty interventions for the 46–60 customer band.**

---

## 🖼️ Dashboard Preview

<img width="1424" height="752" alt="Screenshot 2026-05-02 080825" src="https://github.com/user-attachments/assets/57759c8f-97d8-4fe0-9a75-4f36f1ca162b" />

<img width="1379" height="791" alt="Screenshot 2026-05-02 080833" src="https://github.com/user-attachments/assets/c81e9d07-c84d-4cd6-9831-cb24ebd386f2" />

<img width="289" height="941" alt="Screenshot 2026-05-02 080945" src="https://github.com/user-attachments/assets/640371de-213a-4b32-b607-5990cdd79b73" />

---

## 🗂️ Dataset Scope

The analysis was performed on a structured European banking customer dataset containing demographic, financial, and engagement attributes.

| Variable | Description |
|----------|-------------|
| CreditScore | Customer creditworthiness |
| Geography | France / Germany / Spain |
| Gender | Male / Female |
| Age | Customer age |
| Tenure | Years with bank |
| Balance | Account deposit balance |
| NumOfProducts | Number of banking products |
| HasCrCard | Credit card ownership |
| IsActiveMember | Activity status |
| EstimatedSalary | Annual salary |
| Exited | Churn target flag |

---

## 📊 Customer Segmentation Layers

To move beyond simple churn percentage analysis, customers were segmented into strategic risk cohorts:

| Segment | Groups |
|---------|--------|
| Age Band | Under 30 / 30–45 / 46–60 / 60+ |
| Credit Band | Low / Medium / High |
| Tenure Group | New / Mid / Long-Term |
| Balance Segment | Zero / Low / High Value |

This segmentation enabled deeper identification of churn-prone profiles rather than generic averages.

---

## 🧰 Technology Stack

| Tool | Role |
|------|------|
| Python | Core analytics programming |
| Pandas | Data cleaning & KPI generation |
| NumPy | Numerical computations |
| Plotly | Interactive visual analytics |
| Matplotlib / Seaborn | Exploratory chart generation |
| Streamlit | Executive dashboard deployment |

---

## 🖥️ Dashboard Modules

The Streamlit dashboard includes:

- Executive KPI Cards
- Geography-wise Churn Monitoring
- Age & Tenure Risk Comparison
- High Value Customer Exposure
- Product Saturation Analysis
- Engagement vs Churn Correlation
- Churn Heatmaps
- Raw Customer Data Explorer

---

## 📁 Repository Structure

```bash
banking-churn-segmentation-dashboard/
│
├── data/
│   ├── European_Bank.csv
│   ├── European_Bank_Cleaned.csv
│   └── KPI_Summary.csv
│
├── charts/
│   └── static_visualizations/
│
├── notebooks/
├── analysis.py
├── charts.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Dashboard

### 1. Clone Repository

```bash
git clone https://github.com/your-username/banking-churn-segmentation-dashboard.git
cd banking-churn-segmentation-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch Streamlit App

```bash
python -m streamlit run app.py
```

### 4. Open Browser

```bash
http://localhost:8501
```

---

## 📌 Deliverables Produced

- Cleaned and segmented banking dataset
- KPI summary file
- Static exploratory visualizations
- Interactive retention dashboard
- Strategic churn reduction recommendations

---

## ⚠️ Note

This project was developed as a customer analytics portfolio case study to demonstrate churn intelligence, financial exposure analysis, and retention strategy generation in the retail banking domain.

---

## 👤 Author

**Kreetika Kishore**  
Data Analytics Portfolio Project | 2026
