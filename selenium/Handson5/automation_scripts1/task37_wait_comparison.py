import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

start = time.time()

driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Autoclosable Success Message')]"
).click()

time.sleep(3)

end = time.time()

print("Time using sleep():", round(end - start, 2), "seconds")

driver.refresh()

start = time.time()

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Autoclosable Success Message')]")
    )
)

button.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
)

end = time.time()

print("Time using Explicit Wait:", round(end - start, 2), "seconds")

driver.quit()