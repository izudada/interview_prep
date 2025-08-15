import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("TOGETHER_API_KEY")

CLIENT = OpenAI(api_key=API_KEY)


def get_feedback(question, answer, tone):
    prompt = f"""
    As a {tone.lower()} interviewer, evaluate the following response.

    Question: {question}
    Answer: {answer}

    Provide specific feedback in 2-3 sentences.
    """
    import ollama


    response = ollama.chat(
        model='gemma:2b',  # or 'gemma:7b' if you have enough RAM space
        messages=[
            {
                'role': 'system', 
                'content': prompt
            }
        ]
    )

    feedback = response.message.content.split("\n") 
    print("FEEEEEEEEDBAAAAAACK", feedback)
    return feedback
