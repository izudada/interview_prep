import streamlit as st

from components import (
    footer_section, 
    hero_section, 
    interview_flow,
    tone_selector_card
)
from utils.question_generator import generate_questions


hero_section()

with st.sidebar:

    tone_selector_card()

    footer_section()


if st.session_state.get("start"):
    if "questions" not in st.session_state or not st.session_state.questions:
        st.session_state.questions = generate_questions(
            # st.session_state.tone, 
            st.session_state.num_questions,
            st.session_state.text_input,
            st.session_state.difficulty_level
        )
        
    interview_flow()
