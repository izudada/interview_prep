import streamlit as st


class Stylesheet:

    @classmethod
    def card_selector(cls):
        box_shadow = "box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"

        return f"border-radius: 15px; width: 90%; {box_shadow}"
