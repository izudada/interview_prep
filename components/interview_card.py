import streamlit as st
import time

from utils import get_feedback


def interview_flow():

    current = st.session_state.current_question
    if current < len(st.session_state.questions):
        question = st.session_state.questions[current]
        
        st.markdown(f"**Question {current + 1}:** {question}")
        # placeholder = st.empty()   # reserve a placeholder for live updates 

        # full_text = ""  # store accumulated text
        # for chunk in question:
        #     full_text += chunk
        #     placeholder.markdown(full_text)  # update progressively
        #     time.sleep(0.05) 

        answer = st.text_area("Your Answer:", key=f"answer_{current}")

        if st.button("Submit Answer"):
            feedback = get_feedback(
                question, 
                answer, 
                # st.session_state.tone
            )
            st.session_state.feedback.append(feedback)
            st.session_state.current_question += 1
            st.rerun()
    else:
        st.success("🎉 Interview Completed!")
        st.markdown("### Feedback Summary")
        for i, fb in enumerate(st.session_state.feedback):
            st.markdown(f"**Q{i+1} Feedback:** {fb}")
