# Building a Q&A chat bot

from langchain_google_genai import ChatGoogleGenerativeAI
from new_secret_key import google_api_key
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

# Function to load gemini pro model and get responses

def get_geminipro_response(question):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5, google_api_key=os.getenv("GOOGLE_API_KEY"))
    response = llm.predict(question)
    return response
    

# Initialize the Streamlit App
    
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")
input = st.text_input("What is your Query : ", key = 'input')
submit = st.button("Ask the Question")

response = get_geminipro_response(input)

# If as button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)

