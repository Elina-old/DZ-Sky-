from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
sleep(2)

search_box = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
search_box.send_keys("Кнопка")
sleep(5)

search_box.send_keys(Keys.RETURN)

driver.quit()
