from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pytest
import time

# Set up EdgeDriver path
driver_path = "C:/Program Files/Webdriver/msedgedriver.exe"  # Ensure EdgeDriver is in PATH or provide an absolute path if needed
base_url = "file:///C:/Diagonal/Pre-Alpha Multi container/selenium/login.html"  # Use 'file:///' and full path to the local file

@pytest.fixture(scope="module")
def setup_driver():
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_signup(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "new_username").send_keys("testuser")
    driver.find_element(By.ID, "new_password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    time.sleep(5)  # Wait for the alert
    alert = driver.switch_to.alert
    assert "Signup successful!" in alert.text
    alert.accept()

def test_login_success(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)  # Wait for the alert
    alert = driver.switch_to.alert
    assert "Login successful!" in alert.text
    alert.accept()

def test_login_failure(setup_driver):
    driver = setup_driver
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)  # Wait for the alert
    alert = driver.switch_to.alert
    assert "Invalid credentials" in alert.text
    alert.accept()
