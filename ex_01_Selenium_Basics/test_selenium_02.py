from selenium import webdriver
import pytest
import allure


@allure.title("Test case to check the title of a web page")
@allure.description("Test case to check the title of a web page")
@pytest.mark.positive
def test_title():
    # path = "C:\Users\Chrome_Driver.exe"
    # driver = webdriver.Chrome(executable_path=path)
    # In selenium 3 we used to give path of chrome driver which we would need to install in our system
    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com/")
    driver.maximize_window()
    assert "TheTestingAcademy" in driver.title
    driver.quit()
