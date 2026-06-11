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

st.title("⚙️ Inventory Optimization")
st.caption("Economic Order Quantity (EOQ), Safety Stock & Reorder Point Optimization")

st.markdown("---")

# =====================================================
# OPTIMIZATION SUMMARY
# =====================================================

st.subheader("📊 Optimization Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Stockout Risk",
        "7"
    )

with col2:
    st.metric(
        "Overstock Risk",
        "135"
    )

with col3:
    st.metric(
        "Inventory Turnover",
        "0.59"
    )

with col4:
    st.metric(
        "Service Level",
        "95.33%"
    )

st.markdown("---")

# =====================================================
# INVENTORY PARAMETERS
# =====================================================

st.subheader("📦 Inventory Optimization Parameters")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average EOQ",
        "66.89"
    )

with col2:
    st.metric(
        "Average Safety Stock",
        "1719.61"
    )

with col3:
    st.metric(
        "Average ROP",
        "1966.94"
    )

with col4:
    st.metric(
        "Holding vs Ordering Cost",
        "10 : 50"
    )

st.markdown("---")

# =====================================================
# EOQ SAFETY STOCK ROP CHART
# =====================================================

st.subheader("📈 Optimization Parameters Comparison")

parameter_df = pd.DataFrame({
    "Parameter": [
        "EOQ",
        "Safety Stock",
        "ROP"
    ],
    "Value": [
        66.89,
        1719.61,
        1966.94
    ]
})

fig = px.bar(
    parameter_df,
    x="Parameter",
    y="Value",
    color="Parameter",
    text="Value",
    title="EOQ vs Safety Stock vs ROP"
)

fig.update_traces(
    texttemplate='%{text:.2f}',
    textposition='outside'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# RISK COMPOSITION
# =====================================================

st.subheader("⚠️ Inventory Risk Composition")

risk_df = pd.DataFrame({
    "Risk Type": [
        "Stockout Risk",
        "Overstock Risk"
    ],
    "Count": [
        7,
        135
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
# COST STRUCTURE
# =====================================================

st.subheader("💰 Cost Structure")

cost_df = pd.DataFrame({
    "Cost Type": [
        "Holding Cost",
        "Ordering Cost"
    ],
    "Value": [
        10,
        50
    ]
})

fig = px.bar(
    cost_df,
    x="Cost Type",
    y="Value",
    color="Cost Type",
    text="Value",
    title="Inventory Cost Structure"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# BUSINESS INTERPRETATION
# =====================================================

st.subheader("📋 Optimization Interpretation")

st.info("""
Inventory Optimization menghasilkan parameter inventory yang optimal.

Key Findings:

• Service Level mencapai 95.33%

• Average EOQ sebesar 66.89 unit

• Average Safety Stock sebesar 1719.61 unit

• Average Reorder Point sebesar 1966.94 unit

• Stockout Risk hanya 7 produk

• Overstock Risk sebanyak 135 produk

Parameter ini digunakan sebagai dasar
pengambilan keputusan inventory management.
""")

st.markdown("---")

# =====================================================
# RECOMMENDATION
# =====================================================

st.subheader("🚀 Decision Support Recommendation")

st.success("""
### Strategic Recommendation

1. Gunakan EOQ (66.89 unit) sebagai dasar pemesanan ekonomis.

2. Pertahankan Safety Stock rata-rata sebesar 1719.61 unit.

3. Terapkan Reorder Point (ROP) sebesar 1966.94 unit sebagai trigger replenishment.

4. Monitoring SKU dengan Overstock Risk tinggi.

5. Pertahankan Service Level di atas 95%.

6. Evaluasi inventory turnover secara berkala untuk meningkatkan efisiensi gudang.
""")

st.markdown("---")

st.caption(
    "Inventory Optimization Module | PT Mega Retail Indonesia"
)