from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(r"C:\Users\dilip\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://discord.com/channels/688852585071116289/1059941605110468668")
driver.implicitly_wait(60)

event_link = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'https://events.mlh.io/events/')]"))
)
event_link.click()

time.sleep(15)
print(driver.title)
driver.quit()
