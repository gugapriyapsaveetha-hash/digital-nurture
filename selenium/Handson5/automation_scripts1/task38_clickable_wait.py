from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

wait = WebDriverWait(driver, 10)

button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Autoclosable Success Message')]")
    )
)

button.click()

print("Button clicked successfully using element_to_be_clickable()")

driver.quit()