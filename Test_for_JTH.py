import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.title("Service Inquiry Form")

def send_email(name, email_address, phone, company, services):
    sender_email = "myname@gmail.com"  # Replace with your Gmail
    sender_password = "abcd efgh ijkl mnop"  # The 16-character App Password
    
    # Create email content
    subject = "Service Inquiry Submission"
    body = f"""
    Hello,

    Thank you for your inquiry. Here are your submission details:

    Full Name: {name}
    Email Address: {email_address}
    Phone Number: {phone}
    Company/Organization: {company}
    
    Selected Services:
    {chr(10).join([f'• {service}' for service in services])}
    
    Best regards,
    Your Company
    """
    
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email_address
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    # Send email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email_address, message.as_string())
        server.quit()
        return True
    except Exception as error:
        st.error(f"✗ Error sending email: {error}")
        return False

# Create form
with st.form("inquiry_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    company = st.text_input("Company/Organization")
    services = st.multiselect("Select Services", ["Service 1", "Service 2", "Service 3"])
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if send_email(name, email, phone, company, services):
            st.success("✓ Email sent successfully!")
        else:
            st.error("Failed to send email. Please try again.")