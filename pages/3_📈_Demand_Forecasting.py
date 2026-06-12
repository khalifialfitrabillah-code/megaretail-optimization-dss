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
# PAGE CONFIG
# =====================================================

st.title("📈 Demand Forecasting")
st.caption("Predictive Analytics using Random Forest Forecast Model")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/inventory_final.csv")

# =====================================================
# MODEL EVALUATION
# =====================================================

st.subheader("🎯 Forecast Model Evaluation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "MAE",
        "34.50"
    )

with col2:
    st.metric(
        "MAPE",
        "15.56%"
    )

with col3:
    st.metric(
        "RMSE",
        "56.06"
    )

with col4:
    st.metric(
        "R² Score",
        "0.96"
    )

st.success("""
Model Random Forest menunjukkan performa yang sangat baik.

• MAE = 34.50

• MAPE = 15.56%

• RMSE = 56.06

• R² = 0.96

Model memiliki akurasi tinggi dan layak digunakan
sebagai dasar Decision Support System (DSS).
""")

st.markdown("---")

# =====================================================
# ACTUAL VS FORECAST
# =====================================================

st.subheader("📊 Demand vs Forecast Demand")

sample_df = df.head(50)

fig = px.line(
    sample_df,
    y=["Demand", "Forecast_Demand"],
    title="Actual Demand vs Forecast Demand"
)

fig.update_layout(
    xaxis_title="Product Index",
    yaxis_title="Demand"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# DEMAND DISTRIBUTION
# =====================================================

st.subheader("📦 Demand Distribution")

fig = px.histogram(
    df,
    x="Demand",
    nbins=20,
    title="Demand Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# FORECAST DISTRIBUTION
# =====================================================

st.subheader("🔮 Forecast Demand Distribution")

fig = px.histogram(
    df,
    x="Forecast_Demand",
    nbins=20,
    title="Forecast Demand Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# FORECAST INSIGHT
# =====================================================

st.subheader("📌 Forecast Insight")

st.info(f"""
Total Produk            : {df['Product_ID'].nunique()}

Rata-rata Demand        : {df['Demand'].mean():.2f}

Rata-rata Forecast      : {df['Forecast_Demand'].mean():.2f}

Model digunakan untuk membantu
perencanaan inventory dan
pengambilan keputusan replenishment.
""")