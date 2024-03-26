import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("KARTHIK TADAKAPALLI")
    content1 = """
    Hello, This is Karthik Tadakapalli, I am a Python Programmer and software Engineer by trade. 
    I graduated in 2014 from Lambton college in Web Technology and Web Design. 
    I have worked with companies from various provinces in canada such as 
    Saskatchewan health authority and eHealth Saskatchewan
    
    Known Languages:
    
    English,
    Hindi and 
    Telugu
    
    Education: 
    
        •Information Technology of Arts and technology, Lambton College, Canada – 2013 - 2014.
        •Bachelor of Technology in Computer science, JNTU, India – 2008 – 2012.

    
    """
    st.info(content1)
content2 = """Below you can find some of the apps I Have built in Python. 
Feel Free to contact me!"""

st.write(content2)


col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

