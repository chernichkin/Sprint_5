import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture() #запускаем перед каждым тестом
def open_cite():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    return open_cite