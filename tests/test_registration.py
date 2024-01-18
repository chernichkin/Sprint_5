from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from use_data import UsersData

#Ошибка при входе

#Успешный логин
class TestRegistration:
    def test_registration_is_true(self, driver):

        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.LINK_REGISTRATION))
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_REGISTRATION)))
        driver.find_element(*Locators.INPUT_NAME).send_keys(UsersData.USERNAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UsersData.randomEmail)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UsersData.USERPASSWORD)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_LOGIN)))
        text_button = driver.find_element(*Locators.BUTTON_LOGIN).text

        assert text_button == 'Войти'

    def test_registration_is_false_with_bad_password(self, driver):

        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.LINK_REGISTRATION)))
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_REGISTRATION)))
        driver.find_element(*Locators.INPUT_NAME).send_keys(UsersData.USERNAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UsersData.randomEmail)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UsersData.WRONGPASSWORD)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.TEXT_INPUT_ERROR)))
        text_button = driver.find_element(*Locators.TEXT_INPUT_ERROR).text

        assert text_button == 'Некорректный пароль'
