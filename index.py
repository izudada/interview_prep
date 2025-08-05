import streamlit as st

from components import footer_section, hero_section


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
    }}

    div[data-testid="stMarkdownContainer"] > p {{
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

hero_section()

footer_section()
