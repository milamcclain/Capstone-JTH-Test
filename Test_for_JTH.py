from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    send_email(data['name'], data['email'], data['phone'], data['company'], data['services'])
    return jsonify({'status': 'success'})

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
        print("\n✓ Email sent successfully!")
    except Exception as error:
        print(f"\n✗ Error sending email: {error}")

if __name__ == '__main__':
    app.run(debug=True)