import streamlit as st

# Baca file HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Tampilkan di Streamlit
st.components.v1.html(html_code, height=400, scrolling=True)
