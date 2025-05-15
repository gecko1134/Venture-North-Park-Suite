import streamlit as st

import ai_matchmaker_tool
import ai_scheduler_tool
import ai_scheduling_suggestions
import central_dashboard
import complex_usage_optimizer
import contract_insights_ai
import contract_usage_tracker
import dome_usage_tool
import dynamic_pricing_tool
import event_control_panel
import facility_access_tracker
import facility_contract_monitor
import facility_master_tracker
import facility_membership_comparator_ai
import facility_membership_monitor
import governance_tool
import league_coordinator
import marketing_flipbook_generator
import membership_credit_tracker
import membership_crm_tracker
import membership_goal_tracker
import membership_insights_ai
import membership_loyalty_rewards
import membership_marketing_ai
import membership_ticketing_integration
import memberships_tool
import mentorship_center
import nil_tracker
import pandadoc_contract
import performance_goal_ai
import proposal_to_pdf
import referee_manager
import report_download_portal
import revenue_heatmap
import revenue_proforma_auto
import scholarship_fund_manager
import sponsorship_ai_calculator
import sponsorship_availability
import sponsorship_contract_generator
import sponsorship_tracker
import weekly_report_generator
import event_creator_ai
import event_goal_tracker
import event_marketing_perks_ai
import event_sponsor_builder

TOOLS = {
    "Dashboard": central_dashboard,
    "Memberships": memberships_tool,
    "Member CRM": membership_crm_tracker,
    "Membership Marketing": membership_marketing_ai,
    "Membership Goals": membership_goal_tracker,
    "Membership Loyalty": membership_loyalty_rewards,
    "Ticketing & Access Logs": membership_ticketing_integration,
    "Sponsorship Tracker": sponsorship_tracker,
    "Sponsorship AI Calculator": sponsorship_ai_calculator,
    "Sponsorship Contract Generator": sponsorship_contract_generator,
    "Sponsorship Availability": sponsorship_availability,
    "Proposal to PDF": proposal_to_pdf,
    "PandaDoc Contract": pandadoc_contract,
    "Contracts Tracker": contract_usage_tracker,
    "Contract AI Insights": contract_insights_ai,
    "Facility Contracts Benchmark": facility_contract_monitor,
    "Revenue Heatmap": revenue_heatmap,
    "Revenue Proforma": revenue_proforma_auto,
    "Scheduler AI": ai_scheduler_tool,
    "Scheduling Suggestions": ai_scheduling_suggestions,
    "Dynamic Pricing Tool": dynamic_pricing_tool,
    "Facility Optimizer": complex_usage_optimizer,
    "Visual Layout": facility_master_tracker,
    "Event Creator AI": event_creator_ai,
    "Event Sponsorship Builder": event_sponsor_builder,
    "Event Goals Tracker": event_goal_tracker,
    "Event Conflict Calendar": event_control_panel,
    "Event Marketing AI": event_marketing_perks_ai,
    "Volunteer Manager": referee_manager,
    "Referees": referee_manager,
    "Teams & Leagues": team_club_manager,
    "League Coordinator": league_coordinator,
    "Governance": governance_tool,
    "Student Committee": scholarship_fund_manager,
    "Mentorships": mentorship_center,
    "Scholarship Fund": scholarship_fund_manager,
    "NIL Tracker": nil_tracker,
    "AI Matchmaker": ai_matchmaker_tool,
    "Weekly Report Generator": weekly_report_generator,
    "Report Downloads": report_download_portal,
    "Facility Membership Comparison": facility_membership_comparator_ai,
    "Facility Access Log": facility_access_tracker
}

def run():
    st.set_page_config(page_title="Venture North Admin", layout="wide")
    st.sidebar.title("📊 Admin Tools")
    selected = st.sidebar.selectbox("Select Tool", list(TOOLS.keys()))
    TOOLS[selected].run()