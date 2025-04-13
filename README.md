# 🎉 Birthday Wisher Bot 🎂

A simple Python automation script that sends personalized birthday wishes via email. Built using `pandas`, `datetime`, and `smtplib`.

## 📌 Features

- 📅 Automatically checks for birthdays every day
- 💌 Sends personalized email greetings to your friends/family
- 📝 Supports customizable letter templates
- 🔐 Email login credentials securely used via environment variables or config file

---

## 📁 Project Structure

```
.
├── birthdays.csv              # List of people and their birthdays
├── main.py                    # Main script to send birthday emails
└── letter_templates/
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

---

## 📦 Requirements

- Python 3.x
- pandas

Install dependencies:

```bash
pip install pandas
```

---

## 🛠 How It Works

1. The script reads `birthdays.csv` to find any matching birthdays for the current day.
2. If a match is found:
   - A random birthday letter template is chosen.
   - The placeholder `[NAME]` is replaced with the recipient's name.
   - An email is sent via Gmail using `smtplib`.

---

## ✍️ Sample CSV Format

```csv
name,email,year,month,day
John Doe,john@example.com,1990,4,13
Jane Smith,jane@example.com,1985,6,22
```

📄 [Click here to view the birthdays.csv file](./birthdays.csv)

---

## 📬 Email Setup

You must enable **"Less secure app access"** or use **App Passwords** in your Gmail account settings.

Update the following in `main.py`:

```python
my_email = "youremail@gmail.com"
my_password = "your_app_password"
```

⚠️ **Important:** Never upload your real credentials to GitHub. Use `.env` or config files and add them to `.gitignore`.

---

## 🤖 Automation Tip

You can schedule this script to run daily using:

- **Windows**: Task Scheduler
- **Mac/Linux**: `cron` job

---

## 🙌 Contribution

Pull requests are welcome! If you’d like to suggest improvements or new features, feel free to open an issue.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Author

**Hare Krishana Mishra**  

