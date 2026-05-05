import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    # Initialize Edge WebDriver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")  # ✅ fixed URL
    yield driver
    driver.quit()


def test_simple_js_alert(driver):
    # Click the "Click for JS Alert" button
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    # Switch to alert
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert", "Alert text mismatch"

    # Accept the alert
    alert.accept()
    time.sleep(3)
    # Optional: wait briefly to observe
    time.sleep(3)

    # Verify result text on page
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You successfully clicked an alert", "Result message mismatch"




def test_simple_js_confirmdismiss(driver):
    # Click the "Click for JS Alert" button
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    # Switch to alert
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", "Alert text mismatch"
    time.sleep(3)
    # Accept the alert
    alert.dismiss()

    # Optional: wait briefly to observe
    time.sleep(3)

    # Verify result text on page
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You clicked: Cancel", "Result text was wrong"



def test_simple_js_ok(driver):
    # Click the "Click for JS Alert" button
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    # Switch to alert
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", "Alert text mismatch"
    time.sleep(3)
    # Accept the alert
    alert.accept()

    # Optional: wait briefly to observe
    time.sleep(3)

    # Verify result text on page
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You clicked: Ok", "Result text was wrong"


def test_simple_js_prompt(driver):
    # Click the "Click for JS Prompt" button
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

    # Switch to alert
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt", "Alert text mismatch"  # ✅ fixed capitalization

    # Send input to the prompt
    alert.send_keys("Python Selenium")
    alert.accept()

    # Verify result text on page
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You entered: Python Selenium", "Result"