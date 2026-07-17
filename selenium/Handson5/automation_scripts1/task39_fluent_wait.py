from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

row = wait.until(
    lambda d: d.find_element(By.XPATH, "//table[@id='example']/tbody/tr[1]")
)

print("First Table Row:")
print(row.text)

driver.quit()