from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
service = Service(executable_path="C://webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Open the URL
    driver.get("https://google.com")

    # Wait for the search box to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Find the search box, clear it, and enter the search query
    input_element = driver.find_element(By.NAME, "q")
    input_element.clear()
    input_element.send_keys("Tech With Tim" + Keys.ENTER)

    # Wait for the search results to load and find the link to click
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
    )
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
    link.click()

    # Additional wait to observe the actions (optional)
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
