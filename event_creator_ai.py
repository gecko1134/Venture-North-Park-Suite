import streamlit as st

def run():
    st.title("🎉 Event Creator AI")
    event = st.selectbox("Event Type", ["Esports", "Wedding", "Expo", "Movie Night", "Festival"])
    location = st.selectbox("Surface", ["Full Dome", "Half Turf", "Court 1", "Court 2", "Pavilion"])
    duration = st.slider("Hours", 1, 12, 4)
    setup = st.radio("Setup Type", ["Turnkey", "Partial", "DIY"])

    cost = 150 * duration
    if location == "Full Dome": cost *= 3
    elif location == "Half Turf": cost *= 2
    if setup == "Turnkey": cost *= 1.5
    elif setup == "Partial": cost *= 1.2

    st.metric("Estimated Cost", f"${cost:,.2f}")
    st.success(f"{event} created for {duration} hours on {location} with {setup} setup.")