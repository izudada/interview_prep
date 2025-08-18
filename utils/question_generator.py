import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("TOGETHER_API_KEY")

CLIENT = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)


def generate_questions(
        # tone, 
        num_questions, 
        profession,
        difficulty_level
):
    import ollama

    # tone_text = f"with a {tone.lower()} tone"
    prompt = f"""
    You are an interviewer.
    Generate {num_questions} interview questions suitable for a job candidate 
    for the role of {profession}.
    Keep them clear and concise. 
    Question difficulty level should be {difficulty_level}
    """

    response = ollama.chat(
        model='gemma:2b',  # or 'gemma:7b' if you have enough RAM space
        messages=[
            {
                'role': 'system', 
                'content': prompt
            }
        ]
    )

    return [
        q.strip() for q in response.message.content.split("\n") 
        if q.strip() and "question"not in q.strip().lower()
    ]
