import streamlit as st

from components import (
    footer_section, 
    hero_section, 
    interview_flow,
    tone_selector_card
)
from utils.question_generator import generate_questions



# Create toggle (simulates an ON/OFF switch)
dark_mode = st.toggle(
    "🌙 Light Mode" if not st.session_state.get("dark_mode", False) else "☀️ Dark Mode"
)

# Set color variables based on mode
if dark_mode:
    background = "#121212"
    text_color = "#ffffff"
    card_background = "#1e1e1e"
    st.session_state.dark_mode = dark_mode
else:
    background = "#f9f9f9"
    text_color = "#000000"
    card_background = "#ffffff"
    st.session_state.dark_mode = dark_mode
   

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {background};
            color: {text_color};
            display: flex;
            flex-direction: column;
        }}

        div[data-testid="stMarkdownContainer"] > p {{
            color: {text_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

hero_section()

tone_selector_card()

if st.session_state.get("start"):
    if "questions" not in st.session_state or not st.session_state.questions:
        st.session_state.questions = generate_questions(
            # st.session_state.tone, 
            st.session_state.num_questions,
            st.session_state.text_input,
            st.session_state.difficulty_level
        )
        
    interview_flow()

footer_section()
