from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
# from selenium.webdriver.common.action_chains import ActionChains

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the WordPress login page
driver.get("http://44.217.54.127/wp-login.php")


# Find the username field and enter the username
username = driver.find_element(By.ID, "user_login")
username.send_keys("user")

# Find the password field and enter the password
password = driver.find_element(By.ID, "user_pass")
password.send_keys("x:LBlSm4YGuf")

# Find the login button and click it
login_button = driver.find_element(By.ID, "wp-submit")
login_button.click()

driver.get("http://44.217.54.127/activity")

commentBox = driver.find_element(By.ID, "whats-new")
textToCheck = "Hello, I loved your content. Keep up the good work."
commentBox.send_keys(textToCheck)

postUpdateButton = driver.find_element(By.ID, "aw-whats-new-submit")
postUpdateButton.click()

time.sleep(20)
# Close the browser window
driver.quit()