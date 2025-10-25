# Selenium package is used to automate web browser interaction
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
# browser = webdriver.Chrome()
browser.get('https://github.com')
signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

username_field = browser.find_element(By.ID, 'login_field')
username_field.send_keys('shakhzod2000')
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys(password)
password_field.submit()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'shakhzod2000')]")))

# profile_link = browser.find_element(By.CLASS_NAME, 'prc-Truncate-Truncate-A9Wn6')
# link_label = profile_link.get_attribute('innerHTML')
assert 'shakhzod2000' in browser.page_source
print(True)
browser.quit() # closes browser after opening the page
