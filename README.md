Overview:-

This project automates the process of sending personalized birthday emails using Python. It checks a CSV file (birthdays.csv) to identify if today matches any listed birthdays and sends a custom email using pre-written templates. The goal is to simplify the task of remembering and sending birthday greetings.

Features
Automated Birthday Matching: Reads a CSV file containing names, emails, and birth dates to identify birthdays.

Personalized Emails: Uses pre-designed templates to send customized birthday messages.

Email Integration: Sends emails via Gmail SMTP server with secure authentication.

Dynamic Content Replacement: Replaces placeholders in email templates with recipient-specific information.

Files in the Project
1. main.py
This is the main Python script that:

Reads the birthdays.csv file using Pandas.

Checks if today's date matches any birthdays in the file.

Selects a random email template from the letter_templates/ folder.

Sends the email using Gmail's SMTP server.

2. birthdays.csv
A CSV file containing the following columns:

name: Name of the person.

email: Email address of the person.

year: Year of birth (optional).

month: Month of birth.

day: Day of birth.
