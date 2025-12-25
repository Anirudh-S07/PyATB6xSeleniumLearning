from selenium import webdriver
import pytest
import allure


@allure.title("Test case to check the title of a web page")
@allure.description("Test case to check the title of a web page")
@pytest.mark.positive
def test_title():
    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com/")
    driver.maximize_window()
    assert "TheTestingAcademy" in driver.title
    driver.quit()
