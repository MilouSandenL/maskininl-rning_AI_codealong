# tightly coupled (via API blir det losely coupled)
from chat import JokeBot
import streamlit as st

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.meassage =[]

    if "bot" not in st.session_state:
        st.session_state.bot = JokeBot()
        
def display_chat_messages():
    """iterates over all historical messages and displays them"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            

            
        