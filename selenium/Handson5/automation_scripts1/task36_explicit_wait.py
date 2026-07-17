from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Autoclosable Success Message')]")
    )
)

button.click()

alert = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
)

print(alert.text)

assert "success" in alert.text.lower()

print("Task 36 Completed Successfully")

driver.quit()