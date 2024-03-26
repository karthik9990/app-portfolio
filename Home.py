import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("KARTHIK TADAKAPALLI")
    content1 = """
    Hello, 
    
    This is Karthik Tadakapalli, I am a Python Programmer and software Engineer by trade. 
    I graduated in 2014 from Lambton college in Web Technology and Web Design. 
    I have worked with companies from various provinces in canada such as 
    Saskatchewan health authority and eHealth Saskatchewan
    
    Known Languages:
    
    **English**,
    **Hindi** and 
    **Telugu**
    
    Education: 
    
        •Information Technology of Arts and technology, Lambton College, Canada – 2013 - 2014.
        •Bachelor of Technology in Computer science, JNTU, India – 2008 – 2012.

    Some of the Skills acquired over the years:
    
    1. **Python Programming**: Proficiency in Python, with knowledge of multiple Python versions and the ability to 
    write clean and efficient code.
    
    2. **Frameworks**: Experience with Python frameworks such as Django, Flask, and Pyramid.
    
    3. **Libraries**: Familiarity with Python libraries like NumPy, Pandas, Matplotlib for data manipulation and analysis.
    
    4. **Database Knowledge**: Experience with SQL and NoSQL databases, and Python libraries for database access like 
    SQLAlchemy and PyMongo.
    
    5. **Web Technologies**: Understanding of front-end technologies (HTML, CSS, JavaScript) and RESTful APIs.
    
    6. **Version Control/Git**: Experience with version control systems, particularly Git.
    
    7. **Testing**: Ability to write unit tests and use testing frameworks like PyTest.
    
    8. **Problem-Solving Skills**: Strong logical thinking and problem-solving skills.
    
    9. **Data Science Tools**: Experience with data science tools and libraries such as Scikit-learn, TensorFlow, 
    or Keras is a plus for roles involving data analysis or machine learning.
    
    10. **DevOps Tools**: Familiarity with DevOps practices and tools like Docker and Jenkins can be beneficial.
    
    Soft Skills:
    
    **Communication Skills**
    
    **Problem-Solving Skills**
    
    **Creativity and Innovation**
    
    **Leadership Skills**
    
    **Time Management**
    """

    st.info(content1)
content2 = """Below you can find some of the apps I Have built in Python. 
Feel Free to contact me!"""

st.write(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

