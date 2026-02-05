import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration (The 'Power BI' feel)
st.set_page_config(page_title="Sales Insights Dashboard", layout="wide")

# Custom CSS to make cards look like Power BI "tiles"
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0045ad;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar for Filters
st.sidebar.header("Filter Pane")
region = st.sidebar.multiselect("Select Region", ["North", "South", "East", "West"], default=["North", "South"])

# 3. Dummy Data
data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"] * 25,
    "Sales": [200, 150, 300, 400] * 25,
    "Profit": [20, 15, 60, 80] * 25
})

# 4. Header Section
st.title("📊 Executive Sales Overview")
st.markdown("---")

# 5. KPI Cards (Power BI Tiles)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Sales", value="$105,000", delta="+15%")
with col2:
    st.metric(label="Total Profit", value="$24,000", delta="-2%")
with col3:
    st.metric(label="Active Users", value="1,240", delta="18%")

# 6. Charts Section
st.markdown("### Visual Analytics")
left_chart, right_chart = st.columns(2)

fig1 = px.bar(data, x="Region", y="Sales", color="Region", title="Sales by Region")
left_chart.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(data, values='Profit', names='Region', title='Profit Contribution')
right_chart.plotly_chart(fig2, use_container_width=True)
