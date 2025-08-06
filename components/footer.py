import streamlit as st

from stylesheets import Stylesheet as style


def footer_section():

    st.markdown(
        f"""
        <style>
        .custom-footer {{
            padding: 20px 30px;
            font-size: 13pt;
            z-index: 9999;
            {style.card_selector()}
        }}
        </style>

        <div class='custom-footer'>
            <p style='font-size: 15pt; font-weight: bold; margin-bottom: 10px;'>How to use:</p>
            <ol style='margin: 0; padding-left: 20px; line-height: 1.6;'>
                <li>Select your preferred interviewer feedback style</li> 
                <li>Click "Generate Interview Question" to get a random question</li> 
                <li>Type your answer in the text area</li>
                <li>Submit to receive personalized feedback based on your chosen style</li>
                <li>Continue with more questions or start over</li>
            </ol>
        </div>""",
        unsafe_allow_html=True
    )
