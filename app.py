"""
app.py
-------
Main Streamlit application file.
Run this file using: streamlit run app.py
"""

import streamlit as st
from chatbot import StudentSupportBot
from utils import get_greeting_message

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Student Support Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ---------- LOAD CHATBOT (only once, cached) ----------
@st.cache_resource
def load_bot():
    return StudentSupportBot("knowledge_base.json")

bot = load_bot()

# ---------- SESSION STATE FOR CHAT HISTORY ----------
if "messages" not in st.session_state:
    # Each message is a dict: {"role": "user"/"bot", "text": "..."}
    st.session_state.messages = [
        {"role": "bot", "text": get_greeting_message()}
    ]

# ---------- TITLE ----------
st.title("AI Student Support Chatbot")
st.caption("Ask me about attendance, fees, exams, library, hostel, placements, scholarships, holidays, timetable & faculty.")

st.divider()

# ---------- DISPLAY CHAT HISTORY ----------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["text"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["text"])

# ---------- INPUT AREA ----------
user_input = st.chat_input("Type your question here...")

if user_input:
    # 1. Add user message to history
    st.session_state.messages.append({"role": "user", "text": user_input})

    # 2. Get chatbot's response
    response = bot.get_response(user_input)

    # 3. Add bot response to history
    st.session_state.messages.append({"role": "bot", "text": response})

    # 4. Refresh the page to show new messages
    st.rerun()

# ---------- CLEAR CHAT BUTTON ----------
st.divider()
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {"role": "bot", "text": get_greeting_message()}
        ]
        st.rerun()