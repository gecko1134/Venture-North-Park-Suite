import streamlit as st
import auth

TOOLS = {
}

def run():
    st.set_page_config(page_title='Venture North Admin', layout='wide')
    st.sidebar.title('🧭 Select Tool')
    selection = st.sidebar.selectbox('Choose a Tool', list(TOOLS.keys()))
    TOOLS[selection].run()