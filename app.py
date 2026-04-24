import streamlit as st

st.set_page_config(page_title="OLA Dashboard", layout="wide")

# Main Title
st.title("🚖 OLA Ride Insights Dashboard")

# Sidebar info
st.sidebar.success("Navigate pages from left menu")

# Welcome section
st.markdown("""
### 📊 Welcome to the OLA Ride Insights Dashboard  
This dashboard provides insights into ride trends, cancellations, revenue, and customer behavior using data analytics.
""")