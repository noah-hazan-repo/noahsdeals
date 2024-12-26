from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email
def send_email(subject, body):
    sender_email = "noahhazan1@gmail.com"
    receiver_email = "noahhazan1@gmail.com"
    password = "bewa fdqu emaw mxrs"  # Use your email password or an app-specific password

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Establish the connection to the email server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()  # Close the connection
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Set up the headless browser
chrome_options = Options()
chrome_options.add_argument('--headless')

# Set up the ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
url = "https://www.dansdeals.com/"
driver.get(url)

# Search for the word "hurry" on the page
try:
    # Get the page source
    page_content = driver.page_source.lower()  # Convert to lowercase for case-insensitive search
    
    # Check if the word "hurry" exists
    if "hurry" in page_content:
        subject = "DansDeals HURRY Alert"
        body = "DansDeals HURRY appeared on the website: dansdeals.com"
        send_email(subject, body)  # Send the email when "hurry" is found
        print("The word 'hurry' was found on the page and email sent!")
    else:
        print("The word 'hurry' was not found on the page.")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
