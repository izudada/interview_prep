import os

from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI


load_dotenv()

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("G_TOKEN")
if not API_KEY:
    raise RuntimeError("Missing GEMINI_API_KEY in environment")

genai.configure(api_key=API_KEY)

# Choose model (Gemini 1.5 Pro = strong reasoning, Gemini 1.5 Flash = fast/cheap)
DEFAULT_MODEL = "gemini-1.5-flash"


def generate_questions(
        # tone, 
        num_questions, 
        profession,
        difficulty_level
):

    # tone_text = f"with a {tone.lower()} tone"
    system_prompt = f"""
    You are an interviewer.
    Generate {num_questions} concise interview questions for a candidate applying
    for the role of {profession}.
    Difficulty: {difficulty_level}.
    Return the questions as a simple numbered list.
    """

    model = genai.GenerativeModel(DEFAULT_MODEL)
    response = model.generate_content(system_prompt)

    # Parse response into clean list
    text = response.text.strip()
    lines = [l.strip("0123456789. )-") for l in text.splitlines() if l.strip()]
    return lines[:num_questions]
