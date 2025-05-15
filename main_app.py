import streamlit as st
import central_dashboard
import memberships_tool
import sponsorship_ai_calculator
import event_creator_ai

TOOLS = {
    "📊 Central Dashboard": central_dashboard,
    "👥 Memberships": memberships_tool,
    "💼 Sponsorship AI": sponsorship_ai_calculator,
    "🎉 Event Creator": event_creator_ai
}

def run():
    st.set_page_config(page_title="Venture North Admin", layout="wide")
    st.sidebar.title("Select Tool")
    choice = st.sidebar.selectbox("Tool", list(TOOLS.keys()))
    TOOLS[choice].run()