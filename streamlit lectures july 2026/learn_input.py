import streamlit as st

st.subheader("Learn Number inpput..!")

age = st.number_input("Enter your age", min_value = 20, max_value = 100,
                      step = 5, help = "Enter your age"
                      )

dob = st.datetime_input("This is datetime")

date = st.date_input("This is date")

time = st.time_input("This is date")