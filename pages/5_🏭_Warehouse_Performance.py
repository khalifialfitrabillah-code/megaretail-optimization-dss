import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("🔒 Silakan login terlebih dahulu.")
    st.stop()

import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# LOGIN PROTECTION
# =====================================================

if "logged_in" not in st.session_state:
    st.switch_page("app.py")

if not st.session_state.logged_in:
    st.switch_page("app.py")

# =====================================================
# PAGE TITLE
# =====================================================

st.title("🏭 Warehouse Performance")
st.caption("Warehouse Monitoring & Service Level Analysis")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/inventory_final.csv")

# =====================================================
# KPI SUMMARY
# =====================================================

st.subheader("📊 Warehouse Performance Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Service Level",
        "95.33%"
    )

with col2:
    st.metric(
        "Warehouse",
        df["Warehouse_ID"].nunique()
    )

with col3:
    st.metric(
        "Inventory Records",
        len(df)
    )

with col4:
    st.metric(
        "Inventory Turnover",
        "0.59"
    )

st.markdown("---")

# =====================================================
# SERVICE LEVEL ANALYSIS
# =====================================================

st.subheader("⭐ Service Level Analysis")

service_df = pd.DataFrame({
    "Condition": [
        "Fulfilled Demand",
        "Potential Stockout"
    ],
    "Percentage": [
        95.33,
        4.67
    ]
})

fig = px.pie(
    service_df,
    names="Condition",
    values="Percentage",
    title="Service Level Performance"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# INVENTORY BY WAREHOUSE
# =====================================================

st.subheader("📦 Inventory Distribution by Warehouse")

warehouse_inventory = (
    df.groupby("Warehouse_ID")["Current_Inventory"]
    .sum()
    .reset_index()
)

fig = px.bar(
    warehouse_inventory,
    x="Warehouse_ID",
    y="Current_Inventory",
    color="Current_Inventory",
    title="Inventory Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# DEMAND BY WAREHOUSE
# =====================================================

st.subheader("📈 Demand Performance by Warehouse")

warehouse_demand = (
    df.groupby("Warehouse_ID")["Demand"]
    .sum()
    .reset_index()
)

fig = px.bar(
    warehouse_demand,
    x="Warehouse_ID",
    y="Demand",
    color="Demand",
    title="Demand Served by Warehouse"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# INVENTORY TURNOVER
# =====================================================

benchmark_df = pd.DataFrame({
    "Category": ["Current", "Target"],
    "Value": [0.59, 1.00]
})

fig = px.bar(
    benchmark_df,
    x="Category",
    y="Value",
    color="Category",
    text="Value",
    title="Inventory Turnover Benchmark"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================
# OPERATIONAL INSIGHT
# =====================================================

st.subheader("📋 Operational Insight")

st.info("""
Warehouse Performance Summary

• Service Level mencapai 95.33%

• Inventory Turnover sebesar 0.59

• Mayoritas permintaan berhasil dipenuhi

• Risiko stockout hanya sekitar 4.67%

• Distribusi inventory antar warehouse relatif stabil

Warehouse mampu mempertahankan tingkat pelayanan yang tinggi
dengan dukungan inventory yang memadai.
""")

st.markdown("---")

# =====================================================
# RECOMMENDATION
# =====================================================

st.subheader("🚀 Recommendation")

st.success("""
1. Pertahankan Service Level di atas 95%.

2. Monitoring warehouse dengan inventory turnover rendah.

3. Optimalkan redistribusi inventory antar warehouse.

4. Fokus pada pengurangan risiko stockout.

5. Gunakan hasil forecasting sebagai dasar replenishment.
""")

st.markdown("---")

st.caption(
    "Warehouse Performance Module | PT Mega Retail Indonesia"
)