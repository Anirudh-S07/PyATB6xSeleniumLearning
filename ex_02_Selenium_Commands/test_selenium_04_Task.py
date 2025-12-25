from selenium import webdriver
import pytest
import allure


@allure.title("To check if 'CURA Healthcare Service' is present in website")
@allure.description("To check if 'CURA Healthcare Service' is present in website")
@pytest.mark.positive
def test_text_in_page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    assert "CURA Healthcare Service" in driver.page_source
    driver.quit()
