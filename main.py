from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import requests


def website_exists(url):
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(5)
    driver = browser

    # Set the timeout to 10 seconds
    timeout = 5

    try:
        # Load the website
        driver.get(url)

        # Wait until the page has loaded
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "next-error-h1"))
        )

        print("Website not exists")
        return False
    except TimeoutException:
        print("Website exists")
        # If a TimeoutException is thrown, the website does not exist
        return True
    finally:
        # Clean up the webdriver instance
        driver.quit()


events_pages = requests.get("https://api.eventsradar.in/api/events/title/").json()
for event in events_pages:
    print("Checking", event + "...")
    status = website_exists(f"https://eventsradar.in/event/{event}")
    print("Status:", status, "\n\n")
