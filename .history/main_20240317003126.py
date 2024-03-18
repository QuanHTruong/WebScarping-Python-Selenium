from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# https://sites.google.com/chronium.org/driver/ 

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(10)

driver.quit