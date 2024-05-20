from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://demo.applitools.com/')
time.sleep(5)
USERNAME='dummy@email.com'
PASSWORD='dummy'
email = driver.find_element(By.ID, 'username')
email.send_keys(USERNAME)
password = driver.find_element(By.ID, 'password')
password.send_keys(PASSWORD)

sign_in = driver.find_element(By.ID, 'log-in')
sign_in.click()

time.sleep(10)