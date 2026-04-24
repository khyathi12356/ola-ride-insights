import streamlit as st
from utils.db import create_database

st.set_page_config(page_title="OLA Dashboard", layout="wide")

st.title("🚖 OLA Ride Insights Dashboard")

st.sidebar.success("Navigate pages from left menu")

st.markdown("""
### 📊 Welcome to the OLA Ride Insights Dashboard
This dashboard provides insights into ride trends, cancellations, revenue, and customer behavior.
""")

# Developer-only section (hidden from normal users)
if st.sidebar.checkbox("🔧 Developer Mode"):
    if st.button("🔄 Reset Database"):
        create_database()
        st.success("Database rebuilt successfully!")