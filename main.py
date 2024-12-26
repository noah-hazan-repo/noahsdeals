from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pywhatkit

phone_number = "+16143698703"
message = "DansDeals HURRY appeared: dansdeals.com"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.dansdeals.com/"
driver.get(url)

try:
    page_content = driver.page_source.lower()
    if "hurry" in page_content:
        pywhatkit.sendwhatmsg_instantly(phone_number, message, 10, tab_close=True)
        print("WhatsApp message sent!")
        print("The word 'hurry' was found on the page!")
    else:
        print("The word 'hurry' was not found on the page.")
except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()
