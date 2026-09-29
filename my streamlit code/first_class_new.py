import streamlit as st

f_name = st.text_input("First Name", max_chars = 10, 
              placeholder = "Enter your first name..", 
              help = "Enter minium 5 cahrcter")

btn = st.button("Submit", type = "primary")

if btn:
    st.subheader(f"User name is : {f_name}")
    st.balloons()