import streamlit as st
import pandas as pd
from send_to_email import send_email


with open("topics.csv") as db_file:
    db = pd.read_csv(db_file)
    options = db["topic"]


st.title("Contact Us")
st.write("Please fill out the form below to send me a message.")

with st.form(key="contact_form"):
    sender_email = st.text_input("Your email")
    selected_topic = st.selectbox("Choose a topic", options)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {sender_email} 

From: {sender_email}
Topic: {selected_topic}
{raw_message}

"""
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        send_email(message)
        st.success("Your message has been sent successfully!")
