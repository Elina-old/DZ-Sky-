from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Chrome()

element = WebDriverWait(driver, 10)
driver.get("http://the-internet.herokuapp.com/login")

search_box = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
search_box.send_keys("tomsmith")
sleep(5)

search_box = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
search_box.send_keys("SuperSecretPassword!")
sleep(5)


search_box = driver.find_element(By.CSS_SELECTOR, "button.radius")
search_box.send_keys("Login")
search_box.click()
sleep(5)

print('[alt="Fork me on GitHub"]')