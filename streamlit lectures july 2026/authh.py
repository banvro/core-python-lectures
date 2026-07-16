import streamlit as st 

u_name = "naresh"
u_pass = "Naresh@1234"

st.header("Login Here")

username = st.text_input("Enter your username", help = "enter your vaild username", placeholder = "Username..")

password = st.text_input("Enter your password", type = "password", help = "enter a vaild password", placeholder = "Password..")

if st.button("Login"):
    if username == "" or password == "":
        st.warning("Username and password fileds are required!!!")
    
    else:
        if username == u_name:
            if password == u_pass:
                st.success("Login Successfulyy Done..!")
                st.toast("Congratulations.")
                st.balloons()
            
            else:
                st.error("Please Enter valid password...!tray again")
                st.snow()
        else:
            st.error("Please Enter vaild Username to Login!")
            st.snow()