from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Users\dilip\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://discord.com/channels/688852585071116289/1059941605110468668")
driver.implicitly_wait(60)

latest_link = driver.find_element(By.XPATH, '//*[@id="message-content-1328589214752833559"]/a/span')  
latest_link.click()

time.sleep(15)
print(driver.title)
driver.quit()
