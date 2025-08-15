import streamlit as st

from utils import generate_questions, get_feedback


def interview_flow():
    if "questions" not in st.session_state or not st.session_state.questions:
        st.session_state.questions = generate_questions(
            st.session_state.tone, 
            st.session_state.num_questions,
            st.session_state.text_input
        )

    current = st.session_state.current_question
    if current < len(st.session_state.questions):
        question = st.session_state.questions[current]
        st.markdown(f"**Question {current + 1}:** {question}")
        answer = st.text_area("Your Answer:", key=f"answer_{current}")

        if st.button("Submit Answer"):
            feedback = get_feedback(question, answer, st.session_state.tone)
            st.session_state.feedback.append(feedback)
            st.session_state.current_question += 1
            st.experimental_rerun()
    else:
        st.success("🎉 Interview Completed!")
        st.markdown("### Feedback Summary")
        for i, fb in enumerate(st.session_state.feedback):
            st.markdown(f"**Q{i+1} Feedback:** {fb}")
