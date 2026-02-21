import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("Just the Heart")

st.write("At Just The Heart, LLC, we're an award-winning strategy and creative firm devoted to helping brands with purpose, passion, and measurable results. From data-driven digital marketing and branding to UX design, social media, training, and full-service development solutions, we combine innovation with integrity to elevate your business and connect you with the audiences that matter most. Our team listens, collaborates, and crafts tailored strategies that truly resonate — so you can stand out, grow, and succeed.")

st.divider()

st.header("Service Inquiry Form")

with st.form(key='service_form'):
    full_name = st.text_input('Full Name')
    email = st.text_input('Email Address')
    phone_number = st.text_input('Phone Number')
    company = st.text_input('Company/Organization')
    services = st.multiselect('What services are you interested in?', ['Marketing', 'Strategy', 'Technology', 'Design', 'Trainings'])
    submit_button = st.form_submit_button(label='Submit Inquiry')

if submit_button:
    if full_name and email and phone_number and company and services:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        new_data = {
            "Timestamp": [timestamp],
            "Full Name": [full_name],
            "Email": [email],
            "Phone": [phone_number],
            "Company": [company],
            "Services": [', '.join(services)]
        }
        new_df = pd.DataFrame(new_data)
        
        if os.path.exists('submissions.xlsx'):
            existing_df = pd.read_excel('submissions.xlsx')
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            combined_df.to_excel('submissions.xlsx', index=False)
        else:
            new_df.to_excel('submissions.xlsx', index=False)
        
        st.success('Thank you for your submission! We will be in touch soon.')
    else:
        st.error('Please fill out all fields.')
