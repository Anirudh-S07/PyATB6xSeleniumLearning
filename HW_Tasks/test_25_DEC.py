from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

"""

// Locators - Find the Web elements

// Open the URL https://app.vwo.com/#/login

// Find the Email id** and enter the email as admin@admin.com

// Find the Pass inputbox** and enter passwrod as admin.

// Find and Click on the submit button

// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_

"""


def test_25_dec_vwo():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")

    """
    <input type="email" 
    class="text-input W(100%)" 
    name="username" 
    vwo-html-translate-attr="placeholder" 
    vwo-html-translate-placeholder="login:enterEmailID" 
    id="login-username" 
    data-qa="hocewoqisi" 
    placeholder="Enter email ID">
    """
    email_address_textbox_element = driver.find_element(By.ID, "login-username")
    email_address_textbox_element.send_keys("admin@admin.com")

    """
    <input type="password" 
    class="text-input W(100%)" 
    vwo-html-translate-attr="placeholder" 
    vwo-html-translate-placeholder="login:enterPassword" 
    name="password" 
    id="login-password" 
    data-qa="jobodapuxe" 
    placeholder="Enter password">
    """
    password_textbox_element = driver.find_element(By.ID, "login-password")
    password_textbox_element.send_keys("passwrod")

    """
   <button type="submit" 
   id="js-login-btn" 
   class="btn btn--primary btn--inverted W(100%) Mb(8px) Mb(0):lc" 
   onclick="login.login(event)" data-qa="sibequkica"> 
   <span class="icon loader hidden" data-qa="zuyezasugu"></span> 
   <span data-qa="ezazsuguuy" vwo-html-translate="login:signIn">Sign in</span> </button>
    """
    login_button_element = driver.find_element(By.ID, "js-login-btn")
    login_button_element.click()
    time.sleep(2)

    """
    <div class="notification-box-description" 
    id="js-notification-box-msg" 
    data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    """
    error_message_element = driver.find_element(By.XPATH, "//div[@data-qa='rixawilomi']")
    assert "Your email, password, IP address or location did not match" == error_message_element.text
    driver.quit()
