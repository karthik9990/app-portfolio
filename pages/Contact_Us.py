import streamlit as st
from send_email import send_email


st.header("Contact US:")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address:")
    user_message = st.text_area("Message")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}
Message: {user_message}
"""
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(message)
        st.info("Your Email was sent successfully")






