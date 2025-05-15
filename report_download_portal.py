import streamlit as st

def run():
    st.title("📥 Report Download Portal")

    st.markdown("### Latest Weekly Reports")
    st.download_button("Download Revenue Report (PDF)", "SampleRevenueReport".encode(), "revenue_report.pdf")
    st.download_button("Download Contract Summary (CSV)", "Contract,Value\nNike,50000".encode(), "contracts.csv")