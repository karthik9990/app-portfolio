import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("KARTHIK TADAKAPALLI")
    content = """
    Hello, This is Karthik Tadakapalli, I am a Python Programmer and software Engineer by trade. 
    I graduated in 2014 from Lambton college in Web Technology and Web Design. 
    I have worked with companies from various provinces in canada such as 
    Saskatchewan health authority and eHealth Saskatchewan
    """
    st.info(content)