import streamlit as st
import csv

# Title
st.title("Just the Heart")

# Company description
st.write("Welcome to Just the Heart! We provide insights and services to help individuals focus on their health and well-being.")

# Inquiry form
st.header("Inquiry Form")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Submit"):
    with open('inquiries.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])
    st.success("Your inquiry has been submitted!")
