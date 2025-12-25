from selenium import webdriver
import pytest
import allure


@allure.title("Test case to check the title and print thee page source of a web page")
@allure.description("Test case to check the title of a web page and print the page source")
@pytest.mark.positive
def test_title():
    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com/")
    driver.maximize_window()
    assert "TheTestingAcademy" in driver.title
    print(driver.page_source)
    driver.quit()
