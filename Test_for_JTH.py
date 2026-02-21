import csv
import streamlit as st
from datetime import datetime

# Streamlit form inputs
def form():
    with st.form(key='contact_form'):
        full_name = st.text_input('Full Name')
        email = st.text_input('Email Address')
        phone_number = st.text_input('Phone Number')
        company = st.text_input('Company/Organization')
        selected_services = st.multiselect(
            'Selected Services',
            ['Marketing', 'Strategy', 'Technology', 'Design', 'Trainings']
        )
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            save_submission(full_name, email, phone_number, company, selected_services)
            st.success('Thank you for your submission!')

# Function to save submissions to CSV using built-in csv module
def save_submission(full_name, email, phone_number, company, selected_services):
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, full_name, email, phone_number, company, selected_services])

if __name__ == '__main__':
    form()