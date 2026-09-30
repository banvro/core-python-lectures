import streamlit as st 
import pycountry

st.header("Out :red[Contact Us Form]")

# st.image("image.png")

# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.image("image.png")
    
# with col2:
#     st.image("image.png")
    
# with col3:
#     st.image("image.png")
    
# with col4:
#     st.image("image.png")


col1, col2 = st.columns(2)

with col1:
    f_name = st.text_input("Enter your first name ")
    
with col2:
    l_name = st.text_input("Enter your last name")
    
email = st.text_input("Enter your email id")

x, y = st.columns(2)

with x:
    p_number = st.number_input("Enter phone number", step = 10)

with y:
    a_p_number = st.number_input("Enter altranate phone number", step = 10)
    
col1, col2, col3 = st.columns(3)

with col1:
    country = st.selectbox("Chhose your country", 
                           [country.name for country in pycountry.countries]
                           )
    
with col2:
    states = st.selectbox("Chhose your state", ["Punjab", "Ch"])

with col3:
    pin_code = st.number_input("Enter your pin code", step = 1000)
    
message = st.text_area("Enter your query..")

btn = st.button("Submit Query", type = "primary")

if btn:
    
    st.text(f"""
             User first name : {f_name}
             User last name : {l_name}
             email address : {email}
             phone number : {p_number}
             a phone_number : {a_p_number}
             user contry : {country}
             user state : {states}
             pin code : {pin_code}
             message : {message}
             """)
    
    st.balloons()