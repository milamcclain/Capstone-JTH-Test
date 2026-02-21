import streamlit as st

# Set the page configuration
st.set_page_config(page_title='Capstone JTH Test', layout='wide')

# Title with bronze color
st.markdown('<h1 style="color: #cd7f32;">Welcome to the Capstone JTH Test</h1>', unsafe_allow_html=True)

# Header
st.header('Please fill out the form below:')

# Input fields
name = st.text_input('Your Name')
email = st.text_input('Your Email')

# Submit button with hover effect
if st.button('Submit', key='submit'):
    st.write(f'Thank you, {name}! Your email {email} has been submitted.')
else:
    st.markdown('<style>button.stButton:hover {background-color: #cd7f32; color: white;}</style>', unsafe_allow_html=True)