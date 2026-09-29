import streamlit as st

st.set_page_config(layout = "wide")

st.title("This is :red[my first] web application..")

st.header("this is header :blue[smaller] then title..")

st.subheader("this :orange[is my subheader and smaller] then header..")

st.write("this is an write very samll...")

st.success("This is my success message...")

st.warning("This is my warning message to warn for something..")

st.error("this is my error message.. ")

st.info("this is my info message to show information..")

st.code("Please copy this token code : 912939823")

st.code("""
        # adding two numbers
        
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        
        zx = num1 + num2
        
        print(f"the sum of {num1} and {num2} is : {zx})
        """)

st.text("""
        Name : Naresh
        Age : 25
        Contact : 8219836118""")

st.caption("this is my caption")

# st.write("E = mc^2")

st.latex("E = mc^2")


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


st.markdown("""
            # this is heading
            ## this is single haashh
            ### this is samller then double hash
            
            this is a **car this** is a *nice car*
            
            [Go to Programography](https://programography.com/)
            
            ![myimg](https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_960_720.jpg)
            """)