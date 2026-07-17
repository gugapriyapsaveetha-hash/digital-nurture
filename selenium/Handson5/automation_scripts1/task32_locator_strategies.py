from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

driver.find_element(By.ID, "user-message")
print("Located using ID")

try:
    driver.find_element(By.NAME, "message")
    print("Located using NAME")
except:
    print("NAME locator not available on current website")

driver.find_element(By.CLASS_NAME, "form-control")
print("Located using CLASS_NAME")

driver.find_element(By.TAG_NAME, "input")
print("Located using TAG_NAME")

driver.find_element(By.XPATH, "//input[@id='user-message']")
print("Located using Relative XPath")

driver.quit()