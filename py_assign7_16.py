import re

class EmailFinder:

    def __init__(self, text):
        self.text = text

        self.pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

    # Find all email addresses
    def find_emails(self):
        return re.findall(self.pattern, self.text)

    # Validate a single email
    def validate_email(self, email):
        return re.fullmatch(self.pattern, email) is not None


# Sample text
text = """
Student Name: Janhavi Dorge
Department: SOC CSE - SY11
Enrollment No.: ADT25SOCB0496
Email: janasvidorge@gmail.com
Contact No.: 9022980493

Other emails:
support@example.com
student.help@college.co.in
"""

email_finder = EmailFinder(text)

# Find emails
emails = email_finder.find_emails()

print("Emails found:")

for email in emails:
    print(email)

# Validate user input
email = input("\nEnter an email to validate: ")

if email_finder.validate_email(email):
    print("Valid email")
else:
    print("Invalid email")