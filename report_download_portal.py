import streamlit as st
def run():
    st.title("📥 Report Download Portal")
    st.download_button("Download Summary", "Summary content".encode(), "summary.pdf")