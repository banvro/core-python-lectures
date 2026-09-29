import streamlit as st

st.title("Our :red[Voating System]")

st.caption("Check your voat eligblitly by passing you age..")

age = st.number_input("Enter your age : ", step = 1)

btn = st.button("Check Eligiblity", type = "primary")

if btn:
    
    if age > 18:
        st.success("Grate! You are eligible for vaot..!")
        st.balloons()
    
    elif age == 18:
        st.info("Congratulation!! This is your first voat..!")
        st.balloons()
    
    else: 
        st.error("oops! you are not eligible for voat! best luck next time.")
        st.snow() 