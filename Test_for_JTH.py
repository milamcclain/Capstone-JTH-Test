import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
from datetime import datetime
import os

# Title of the web app
st.title('Service Inquiry Form')

# Function to save submissions to a CSV file
def save_to_csv(data):
    file_exists = os.path.isfile('submissions.csv')
    with open('submissions.csv', mode='a', newline='') as file:
        fieldnames = ['Timestamp', 'Full Name', 'Email Address', 'Phone Number', 'Company/Organization', 'Selected Services']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Write header if file doesn't exist
        writer.writerow(data)

# Function to send confirmation email
def send_email(email_address):
    msg = MIMEMultipart()
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = email_address
    msg['Subject'] = 'Confirmation of Your Inquiry'
    body = 'Thank you for your inquiry! We will get back to you soon.'
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail(msg['From'], msg['To'], msg.as_string())

# Form for the inquiry
with st.form(key='inquiry_form'):
    full_name = st.text_input('Full Name')
    email_address = st.text_input('Email Address')
    phone_number = st.text_input('Phone Number')
    company_organization = st.text_input('Company/Organization')
    services = st.multiselect('Select Services', ['Marketing', 'Strategy', 'Technology', 'Design', 'Trainings'])
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Gather data
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'Timestamp': timestamp,
            'Full Name': full_name,
            'Email Address': email_address,
            'Phone Number': phone_number,
            'Company/Organization': company_organization,
            'Selected Services': ', '.join(services)
        }
        try:
            # Save to CSV and send email
            save_to_csv(data)
            send_email(email_address)
            st.success('Your inquiry has been submitted successfully!')
        except Exception as e:
            st.error('An error occurred: ' + str(e))