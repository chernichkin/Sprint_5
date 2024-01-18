import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from use_data import UsersData
from locators import Locators


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(UsersData.USEREMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UsersData.USERPASSWORD)
    driver.find_element(*Locators.BUTTON_LOGIN).click()