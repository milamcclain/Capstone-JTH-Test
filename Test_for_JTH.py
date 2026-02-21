import csv

class Form:
    def __init__(self):
        self.data = {}

    def submit(self):
        self.collect_data()
        self.save_to_csv()
        print("Thank you for your submission!")

    def collect_data(self):
        # Example: Collect data from a form
        self.data['name'] = input('Enter your name: ')
        self.data['email'] = input('Enter your email: ')

    def save_to_csv(self):
        with open('submissions.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'email'])
            writer.writerow(self.data)

if __name__ == '__main__':
    form = Form()
    form.submit()