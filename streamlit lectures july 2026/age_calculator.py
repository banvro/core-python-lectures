import streamlit as st
from datetime import datetime

st.subheader("Age Calculaotr")

dob = st.date_input("Choose your Date of Birth",
                    min_value = "2000-12-12", 
            )

btn = st.button("Calculate Age", type = "primary")

if btn:
    st.success(f"User DOB is : {dob}")
    
    st.success(f"You are {datetime.today().year - dob.year} Years, {datetime.today().month - dob.month} months and {datetime.today().day - dob.day} days years old..!")
    
    # new_dob = datetime.strptime(dob, )
    
    # st.write(f"{datetime.today()}")
    
    # st.write(f"{dob.year}")