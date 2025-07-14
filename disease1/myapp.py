import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ API key not loaded from .env. Check the file name and contents.")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # or remove if using OpenAI directly
)

def diseasedetectorllm(prompt):
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": "You are a health assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

st.title("🧬 AI Disease Assistant")

user_input = st.text_input("Ask me anything about health or weather:")

if st.button("Get Advice"):
    if user_input:
        with st.spinner("Thinking..."):
            result = diseasedetectorllm(user_input)
            st.markdown(result)
    else:
        st.warning("Please enter a question.")
