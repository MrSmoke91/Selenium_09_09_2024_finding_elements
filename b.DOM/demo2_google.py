from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()
driver.get('http://www.google.com')
time.sleep(3)

# find the input element for the last element - BY.NAME
web_element = driver.find_element(By.NAME, 'q')
web_element.send_keys("python")
web_element.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
