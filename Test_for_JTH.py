import streamlit as st
import pandas as pd

# Set the title of the app
st.title('Just the Heart')

# Company description blurb
st.write('Welcome to Just the Heart, where we provide services to enhance your heart health and wellbeing. Our mission is to empower individuals to take control of their heart health through knowledge and the right resources.')

# Create a form for user input
with st.form(key='submission_form'):
    full_name = st.text_input('Full Name')
    email = st.text_input('Email')
    phone = st.text_input('Phone')
    company = st.text_input('Company')
    services = st.multiselect('Services', ['Cardiology', 'Nutrition', 'Exercise Training', 'Stress Management'])
    submit_button = st.submit_button('Submit')

# Logic for handling the submission
if submit_button:
    # Store submissions in a DataFrame
    data = {'Full Name': [full_name], 'Email': [email], 'Phone': [phone], 'Company': [company], 'Services': [', '.join(services)]}
    df = pd.DataFrame(data)
    df.to_excel('submissions.xlsx', index=False)
    st.success('Your submission has been recorded!')
    st.download_button('Download Submissions', data=open('submissions.xlsx', 'rb'), file_name='submissions.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
# Run the app using streamlit run Test_for_JTH.py
