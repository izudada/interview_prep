import streamlit as st


def tone_selector_card():

    with st.form("tone_form"):
        # Inject button style
        st.markdown("""
            <style>
            button[kind='secondaryFormSubmit']{
                color: white !important;
                background-color: #1a73e8 !important;
                border-radius: 8px;
                padding: 0.5rem 1.2rem;
                font-weight: bold;
            }
            div.stButton > button:first-child:hover {
                background-color: #155ab6 !important;
            }
            </style>
        """, unsafe_allow_html=True)

        # tone = st.selectbox("Select Interviewer Tone", ["Professional", "Sassy", "Strict"])
        difficulty_level = st.selectbox("Select Difficulty Level", ["Easy", "Medium", "Tough"])
        num_questions = st.number_input("Number of Questions", min_value=1, max_value=10, value=3, step=1)
        text_input = st.text_input(
            "Interviewee Role (eg. Digital Marketer)", 
            max_chars=50
        )
        submitted = st.form_submit_button(
            "Start Interview",
            type="secondary"
        )

    if submitted:
        # st.session_state.tone = tone
        st.session_state.difficulty_level = difficulty_level
        st.session_state.num_questions = num_questions
        st.session_state.text_input = text_input
        st.session_state.start = True
        st.session_state.current_question = 0
        st.session_state.questions = []
        st.session_state.feedback = []
        st.rerun()
