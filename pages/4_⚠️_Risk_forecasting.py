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

st.title("⚠️ Risk Forecasting")
st.caption("Inventory Risk Monitoring & Decision Support System")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/inventory_final.csv")

# =====================================================
# KPI SUMMARY
# =====================================================

stockout_risk = (df["Stockout_Risk"] == 1).sum()
overstock_risk = (df["Overstock_Risk"] == 1).sum()

increase_inventory = stockout_risk
reduce_inventory = overstock_risk

st.subheader("📊 Risk Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Stockout Risk",
        stockout_risk
    )

with col2:
    st.metric(
        "Overstock Risk",
        overstock_risk
    )

with col3:
    st.metric(
        "Increase Inventory",
        increase_inventory
    )

with col4:
    st.metric(
        "Reduce Inventory",
        reduce_inventory
    )

st.markdown("---")

# =====================================================
# RISK COMPOSITION
# =====================================================

st.subheader("🚨 Risk Composition")

risk_df = pd.DataFrame({
    "Risk Type": [
        "Stockout Risk",
        "Overstock Risk"
    ],
    "Count": [
        stockout_risk,
        overstock_risk
    ]
})

fig = px.pie(
    risk_df,
    names="Risk Type",
    values="Count",
    title="Inventory Risk Composition"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# STOCKOUT VS OVERSTOCK
# =====================================================

st.subheader("📈 Risk Comparison")

fig = px.bar(
    risk_df,
    x="Risk Type",
    y="Count",
    color="Risk Type",
    text="Count",
    title="Stockout vs Overstock Risk"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# WAREHOUSE RISK ANALYSIS
# =====================================================

st.subheader("🏭 Warehouse Risk Analysis")

warehouse_risk = (
    df.groupby("Warehouse_ID")
    .agg({
        "Stockout_Risk": "sum",
        "Overstock_Risk": "sum"
    })
    .reset_index()
)

fig = px.bar(
    warehouse_risk,
    x="Warehouse_ID",
    y=[
        "Stockout_Risk",
        "Overstock_Risk"
    ],
    barmode="group",
    title="Risk by Warehouse"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# DECISION SUPPORT
# =====================================================

st.subheader("📋 Risk Recommendation")

st.success(f"""
Inventory Risk Assessment:

• Stockout Risk SKU : {stockout_risk}

• Overstock Risk SKU : {overstock_risk}

Recommended Actions:

1. Tambah inventory pada SKU dengan Stockout Risk.

2. Kurangi inventory pada SKU dengan Overstock Risk.

3. Monitoring warehouse dengan risiko tertinggi.

4. Pertahankan Service Level di atas 95%.

5. Evaluasi replenishment policy secara berkala.
""")

st.markdown("---")

st.caption(
    "Risk Forecasting Module | PT Mega Retail Indonesia"
)