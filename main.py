import streamlit as st

# st.title("Hi, I am turtle code")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is a text")

# st.markdown("# Turtle code")
# st.markdown("## Turtle code")
# st.markdown("**Turtle** code")
# st.markdown("*Turtle* code")
# st.markdown(">Turtle code")
# st.markdown("1. Item one\n 2. Item two\n 3. Item three")

# code_string = "print('Hello world!')"
# st.code(code_string)
# st.markdown("---")
# st.markdown("[Google](https://www.google.com)")

# mk_table  = """
#     | Syntax | Description |
#     | ----------- | ----------- |
#     | Header | Title |
#     | Paragraph | Text |
# """
# st.markdown(mk_table)

# mk_image = ("![alt text](https://res.cloudinary.com/dro7pyxba/image/upload/v1674212920/my_portfolio/DSC_2263_se97xu.jpg)")
# # st.markdown(mk_image)

# mk_json = {"name": "Anthony", "age": "12", "country": "Japan"}
# st.json(mk_json)

st.metric(
    label="Min Speed",
    value="70ms",
    delta="-2.9"
)
st.metric(
    label="Max Speed",
    value="140ms",
    delta="4.9"
)

emoji_sentence = "That is so funny! :joy:"
st.markdown(emoji_sentence)