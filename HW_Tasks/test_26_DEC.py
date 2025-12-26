from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

"""

// Locators - Find the Web elements

// Open the URL https://www.idrive360.com/enterprise/login

// Find the Email id** and enter the email as augtest_040823@idrive.com

// Find the Pass inputbox** and enter 123456 .

// Find and Click on the sign in button

// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_

"""


def test_26_dec_idrive360():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(10)
    """
    <input _ngcontent-vnr-c171="" 
    type="email" id="username" 
    name="username" autofocus="" 
    class="id-form-ctrl ng-pristine ng-valid ng-touched">
    """
    email_address_textbox_element = driver.find_element(By.ID, "username")
    email_address_textbox_element.send_keys("augtest_040823@idrive.com")

    """
    <input _ngcontent-vnr-c171="" 
    id="password" 
    name="password" 
    tabindex="0" maxlength="20" 
    class="id-form-ctrl ng-pristine ng-valid ng-touched" 
    type="password">
    """
    password_textbox_element = driver.find_element(By.ID, "password")
    password_textbox_element.send_keys("123456")

    """
   <button _ngcontent-vnr-c171="" 
   type="submit" id="frm-btn" 
   class="id-btn id-info-btn-frm">Sign in</button>
    """
    login_button_element = driver.find_element(By.ID, "frm-btn")
    login_button_element.click()
    time.sleep(10)

    """
    <div class="notification-box-description" 
    id="js-notification-box-msg" 
    data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    """
    error_message_element = driver.find_element(By.CLASS_NAME, "id-warning-btn-drk")
    print(error_message_element.text)
    assert "Upgrade Now!" == error_message_element.text

    """
       <div class="notification-box-description" 
       id="js-notification-box-msg" 
       data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    """
    error_message_element2 = driver.find_element(By.ID, "expiredmsg")
    assert "Your free trial has expired!" in error_message_element2.text
    driver.quit()
    