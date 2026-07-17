from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

driver.find_element(By.CSS_SELECTOR, "#user-message")
print("CSS Selector by ID")

try:
    driver.find_element(By.CSS_SELECTOR, "input[name='message']")
    print("CSS Selector by Attribute")
except:
    print("CSS Attribute not available on current website")

driver.find_element(By.CSS_SELECTOR, "div input")
print("CSS Selector Parent Child")

driver.quit()