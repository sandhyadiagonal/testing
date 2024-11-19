import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile

@pytest.fixture
def driver():
    # Set up Firefox WebDriver with the correct path
    service = FirefoxService(executable_path="/usr/local/bin/geckodriver")
    options = webdriver.FirefoxOptions()

    # Use a temporary directory for user data to avoid conflicts
    temp_dir = tempfile.mkdtemp()
    options.set_preference("profile", temp_dir)

    # Run in headless mode for environments without display capabilities
    options.add_argument("--headless")

    # Initialize the WebDriver
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("http://localhost:3000")  # URL for the running React app
    yield driver
    driver.quit()

def test_successful_login(driver):
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "username")))

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("testuser")
    password_input.send_keys("testpass")
    login_button.click()

    success_message = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "success-message"))
    )
    assert success_message.text == "Login successful", "Expected 'Login successful' message not found."

def test_invalid_login(driver):
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "username")))

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("wronguser")
    password_input.send_keys("wrongpass")
    login_button.click()

    error_message = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "error-message"))
    )
    assert error_message.text == "Invalid username or password", "Expected 'Invalid username or password' message not found."

# def test_empty_username(driver):
#     WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "username")))

#     password_input = driver.find_element(By.ID, "password")
#     login_button = driver.find_element(By.ID, "login-button")

#     password_input.send_keys("testpass")
#     login_button.click()

#     error_message = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, "error-message"))
#     )
#     assert error_message.text == "Invalid username or password", "Expected 'Invalid username or password' message not found."

# def test_empty_password(driver):
#     WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "username")))

#     username_input = driver.find_element(By.ID, "username")
#     login_button = driver.find_element(By.ID, "login-button")

#     username_input.send_keys("testuser")
#     login_button.click()

#     error_message = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, "error-message"))
#     )
#     assert error_message.text == "Inavalid username or password", "Expected 'Invalid username or password' message not found."

# def test_empty_username_and_password(driver):
#     WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "username")))

#     login_button = driver.find_element(By.ID, "login-button")
#     login_button.click()

#     error_message = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, "error-message"))
#     )
#     assert error_message.text == "Invalid username or password", "Expected 'Invalid username or password' message not found."
