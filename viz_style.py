import streamlit as st


def load_local_css(path=".streamlit/custom.css", max_width="960px"):
    with open(path, "r") as f:
        css = f.read().replace("{{MAX_WIDTH}}", max_width)
        # css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)