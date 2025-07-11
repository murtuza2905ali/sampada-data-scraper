# 🏛️ Sampada Portal Automation (Govt. Property Records)

This project automates data scraping from the Sampada government website using Python, Django, and Playwright (or Selenium).  
It handles **automatic login**, **CAPTCHA solving via OCR**, **data extraction**, and **Excel export** — all triggered by a simple HTML form.

---

## 🚀 Features

- 🔐 Auto-login to the Sampada government portal
- 🤖 CAPTCHA solved automatically using **Tesseract OCR**
- 📄 Extracts property/ownership details of **100+ entries**
- 📦 Saves scraped data into a structured Excel file
- 🖱️ Triggered via a simple web interface (`form.html`)

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Django** (Web framework)
- **Selenium** or **Playwright** (Browser automation)
- **Tesseract OCR** (For CAPTCHA recognition)
- **Pandas** (For Excel generation)
- **HTML/CSS** (For frontend form)
---

## ⚙️ Setup Instructions

### 1. 🔽 Clone the Repository

```bash
git clone https://github.com/your-username/sampada-automation.git
cd sampada-automation
2. 📦 Install Python Dependencies
```bash
pip install django selenium pillow pytesseract pandas openpyxl

3. 🧠 Install Tesseract OCR
Download and install Tesseract OCR:

Windows Path (Example):

C:\Program Files\Tesseract-OCR\tesseract.exe
Make sure you update your script with the correct path:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
▶️ Running the Project
1. Start the Django Server
python manage.py runserver
2. Trigger the Scraping Process
Open the browser and visit:

http://127.0.0.1:8000/myapp/trigger-scrape/
Enter your login ID in the form

Click the Scrape button

The automation will:

Login to the Sampada portal

Solve the CAPTCHA

Fetch 100+ property records

Save them to sampada_data.xlsx

📁 Output
An Excel file named sampada_data.xlsx is generated with the extracted property data.

❗ Notes
ChromeDriver or Playwright must be installed and compatible with your Chrome version.

Internet connection is required to access the Sampada website.

Use for educational or permitted purposes only.

🧑‍💻 Author
Murtuza Ali
Automation Developer | Data Analyst
GitHub: @murtuza2905ali

📜 Disclaimer
This project is for educational purposes only. Unauthorized scraping of government websites may violate terms of service or legal policies. Use responsibly.



