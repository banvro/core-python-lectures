import streamlit as st   

st.title("This is my first website..")

st.header("This is a header..")

st.subheader("This is my subheader..")

st.text("Python is a good language and the best programming lanague.")

st.write("Python is a good language and the best programming lanague. i learn python from programography.. heyyyy! Python is a good language and the best programming lanague. i learn python from programography..!   ")


st.markdown('''
            # this is single hash
            ## i used 2 hases
            ### i used 3 hashes
            **heyyyyy**
            *Python* is a good programming lanabgue.
            
            > My Prorgamming languages
            - Python
            - Java
            - Javascript
            - Ruby
            
            [Go to Programography](https://programography.com)
            
            ![heyy](https://picsum.photos/200/300?random=1)
            
            ''')


st.code("""
        a = 10
        b = 20
        c = a + b
        print("the sum of a and b is :", a + b)
        """)

st.latex(r'''
         \left( \begin{array}{cc} 2\tau & 7\phi-frac5{12} \\
3\psi & \frac{\pi}8 \end{array} \right)
\left( \begin{array}{c} x \\ y \end{array} \right)
\mbox{~and~} \left[ \begin{array}{cc|r}
3 & 4 & 5 \\ 1 & 3 & 729 \end{array} \right]''')


st.divider()

st.success("This is sucess message...!")

st.warning("This is warnnng...!")

st.error("this is error")

# st.balloons()

st.snow()

st.badge("This is new")

st.toast("This is new notification..")


