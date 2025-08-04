import streamlit as st


def footer_section():
    st.markdown(
        """
        <style>
        .custom-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;`
            padding: 10px 30px;
            font-size: 13pt;
            border-top: 1px solid #ccc;
            z-index: 9999;
        }
        </style>

        <div class='custom-footer'>
            <p style='font-size: 15pt; margin-bottom: 5px;'>How to use:</p>
            <ol style='margin: 0; padding-left: 20px;'>
                <li>Select your preferred interviewer feedback style</li> 
                <li>Click "Generate Interview Question" to get a random question</li> 
                <li>Type your answer in the text area</li>
                <li>Submit to receive personalized feedback based on your chosen style</li>
                <li>Continue with more questions or start over</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )
