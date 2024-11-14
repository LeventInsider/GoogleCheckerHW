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

# Assert the element with class "lnXdpd" should NOT be found (test should fail if element is found)
try:
    element = driver.find_element(By.CLASS_NAME, "zambak")
    # If the element is found, assert False to fail the test
    assert not element.is_displayed()  # This will fail if the element is visible
    print("Test passed: Element should not be visible, and it is not.")
except AssertionError:
    print("Test failed: Element with class 'lnXdpd' is visible as expected.")
except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser after the test
driver.quit()
