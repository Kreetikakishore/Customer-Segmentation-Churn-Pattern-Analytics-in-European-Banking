# =============================================
# PHASE 7 - Streamlit Dashboard
# =============================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page Configuration ────────────────────────
st.set_page_config(
    page_title="European Banking Churn Segmentation Dashboard",
    page_icon="🏦",
    layout="wide"
)

# ── Load Data ─────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('data/European_Bank_Cleaned.csv')
    df['Exited'] = df['Exited'].astype(int)
    return df

df = load_data()

# ── Sidebar ───────────────────────────────────
st.sidebar.image("https://img.icons8.com/color/96/bank.png", width=80)
st.sidebar.title("🏦 Bank Churn Analytics")
st.sidebar.markdown("---")
st.sidebar.header("Filters")

selected_geo = st.sidebar.multiselect(
    "Select Country",
    options=df['Geography'].unique(),
    default=df['Geography'].unique()
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

age_order = ['Under 30', '30-45', '46-60', '60+']
selected_age = st.sidebar.multiselect(
    "Select Age Group",
    options=age_order,
    default=age_order
)

bal_order = ['Zero Balance', 'Low Balance', 'High Balance']
selected_bal = st.sidebar.multiselect(
    "Select Balance Segment",
    options=bal_order,
    default=bal_order
)

st.sidebar.markdown("---")
st.sidebar.markdown("**EuroBank Analytics**")
st.sidebar.markdown("Customer Churn Intelligence")

# ── Apply Filters ─────────────────────────────
filtered = df[
    (df['Geography'].isin(selected_geo)) &
    (df['Gender'].isin(selected_gender)) &
    (df['AgeGroup'].isin(selected_age)) &
    (df['BalanceSegment'].isin(selected_bal))
]

# ── Helper ────────────────────────────────────
def churn_rate(series):
    if len(series) == 0:
        return 0
    return round(series.mean() * 100, 2)

# ── Title ─────────────────────────────────────
st.title("🏦 European Banking Churn Segmentation Dashboard")
st.markdown("Segmentation-driven churn analysis across France, Germany and Spain")
st.markdown("---")

# =============================================
# MODULE 1 — KPI Summary Cards
# =============================================
st.header("📊 Overall Churn Summary")

total     = len(filtered)
churned   = filtered['Exited'].sum()
retained  = total - churned
rate      = churn_rate(filtered['Exited'])
hv        = filtered[filtered['Balance'] >= 100000]
hv_rate   = churn_rate(hv['Exited'])
inactive  = filtered[filtered['IsActiveMember'] == 0]
inact_rate= churn_rate(inactive['Exited'])

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Customers", f"{total:,}")
with col2:
    st.metric("Total Churned", f"{churned:,}", delta=f"{rate}%",
              delta_color="inverse")
with col3:
    st.metric("Total Retained", f"{retained:,}")
with col4:
    st.metric("Overall Churn Rate", f"{rate}%")
with col5:
    st.metric("High Value Churn Rate", f"{hv_rate}%",
              delta_color="inverse")

st.markdown("---")

# =============================================
# MODULE 2 — Geography Churn
# =============================================
st.header("🌍 Geography-wise Churn")

col1, col2 = st.columns(2)

with col1:
    geo = filtered.groupby('Geography')['Exited'].mean() * 100
    geo = geo.reset_index()
    geo.columns = ['Country', 'Churn Rate']
    fig = px.bar(
        geo, x='Country', y='Churn Rate',
        color='Churn Rate',
        color_continuous_scale='RdYlGn_r',
        text=geo['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='Churn Rate by Country'
    )
    fig.add_hline(y=20.37, line_dash='dash',
                  line_color='gray',
                  annotation_text='Avg 20.37%')
    fig.update_traces(textposition='outside')
    fig.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    geo2 = filtered.groupby('Geography')['Exited'].agg(['sum', 'count'])
    geo2.columns = ['Churned', 'Total']
    geo2['Retained'] = geo2['Total'] - geo2['Churned']
    geo2 = geo2.reset_index()
    fig2 = px.bar(
        geo2, x='Geography',
        y=['Retained', 'Churned'],
        title='Churned vs Retained by Country',
        color_discrete_map={
            'Retained': '#2ecc71',
            'Churned' : '#e74c3c'
        },
        barmode='stack'
    )
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 3 — Age & Tenure Churn
# =============================================
st.header("👥 Age & Tenure Churn Comparison")

col1, col2 = st.columns(2)

with col1:
    age_order = ['Under 30', '30-45', '46-60', '60+']
    age = filtered.groupby('AgeGroup')['Exited'].mean() * 100
    age = age.reindex(age_order).reset_index()
    age.columns = ['Age Group', 'Churn Rate']
    fig3 = px.bar(
        age, x='Age Group', y='Churn Rate',
        color='Churn Rate',
        color_continuous_scale='RdYlGn_r',
        text=age['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='Churn Rate by Age Group'
    )
    fig3.add_hline(y=20.37, line_dash='dash',
                   line_color='gray',
                   annotation_text='Avg 20.37%')
    fig3.update_traces(textposition='outside')
    fig3.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    ten_order = ['New (0-2 yrs)', 'Mid (3-6 yrs)', 'Long (7+ yrs)']
    tenure = filtered.groupby('TenureGroup')['Exited'].mean() * 100
    tenure = tenure.reindex(ten_order).reset_index()
    tenure.columns = ['Tenure Group', 'Churn Rate']
    fig4 = px.bar(
        tenure, x='Tenure Group', y='Churn Rate',
        color='Churn Rate',
        color_continuous_scale='RdYlGn_r',
        text=tenure['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='Churn Rate by Tenure Group'
    )
    fig4.add_hline(y=20.37, line_dash='dash',
                   line_color='gray',
                   annotation_text='Avg 20.37%')
    fig4.update_traces(textposition='outside')
    fig4.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 4 — High Value Customer Explorer
# =============================================
st.header("💰 High Value Customer Churn Explorer")

col1, col2, col3 = st.columns(3)

hv_df    = filtered[filtered['Balance'] >= 100000]
hv_total = len(hv_df)
hv_churn = hv_df['Exited'].sum()
hv_safe  = hv_total - hv_churn
hv_bal   = hv_df[hv_df['Exited'] == 1]['Balance'].sum()

with col1:
    st.metric("High Value Customers", f"{hv_total:,}")
with col2:
    st.metric("High Value Churned", f"{hv_churn:,}")
with col3:
    st.metric("Balance at Risk (€)", f"€{hv_bal:,.0f}")

col1, col2 = st.columns(2)

with col1:
    fig5 = px.pie(
        values=[hv_safe, hv_churn],
        names=['Retained', 'Churned'],
        color_discrete_sequence=['#2ecc71', '#e74c3c'],
        title='High Value Customer Churn Split'
    )
    fig5.update_layout(height=380)
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    hv_geo = hv_df.groupby('Geography')['Exited'].mean() * 100
    hv_geo = hv_geo.reset_index()
    hv_geo.columns = ['Country', 'Churn Rate']
    fig6 = px.bar(
        hv_geo, x='Country', y='Churn Rate',
        color='Churn Rate',
        color_continuous_scale='RdYlGn_r',
        text=hv_geo['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='High Value Churn by Country'
    )
    fig6.update_traces(textposition='outside')
    fig6.update_layout(showlegend=False, height=380)
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 5 — Segment Deep Dive
# =============================================
st.header("🔍 Segment Deep Dive")

col1, col2 = st.columns(2)

with col1:
    gender = filtered.groupby('Gender')['Exited'].mean() * 100
    gender = gender.reset_index()
    gender.columns = ['Gender', 'Churn Rate']
    fig7 = px.bar(
        gender, x='Gender', y='Churn Rate',
        color='Gender',
        color_discrete_sequence=['#e91e8c', '#3498db'],
        text=gender['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='Churn Rate by Gender'
    )
    fig7.update_traces(textposition='outside')
    fig7.update_layout(showlegend=False, height=380)
    st.plotly_chart(fig7, use_container_width=True)

with col2:
    prod = filtered.groupby('NumOfProducts')['Exited'].mean() * 100
    prod = prod.reset_index()
    prod.columns = ['Products', 'Churn Rate']
    prod['Products'] = prod['Products'].astype(str)
    fig8 = px.bar(
        prod, x='Products', y='Churn Rate',
        color='Churn Rate',
        color_continuous_scale='RdYlGn_r',
        text=prod['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='Churn Rate by Number of Products'
    )
    fig8.update_traces(textposition='outside')
    fig8.update_layout(showlegend=False, height=380)
    st.plotly_chart(fig8, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    bal_order = ['Zero Balance', 'Low Balance', 'High Balance']
    bal = filtered.groupby('BalanceSegment')['Exited'].mean() * 100
    bal = bal.reindex(bal_order).reset_index()
    bal.columns = ['Balance Segment', 'Churn Rate']
    fig9 = px.bar(
        bal, x='Balance Segment', y='Churn Rate',
        color='Churn Rate',
        color_continuous_scale='RdYlGn_r',
        text=bal['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='Churn Rate by Balance Segment'
    )
    fig9.update_traces(textposition='outside')
    fig9.update_layout(showlegend=False, height=380)
    st.plotly_chart(fig9, use_container_width=True)

with col2:
    active = filtered.groupby('IsActiveMember')['Exited'].mean() * 100
    active = active.reset_index()
    active.columns = ['Status', 'Churn Rate']
    active['Status'] = active['Status'].map({0: 'Inactive', 1: 'Active'})
    fig10 = px.bar(
        active, x='Status', y='Churn Rate',
        color='Status',
        color_discrete_sequence=['#e74c3c', '#2ecc71'],
        text=active['Churn Rate'].apply(lambda x: f'{x:.1f}%'),
        title='Churn Rate by Active Membership'
    )
    fig10.update_traces(textposition='outside')
    fig10.update_layout(showlegend=False, height=380)
    st.plotly_chart(fig10, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 6 — Heatmaps
# =============================================
st.header("🗺️ Churn Heatmaps")

col1, col2 = st.columns(2)

with col1:
    age_order = ['Under 30', '30-45', '46-60', '60+']
    pivot1 = filtered.pivot_table(
        values='Exited',
        index='Geography',
        columns='AgeGroup',
        aggfunc='mean'
    ) * 100
    pivot1 = pivot1.reindex(columns=age_order)
    fig11 = px.imshow(
        pivot1, text_auto='.1f',
        color_continuous_scale='RdYlGn_r',
        title='Churn % — Geography x Age Group',
        aspect='auto'
    )
    fig11.update_layout(height=380)
    st.plotly_chart(fig11, use_container_width=True)

with col2:
    pivot2 = filtered.pivot_table(
        values='Exited',
        index='Geography',
        columns='Gender',
        aggfunc='mean'
    ) * 100
    fig12 = px.imshow(
        pivot2, text_auto='.1f',
        color_continuous_scale='RdYlGn_r',
        title='Churn % — Geography x Gender',
        aspect='auto'
    )
    fig12.update_layout(height=380)
    st.plotly_chart(fig12, use_container_width=True)

st.markdown("---")

# =============================================
# MODULE 7 — Raw Data Explorer
# =============================================
st.header("📋 Raw Data Explorer")

col1, col2 = st.columns([3, 1])
with col1:
    st.write(f"Showing {len(filtered):,} customers based on current filters")
with col2:
    show_churned = st.checkbox("Show churned only", value=False)

display_df = filtered[filtered['Exited'] == 1] if show_churned else filtered
st.dataframe(display_df.head(500), use_container_width=True)

st.markdown("---")
st.markdown("**European Banking Analytics** | Customer Churn Segmentation | 2026")