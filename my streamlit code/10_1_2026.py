# Project ----> chatboat

import streamlit as st
from aii import chat
import wikipedia
import webbrowser

st.subheader(":red[Chatly] (AI BOT)")

st.caption("ask any question and get the solution..")

# how to create sesion in streamlit
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []


user_query = st.chat_input("enter your query")

tuning = ["who build you", "chaltly designed by"]

if user_query:
    
    st.session_state.chat_messages.append(("👤", user_query))
    
    if user_query in tuning:
        st.session_state.chat_messages.append(("🎯", "Programography Pvt LTD"))
        
    elif "open youtube" in user_query:
        webbrowser.open("https://youtube.com/")
        
    elif "open programography" in user_query:
        webbrowser.open("https://programography.com/")
        
    elif "open google" in user_query:
        webbrowser.open("https://google.com/")
    
    elif "wikipedia" in user_query:
        cleaned_text = user_query.replace("wikipedia", "").strip()
        res = wikipedia.summary(f"{cleaned_text}", sentences=2)
        st.session_state.chat_messages.append(("🎯", res))
    
    else:
        response = chat.send_message(user_query + " use emojies and funny responces. in hindi")
        
        st.session_state.chat_messages.append(("🎯", response.text))
    

for key, value in st.session_state.chat_messages:
    with st.chat_message(key):
        if key == "👤":
            st.markdown(value)
        
        else:
            st.markdown(value)
