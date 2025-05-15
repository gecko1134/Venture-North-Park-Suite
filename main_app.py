import streamlit as st
from auth import run as auth_run

import ai_matchmaker_toolimport ai_scheduler_toolimport ai_scheduling_suggestionsimport central_dashboardimport complex_usage_optimizerimport contract_insights_aiimport contract_usage_trackerimport dome_usage_toolimport dynamic_pricing_toolimport event_control_panelimport facility_access_trackerimport facility_contract_monitorimport facility_master_trackerimport facility_membership_comparator_aiimport facility_membership_monitorimport governance_toolimport league_coordinatorimport marketing_flipbook_generatorimport membership_credit_trackerimport membership_crm_trackerimport membership_goal_trackerimport membership_insights_aiimport membership_loyalty_rewardsimport membership_marketing_aiimport membership_ticketing_integrationimport memberships_toolimport mentorship_centerimport nil_trackerimport pandadoc_contractimport performance_goal_aiimport proposal_to_pdfimport referee_managerimport report_download_portalimport revenue_heatmapimport revenue_proforma_autoimport scholarship_fund_managerimport scholarship_trackerimport sponsor_dashboardimport sponsorship_ai_calculatorimport sponsorship_availabilityimport sponsorship_contract_generatorimport sponsorship_inventory_managerimport sponsorship_roi_trackerimport sponsorship_trackerimport student_committeeimport team_club_managerimport visual_calendar_layoutimport volunteer_hubimport weekly_report_generator

TOOLS = {
    "Ai Matchmaker Tool": ai_matchmaker_tool
    "Ai Scheduler Tool": ai_scheduler_tool
    "Ai Scheduling Suggestions": ai_scheduling_suggestions
    "Central Dashboard": central_dashboard
    "Complex Usage Optimizer": complex_usage_optimizer
    "Contract Insights Ai": contract_insights_ai
    "Contract Usage Tracker": contract_usage_tracker
    "Dome Usage Tool": dome_usage_tool
    "Dynamic Pricing Tool": dynamic_pricing_tool
    "Event Control Panel": event_control_panel
    "Facility Access Tracker": facility_access_tracker
    "Facility Contract Monitor": facility_contract_monitor
    "Facility Master Tracker": facility_master_tracker
    "Facility Membership Comparator Ai": facility_membership_comparator_ai
    "Facility Membership Monitor": facility_membership_monitor
    "Governance Tool": governance_tool
    "League Coordinator": league_coordinator
    "Marketing Flipbook Generator": marketing_flipbook_generator
    "Membership Credit Tracker": membership_credit_tracker
    "Membership Crm Tracker": membership_crm_tracker
    "Membership Goal Tracker": membership_goal_tracker
    "Membership Insights Ai": membership_insights_ai
    "Membership Loyalty Rewards": membership_loyalty_rewards
    "Membership Marketing Ai": membership_marketing_ai
    "Membership Ticketing Integration": membership_ticketing_integration
    "Memberships Tool": memberships_tool
    "Mentorship Center": mentorship_center
    "Nil Tracker": nil_tracker
    "Pandadoc Contract": pandadoc_contract
    "Performance Goal Ai": performance_goal_ai
    "Proposal To Pdf": proposal_to_pdf
    "Referee Manager": referee_manager
    "Report Download Portal": report_download_portal
    "Revenue Heatmap": revenue_heatmap
    "Revenue Proforma Auto": revenue_proforma_auto
    "Scholarship Fund Manager": scholarship_fund_manager
    "Scholarship Tracker": scholarship_tracker
    "Sponsor Dashboard": sponsor_dashboard
    "Sponsorship Ai Calculator": sponsorship_ai_calculator
    "Sponsorship Availability": sponsorship_availability
    "Sponsorship Contract Generator": sponsorship_contract_generator
    "Sponsorship Inventory Manager": sponsorship_inventory_manager
    "Sponsorship Roi Tracker": sponsorship_roi_tracker
    "Sponsorship Tracker": sponsorship_tracker
    "Student Committee": student_committee
    "Team Club Manager": team_club_manager
    "Visual Calendar Layout": visual_calendar_layout
    "Volunteer Hub": volunteer_hub
    "Weekly Report Generator": weekly_report_generator
}

def run():
    st.set_page_config(page_title="Venture North Admin", layout="wide")
    st.sidebar.title("🏟️ Venture North Tools")
    selected = st.sidebar.selectbox("Select a Tool", list(TOOLS.keys()))
    TOOLS[selected].run()