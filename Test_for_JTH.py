import streamlit as st
import csv

st.title("Just the Heart")

st.write("At Just The Heart, LLC, we're an award-winning strategy and creative firm devoted to helping brands with purpose, passion, and measurable results. From data-driven digital marketing and branding to UX design, social media, training, and full-service development solutions, we combine innovation with integrity to elevate your business and connect you with the audiences that matter most. Our team listens, collaborates, and crafts tailored strategies that truly resonate — so you can stand out, grow, and succeed.")

# Creating a form
with st.form("contact_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone_number = st.text_input("Phone Number")
    company = st.text_input("Company/Organization")
    services = st.multiselect("Select Services", ["Marketing", "Strategy", "Technology", "Design", "Trainings"])
    submit_button = st.form_submit_button("Submit")

if submit_button:
    # Save data to CSV with timestamp
    with open('submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([full_name, email, phone_number, company, ', '.join(services), '2026-02-21 02:30:55'])
    st.success("Submission successful!")