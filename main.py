import streamlit as st
import pandas as pd

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

# st.metric(
#     label="Min Speed",
#     value="70ms",
#     delta="-2.9"
# )
# st.metric(
#     label="Max Speed",
#     value="140ms",
#     delta="4.9"
# )

# data_table = {
#     "Colmn 1": [1,2,3,4,5],
#     "Column 2": [6,7,8,9,10]
# }
# st.table(data_table)
# st.dataframe(data_table)


# emoji_sentence = "That is so funny! :joy:"
# st.markdown(emoji_sentence)

# st.image("media/image.jpg", caption="Hero Image",width=500)
# st.audio("media/audio.oga", width=300, start_time=200)
# st.video("media/video.mp4", width=400, start_time=3)

car_brands = [
    "ford", 
    "honda", 
    "toyota", 
    "bugatti", 
    "hyundai", 
    "benz", 
    "mitsubushi",
    "bmw"
]
car = st.text_input("Type a car brand")
button = st.button("Check Availability")


if button:
    if car == "":
        st.write("please enter a valid input")

    elif car.lower() in car_brands:
        st.write("This brand is avilable in our garage")

    elif car.lower() not in car_brands:
        st.write("Sorry... This brand is not avilable in our garage")
