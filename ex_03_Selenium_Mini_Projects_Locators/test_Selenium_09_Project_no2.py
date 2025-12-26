from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

"""
## **Project 2 - Automating by using the Selenium Python. **
1. Navigate to the URL - katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login) 
2. Find the **Make appointment** Button
3. Click on the **Make appointment **Button
4. Next Page will be loaded
5. **Find and Enter wrong details **Username and Password** and **Click** on the Login Button
6. Verify current error message 

"""


def test_project_2_katalon():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # 1- Find the element the anchor tag
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg" >
    # Make Appointment
    # < / a >

    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_element.click()

    """
    <input type="text" 
    class="form-control" 
    id="txt-username" 
    name="username" 
    placeholder="Username" 
    value="" 
    autocomplete="off">
    """
    username_textbox_element = driver.find_element(By.NAME, "username")
    username_textbox_element.send_keys("John")

    """
    <input type="password" 
    class="form-control" 
    id="txt-password" 
    name="password" 
    placeholder="Password" 
    value="" autocomplete="off">
    """
    password_textbox_element = driver.find_element(By.NAME, "password")
    password_textbox_element.send_keys("NotAPassword")

    """
    <button id="btn-login" 
    type="submit" 
    class="btn btn-default">
    Login</button>
    """
    login_button_element = driver.find_element(By.ID, "btn-login")
    login_button_element.click()
    time.sleep(2)

    """
    <p class="lead text-danger">Login failed! Please ensure the username and password are valid.</p>
    since class has lead and text-danger we shouldn't use both rather we should use only one like either lead or text-danger
    """
    error_message_element = driver.find_element(By.CLASS_NAME, "text-danger")
    assert "Login failed! Please ensure the username and password are valid." == error_message_element.text

    driver.quit()



