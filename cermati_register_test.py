from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    # 1. Open the registration page
    driver.get("https://www.cermati.com/gabung")

    # 2. Fill in required fields (positive test case)
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("dummyemail123@gmail.com")
    driver.find_element(By.NAME, "mobilePhone").send_keys("81234567890")
    driver.find_element(By.NAME, "fullName").send_keys("Dandy Purwanto")
    driver.find_element(By.NAME, "password").send_keys("SecurePass123!")
    driver.find_element(By.NAME, "confirmPassword").send_keys("SecurePass123!")
    driver.find_element(By.NAME, "kota").click()

    # Select Jakarta (assuming dropdown loads options)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'KOTA JAKARTA')]"))).click()

    # Accept Terms & Conditions
    driver.find_element(By.CLASS_NAME, "checkbox__box").click()

    # Submit the form
    driver.find_element(By.XPATH, "//button[contains(text(), 'Daftar')]").click()

    # Optional: Wait for response / dashboard
    time.sleep(5)

    print("Form submitted successfully (check email/phone verification manually).")

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
