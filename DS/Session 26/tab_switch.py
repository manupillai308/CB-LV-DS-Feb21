from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://facebook.com")
driver.maximize_window()



# time.sleep(5)
# print("Before Clicking", driver.window_handles)
# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/p[5]/a").click()
# time.sleep(2)
# print("After Clicking", driver.window_handles)
# driver.switch_to_window(driver.window_handles[-1])
# time.sleep(1)
# driver.switch_to_window(driver.window_handles[0])
# time.sleep(1)
# driver.close()



time.sleep(1)
# driver.close()
driver.quit()