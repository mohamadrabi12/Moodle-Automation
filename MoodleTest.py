import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_moodle_login(driver):
    driver.get("https://myofek.cet.ac.il/he")
    # Wait for the login button to be clickable and then click it
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/div[1]/div[1]/button'))
    )
    login_button.click()

    cet_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/div[1]/div[1]/div/div/dialog/div/section/div[2]/button/div'))
    )
    cet_login.click()

    driver.implicitly_wait(6)

    # Wait for the username field to be present and then enter the username
    username = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    username.send_keys("קטיהמורה2")

    # Wait for the password field to be present and then enter the password
    password = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    password.send_keys("Qa123456")

    # Wait for the login button to be clickable and then click it
    login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginButtonText"]'))
    )
    login.click()

    another_time = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/dialog/footer/section[1]/button'))
    )
    another_time.click()

def test_add_task(driver):
    # Navigate directly to the course page
    driver.get("https://mvc.cet.ac.il/course/view.php?id=2623")
    driver.implicitly_wait(10)
    edit_course = driver.find_element(By.XPATH, "//button[text()='עריכה']")
    edit_course.click()
    # Wait for the add activity button to be clickable and then click it
    add_activity = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="section-0"]/div[2]/button/span[2]'))
    )
    add_activity.click()
    # Wait for the add file option to be clickable and then click it
    add_task = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="all-3"]/div/div[14]/div/a/div[1]/img'))
    )
    add_task.click()
    name_of_file = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id_name"]'))
    )
    name_of_file.send_keys("automation_Test_Task")
    conditions_for_completing_an_activity = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="collapseElement-10"]'))
    )
    conditions_for_completing_an_activity.click()
    drop_list_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_completion"]'))
    )
    drop_list_button.click()
    option3 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_completion"]/option[3]'))
    )
    option3.click()
    option2 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_completionusegrade"]'))
    )
    option2.click()
    done = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_submitbutton2"]'))
    )
    done.click()
    # Wait for the task to be present in the DOM
    is_the_task_added = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/header/div/nav/a/span'))
    )
    # Optionally, check if it is displayed
    assert is_the_task_added.is_displayed()

def test_add_task_without_conditions(driver):
    # Navigate directly to the course page
    driver.get("https://mvc.cet.ac.il/course/view.php?id=2623")
    driver.implicitly_wait(10)

    # Wait for the add activity button to be clickable and then click it
    add_activity = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="section-0"]/div[2]/button/span[2]'))
    )
    add_activity.click()
    # Wait for the add file option to be clickable and then click it
    add_task = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="all-3"]/div/div[14]/div/a/div[1]/img'))
    )
    add_task.click()
    name_of_file = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id_name"]'))
    )
    name_of_file.send_keys("automation_Test_Task2")
    conditions_for_completing_an_activity = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="collapseElement-10"]'))
    )
    conditions_for_completing_an_activity.click()
    drop_list_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_completion"]'))
    )
    drop_list_button.click()
    option1 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_completion"]/option[1]'))
    )
    option1.click()
    done = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_submitbutton2"]'))
    )
    done.click()
    # Wait for the task to be present in the DOM
    is_the_task_added = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/header/div/nav/a/span'))
    )
    # Optionally, check if it is displayed
    assert is_the_task_added.is_displayed()

def test_add_designed_page_content(driver):
    # Navigate directly to the course page
    driver.get("https://mvc.cet.ac.il/course/view.php?id=2623")


    # Wait for the add activity button to be clickable and then click it
    add_activity = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="section-0"]/div[2]/button/span[2]'))
    )
    add_activity.click()

    # Wait for the add file option to be clickable and then click it
    add_designed_page = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="all-3"]/div/div[6]/div/a/div[1]/img'))
    )
    add_designed_page.click()

    # Wait for the name of file input field and enter text
    name_of_file = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id_name"]'))
    )
    name_of_file.send_keys("automation_Test_designed_page")

    # Wait for content editable field and input text
    content = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_pageeditable"]'))
    )
    content.click()
    content.send_keys("automation_Test_designed_page_content")

    # Select the entered text
    content.send_keys(Keys.CONTROL + "a")

    # Click the color button and select the red color
    edit_color = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '(//button[@title="צבע הגופן"])[2]'))
    )
    edit_color.click()

    red_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@title="Red"]'))
    )
    red_option.click()
    done = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_submitbutton2"]'))
    )
    done.click()
    # Wait for the task to be present in the DOM
    is_the_task_added = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/header/div/nav/a/span'))
    )
    # Optionally, check if it is displayed
    assert is_the_task_added.is_displayed()
