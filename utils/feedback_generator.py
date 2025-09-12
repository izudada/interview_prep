import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("G_TOKEN")
if not API_KEY:
    raise RuntimeError("Missing GEMINI_API_KEY in environment")

genai.configure(api_key=API_KEY)

# Choose model (Gemini 1.5 Pro = strong reasoning, Gemini 1.5 Flash = fast/cheap)
DEFAULT_MODEL = "gemini-1.5-flash"


def get_feedback(
        question, 
        answer, 
        # tone
):
    # tone_text = "As a {tone.lower()} interviewer, evaluate the following response."

    system_prompt = f"""
    You are an interview coach.
    Evaluate the following response in 2-3 sentences with constructive feedback.

    Question: {question}
    Answer: {answer}
    """

    model = genai.GenerativeModel(DEFAULT_MODEL)
    response = model.generate_content(system_prompt)
    return response.text.strip()
