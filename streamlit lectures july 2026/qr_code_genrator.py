import streamlit as st 
import qrcode
from io import BytesIO

st.set_page_config(layout = "wide")

st.title("Genrate a QR with secret Message")

col1, col2 = st.columns(2)

with col1:
    s_message = st.text_area("Enter your secret message..")

    btn = st.button("Genrate QR Code", type = "primary")

with col2:
    if btn:
        if s_message:
            qr = qrcode.make(s_message)
            
            buffer = BytesIO()
            
            qr.save(buffer, format = "PNG")
            
            st.image(buffer.getvalue(), caption = "scan this image to read a message..")

        else:
            st.error("Please fill somethig before click on button.")
            st.snow()
    
    else:
        st.success("QR comming here..")