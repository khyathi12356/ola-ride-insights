import streamlit as st

st.title("📊 Power BI Dashboard (Showcase)")

st.markdown("""
### 🚖 OLA Ride Insights Dashboard

This section presents the Power BI dashboards created for business insights.

Since Power BI service embedding is not available, dashboards are shown as exported visuals.
""")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overall", "Vehicle", "Revenue", "Cancellation", "Ratings"
])

with tab1:
    st.image("assets/overall.png", use_container_width=True)

with tab2:
    st.image("assets/vehicle.png", use_container_width=True)

with tab3:
    st.image("assets/revenue.png", use_container_width=True)

with tab4:
    st.image("assets/cancel.png", use_container_width=True)

with tab5:
    st.image("assets/ratings.png", use_container_width=True)

st.info("📌 Note: Interactive charts are available in other pages of this app.")