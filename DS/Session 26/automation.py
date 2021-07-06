from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(1)

# driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
element1 = driver.find_element_by_name("q")
element1.send_keys("harry potter")
time.sleep(1)
element1.send_keys(Keys.ESCAPE)
# element1.click()
time.sleep(1)
# element1.send_keys(Keys.ENTER)
# element2 = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
# element2.send_keys("hsakha")
# element2.click()
driver.execute_script("document.getElementsByName('btnK')[0].click();")
time.sleep(2)

driver.save_screenshot("./search.png")
"""
with open("harry_potter_search.html", "w") as f:
    f.write(driver.page_source)
OR
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source)
soup.find_all()....
"""
driver.close()