import streamlit as st

# Read your HTML file
with open('Portfolio.html', 'r') as f:
    html_content = f.read()

# Display the HTML
st.components.v1.html(html_content, width=None, height=2000, scrolling=True)
