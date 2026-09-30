import streamlit as st 

st.title("Learn :red[input fields]")

name = st.text_input("Enter your name..")

age = st.number_input("Enter your age", min_value = 17, max_value = 100, step = 3,
                      help = "ENter your valid age, we your age for valation purpoer.."
                      )

dob = st.date_input("Choose your dae of birth", min_value = "1996-12-12")

lecture_time = st.time_input("Choose your bacth time..")

exam_time = st.datetime_input("Chhose your exam time")

you_voice = st.audio_input("Share your audio.")

# vid = st.camera_input("Record you prfile pic.")

gender = st.selectbox("Choose your gender", ["Male", "Female", "Other"])

cources = st.multiselect("Choose your cources", 
                         ["Python", "Data Scince", "AI", 
                          "Web devlop", "Cloud COmpuing", "Cyber Securyty"]
                         )

enroll = st.radio("Wana enroll in cources", ("Enroll", "Drop", "Padning", "Counsling"))

agree = st.checkbox("Aggere for our terms & condations..")

