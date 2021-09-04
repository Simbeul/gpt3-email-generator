import streamlit as st
import openai
from ml_backend import ml_backend

st.title("Convert Python to Natural Language")
st.text("by Simon Bel")

st.markdown(""" 
 
*This app translates python 3 code into natural language so anyone can understand it!*\n   
This project was built to demonstrate the power of the all new *OpenAI Codex*, an AI model that generates program code from natural language descriptions.  

""")

st.markdown("# Convert Python3 to Natural Language")

backend = ml_backend()

with st.form(key="form"):
    prompt = st.text_area("Paste your complicated Python3 code and we'll explain what it means below.")

    submit_button = st.form_submit_button(label='Generate Explanation')

    if submit_button:
        with st.spinner("Generating Explanation..."):
            output = backend.generate_explanation(prompt)
        st.markdown("# Code Explanation:")
        st.subheader(output)