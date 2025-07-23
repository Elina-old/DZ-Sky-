from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://uitestingplayground.com/textinput")

WebDriverWait(driver, 20)
search_box = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_box.send_keys("SkyPro")

WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
).click()


success_message = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(success_message)