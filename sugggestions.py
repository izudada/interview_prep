from openai import OpenAI  # or use openai.ChatCompletion depending on your SDK
import openai

openai.api_key = st.secrets["openai_api_key"]

def generate_questions(tone, num_questions):
    prompt = f"""
    You are an interviewer with a {tone.lower()} tone.
    Generate {num_questions} interview questions suitable for a job candidate.
    Keep them clear and concise.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "system", "content": prompt}],
        temperature=0.7
    )

    return [q.strip() for q in response["choices"][0]["message"]["content"].split("\n") if q.strip()]


def interview_flow():
    if "questions" not in st.session_state or not st.session_state.questions:
        st.session_state.questions = generate_questions(st.session_state.tone, st.session_state.num_questions)

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


def get_feedback(question, answer, tone):
    prompt = f"""
    As a {tone.lower()} interviewer, evaluate the following response.

    Question: {question}
    Answer: {answer}

    Provide specific feedback in 2-3 sentences.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"].strip()


def main():
    st.title("AI Interview Assistant")

    if "start" not in st.session_state:
        st.session_state.start = False

    if not st.session_state.start:
        tone_selector_card()
    else:
        interview_flow()

if __name__ == "__main__":
    main()
