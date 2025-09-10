import streamlit as st


def toggle():
    # Toggle placed OUTSIDE the form
    dark_mode = st.toggle(
        "🌙 Light Mode" if not st.session_state.get("dark_mode", False) else "☀️ Dark Mode"
    )

    # Apply dark/light theme
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
                display: flex;
                flex-direction: column;
            }}

            div[data-testid="stMarkdownContainer"] > p {{
                color: {text_color};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
