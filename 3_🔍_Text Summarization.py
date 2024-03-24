from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Text Summarization🔍")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = "Write 'Summarize the text:' first" 

input = st.text_area(
    "Input",
    label_visibility=st.session_state.visibility,
    disabled=st.session_state.disabled,
    placeholder=st.session_state.placeholder,
)

submit=st.button("Summarize")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Summary")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("Text Input")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    



    

