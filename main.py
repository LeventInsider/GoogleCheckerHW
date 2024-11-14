from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Set up the driver
driver = webdriver.Chrome()

# Implicit wait to allow elements to load
driver.implicitly_wait(5)

# Maximize the browser window
driver.maximize_window()

# Navigate to Google
driver.get("https://www.google.com/")

# Assert the element with class "lnXdpd" (adjust as needed for the specific Google page you're using)
try:
    element = driver.find_element(By.CLASS_NAME, "zambaks")
    assert element.is_displayed()  # Check if the element is visible
    print("Element found and is visible.")
except AssertionError:
    print("Element with class 'lnXdpd' not found or not visible.")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser after the test
driver.quit()
