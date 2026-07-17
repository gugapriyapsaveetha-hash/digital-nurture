from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

# Task 28
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
assert "simple-form-demo" in driver.current_url
print("Task 28 Passed")

driver.back()

# Task 29
driver.execute_script('window.open("https://www.google.com");')

print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

print(driver.title)

# Task 30
driver.switch_to.window(driver.window_handles[0])

driver.save_screenshot("playground_screenshot.png")

print("Screenshot saved successfully")

print(driver.get_window_size())

driver.set_window_size(1280, 800)

print(driver.get_window_size())

driver.quit()