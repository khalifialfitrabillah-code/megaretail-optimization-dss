import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("🔒 Silakan login terlebih dahulu.")
    st.stop()

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy.stats import gaussian_kde

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

st.title("🎯 What-If Analysis")
st.caption("Scenario Simulation & Decision Support System")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/inventory_final.csv")

# =====================================================
# SCENARIO SELECTOR
# =====================================================

st.markdown("### Select Scenario")

scenario = st.radio(
    "",
    [
        "Demand +20%",
        "Lead Time +50%",
        "Capacity Reduction",
        "New Warehouse",
        "Service Level +5%"
    ],
    horizontal=True
)

st.markdown("---")

# =====================================================
# SCENARIO 1
# =====================================================

if scenario == "Demand +20%":

    st.subheader("📈 Scenario 1 : Demand Increase 20%")

    original_avg = 467.37
    surged_avg = 560.85

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Original Demand Average",
            f"{original_avg:.2f}"
        )

    with col2:
        st.metric(
            "Surged Demand Average",
            f"{surged_avg:.2f}"
        )

    original_demand = df["Demand"]
    scenario_demand = original_demand * 1.2

    x = np.linspace(
        min(original_demand.min(),
            scenario_demand.min()),
        max(original_demand.max(),
            scenario_demand.max()),
        500
    )

    kde_original = gaussian_kde(original_demand)
    kde_scenario = gaussian_kde(scenario_demand)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=kde_original(x),
            mode="lines",
            fill="tozeroy",
            name="Original Demand"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=kde_scenario(x),
            mode="lines",
            fill="tozeroy",
            name="Demand +20%"
        )
    )

    fig.update_layout(
        title="Demand Distribution Shift",
        xaxis_title="Demand Volume",
        yaxis_title="Density",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# SCENARIO 2
# =====================================================

elif scenario == "Lead Time +50%":

    st.subheader("🚚 Scenario 2 : Lead Time Increase 50%")

    current_lead = df["Lead_Time"].mean()
    delayed_lead = current_lead * 1.5

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Current Lead Time",
            f"{current_lead:.2f} Days"
        )

    with col2:
        st.metric(
            "Delayed Lead Time",
            f"{delayed_lead:.2f} Days"
        )

    chart_df = pd.DataFrame({
        "Condition": [
            "Current",
            "Delayed"
        ],
        "Lead Time": [
            current_lead,
            delayed_lead
        ]
    })

    fig = px.bar(
        chart_df,
        x="Condition",
        y="Lead Time",
        color="Condition",
        text="Lead Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# SCENARIO 3
# =====================================================

elif scenario == "Capacity Reduction":

    st.subheader("🏭 Scenario 3 : Warehouse Capacity Reduction")

    current_capacity = 10000
    reduced_capacity = 8000

    overflow_products = (
        df["Current_Inventory"]
        > reduced_capacity
    ).sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Capacity",
            current_capacity
        )

    with col2:
        st.metric(
            "Reduced Capacity",
            reduced_capacity
        )

    with col3:
        st.metric(
            "Overflow Products",
            overflow_products
        )

    fig = px.histogram(
        df,
        x="Current_Inventory",
        nbins=20,
        title="Warehouse Capacity Risk"
    )

    fig.add_vline(
        x=reduced_capacity,
        line_dash="dash",
        line_color="red"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# SCENARIO 4
# =====================================================

elif scenario == "New Warehouse":

    st.subheader("🏗️ Scenario 4 : New Warehouse Addition")

    capacity_df = pd.DataFrame({
        "Condition": [
            "Current Capacity",
            "Expanded Capacity"
        ],
        "Capacity": [
            10000,
            15000
        ]
    })

    fig = px.bar(
        capacity_df,
        x="Condition",
        y="Capacity",
        color="Condition",
        text="Capacity"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# SCENARIO 5
# =====================================================

elif scenario == "Service Level +5%":

    st.subheader("⭐ Scenario 5 : Service Level Increase")

    current_sl = 95.33
    target_sl = 100.00

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Current Service Level",
            f"{current_sl:.2f}%"
        )

    with col2:
        st.metric(
            "Target Service Level",
            f"{target_sl:.2f}%"
        )

    comparison_df = pd.DataFrame({
        "Level": [
            "Current",
            "Target"
        ],
        "Service Level": [
            current_sl,
            target_sl
        ]
    })

    fig = px.bar(
        comparison_df,
        x="Level",
        y="Service Level",
        color="Level",
        text="Service Level"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# RECOMMENDATION
# =====================================================

st.markdown("---")

st.success("""
### Decision Support Recommendation

✔ Demand Surge → Increase Safety Stock

✔ Lead Time Delay → Increase Reorder Point

✔ Capacity Reduction → Optimize Warehouse Utilization

✔ New Warehouse → Expand Inventory Flexibility

✔ Service Level Increase → Improve Customer Satisfaction
""")