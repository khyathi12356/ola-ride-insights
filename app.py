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

# ---------------------------
# SESSION STATE (GLOBAL FILTERS)
# ---------------------------
if "vehicle_type" not in st.session_state:
    st.session_state.vehicle_type = []

if "booking_status" not in st.session_state:
    st.session_state.booking_status = []

if "payment_method" not in st.session_state:
    st.session_state.payment_method = []

# ---------------------------
# SIDEBAR SLICERS
# ---------------------------
st.sidebar.header("🔎 Global Filters")

# Vehicle Type (MULTISELECT)
st.session_state.vehicle_type = st.sidebar.multiselect(
    "Vehicle Type",
    ["Prime Sedan", "Bike", "Prime SUV", "eBike", "Mini", "Prime Plus", "Auto"],
    default=st.session_state.vehicle_type
)

# Booking Status (MULTISELECT)
st.session_state.booking_status = st.sidebar.multiselect(
    "Booking Status",
    ["Success", "Canceled by Customer", "Canceled by Driver", "Driver Not Found"],
    default=st.session_state.booking_status
)

# Payment Method (MULTISELECT)
st.session_state.payment_method = st.sidebar.multiselect(
    "Payment Method",
    ["Unknown", "Cash", "UPI", "Credit Card", "Debit Card"],
    default=st.session_state.payment_method
)

# ---------------------------
# SHOW SELECTED FILTERS
# ---------------------------
st.markdown("### 🎛️ Selected Filters")

st.write("🚗 Vehicle Type:", st.session_state.vehicle_type or "All")
st.write("📌 Booking Status:", st.session_state.booking_status or "All")
st.write("💳 Payment Method:", st.session_state.payment_method or "All")

st.success("These filters will apply across all pages.")