import streamlit as st
import auth

import memberships_tool
import sponsorship_ai_calculator
import event_creator_ai
import central_dashboard
import google_sheets_sync
import email_notifications
import flipbook_embedder
import pdf_export_tool
import setup_assistant_ai
import mobile_friendly_ui
import weekly_report_generator
import report_download_portal

TOOLS = {
    "Memberships Tool": memberships_tool
    "Sponsorship Ai Calculator": sponsorship_ai_calculator
    "Event Creator Ai": event_creator_ai
    "Central Dashboard": central_dashboard
    "Google Sheets Sync": google_sheets_sync
    "Email Notifications": email_notifications
    "Flipbook Embedder": flipbook_embedder
    "Pdf Export Tool": pdf_export_tool
    "Setup Assistant Ai": setup_assistant_ai
    "Mobile Friendly Ui": mobile_friendly_ui
    "Weekly Report Generator": weekly_report_generator
    "Report Download Portal": report_download_portal
}

def run():
    st.set_page_config(page_title="Venture North Admin", layout="wide")
    st.sidebar.title("📊 Admin Tools")
    selected = st.sidebar.selectbox("Select Tool", list(TOOLS.keys()))
    TOOLS[selected].run()