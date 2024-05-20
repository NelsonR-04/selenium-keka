from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

USERNAME='nelson.rondon@nulogic.io'
PASSWORD='Somewhereibelong1'

driver = webdriver.Chrome()
driver.get('https://nutech.keka.com/')
time.sleep(5)

google_sign_in_btn = driver.find_elements(By.CLASS_NAME, 'login-button')
google_sign_in_btn[0].click()
time.sleep(5)

email = driver.find_element(By.CSS_SELECTOR, "input[name='identifier'][type='email']")
email.send_keys(USERNAME)
email.send_keys(Keys.ENTER)
time.sleep(5)

password = driver.find_element(By.CSS_SELECTOR, "input[name='Passwd'][type='password']")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(20)

clock_in = driver.find_element(By.XPATH, 'div>button')
clock_in.click()
confirm_btn_modal  = driver.find_element()