from locust import HttpUser, task, between
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Simulate user wait time between requests (1 to 5 seconds)

    @task
    def login(self):
        service = EdgeService(executable_path="C:/Program Files/Webdriver/msedgedriver.exe")
        options = webdriver.EdgeOptions()
        temp_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Edge(service=service, options=options)

        try:
            driver.get("http://localhost:3000")

            # Locate elements
            username_input = driver.find_element(By.ID, "username")
            password_input = driver.find_element(By.ID, "password")
            login_button = driver.find_element(By.ID, "login-button")

            # Input valid credentials
            username_input.send_keys("testuser")
            password_input.send_keys("testpass")
            login_button.click()

            # Validate success message
            success_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "success-message"))
            )
            assert success_message.text == "Login successful", "Expected 'Login successful' message not found."
        finally:
            driver.quit()

    @task
    def invalid_login(self):
        service = EdgeService(executable_path="C:/Program Files/Webdriver/msedgedriver.exe")
        options = webdriver.EdgeOptions()
        temp_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Edge(service=service, options=options)

        try:
            driver.get("http://localhost:3000")

            # Locate elements
            username_input = driver.find_element(By.ID, "username")
            password_input = driver.find_element(By.ID, "password")
            login_button = driver.find_element(By.ID, "login-button")

            # Input invalid credentials
            username_input.send_keys("wronguser")
            password_input.send_keys("wrongpass")
            login_button.click()

            # Validate error message
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "error-message"))
            )
            assert error_message.text == "Invalid username or password", "Expected invalid login message not found."
        finally:
            driver.quit()
