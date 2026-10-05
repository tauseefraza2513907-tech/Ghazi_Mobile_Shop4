from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ghazi Mobile Shop | Shorkot, Jhang",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header, menu, footer and padding so only the shop site shows
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0; width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")

# Increase the height number if the bottom of the page is cut off on your phone
components.html(html, height=3000, scrolling=True)
