from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(6)

driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary").click()
sleep(5)

#driver.quit()
