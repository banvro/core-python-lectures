import streamlit as st 

st.header("Learn input fields")

username = st.text_input("Enter your Name", max_chars = 20, value = "naresh_01",
                         help = "Enter a vaild and unique username..",
                         autocomplete = "email")

password = st.text_input("Enter your password", type = "password",
                         placeholder = "Enter a strong password..."
                         )

email = st.text_input("Enter your email id", disabled = True, value = "prorgramography@gmail.com")


btn = st.button("Submit")

if btn:
    st.subheader("Button Clicked!!")
    st.text(f"Username is : {username}")