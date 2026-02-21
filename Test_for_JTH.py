import csv

# Assuming form submissions are stored as a list of dictionaries
form_submissions = []

# Your existing code to handle form submissions goes here

# Function to collect data and write to CSV

def write_to_csv(data):
    with open('form_submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Assuming data is a dictionary
        # Write headers only if the file is empty
        is_empty = file.tell() == 0
        if is_empty:
            writer.writerow(data.keys())
        writer.writerow(data.values())

# Call this function where you handle form submissions
def handle_form_submission(form_data):
    form_submissions.append(form_data)
    write_to_csv(form_data)