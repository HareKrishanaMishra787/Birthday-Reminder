##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
my_email = "tarun96968@gmail.com"
my_password= "srcv nbae lpoh fhxd"
# 2. Check if today matches a birthday in the birthdays.csv
# today = (today_month, today_day)
today_tuple = (dt.datetime.now().month,dt.datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day):data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents= contents.replace("[NAME]",birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        conection.login(my_email,my_password)
        conection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")





