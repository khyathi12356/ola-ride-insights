import streamlit as st
from utils.db import create_database

st.set_page_config(page_title="OLA Dashboard", layout="wide")

st.title("🚖 OLA Ride Insights Dashboard")

st.sidebar.success("Navigate pages from left menu")

# RUN ONLY ONCE (safe)
if st.button("🔄 Reset Database"):
    create_database()
    st.success("Database rebuilt successfully!")