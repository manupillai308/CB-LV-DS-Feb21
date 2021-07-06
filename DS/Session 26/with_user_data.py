from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument(r"--user-data-dir=C:\Users\Manu\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://mail.google.com/mail/u/0/")

driver.maximize_window()
time.sleep(2)
driver.quit()