from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument('--headless')

# Set up headless options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")  

phone_number = "+16143698703"
message = "DansDeals HURRY appeared: dansdeals.com"

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
        # Sending the WhatsApp Message
        # pywhatkit.sendwhatmsg_instantly(phone_number, message, 10, tab_close=True)
        # # Displaying a Success Message
        # print("WhatsApp message sent!")
        print("The word 'hurry' was found on the page!")
    else:
        print("The word 'hurry' was not found on the page.")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
