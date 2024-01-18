from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from use_data import UsersData

class TestLoginMainPage:
    def test_login_from_main_page_true(self, driver):

        driver.find_element(*Locators.BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UsersData.USEREMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UsersData.USERPASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_MAIN_OFFER))
        text_button_main = driver.find_element(*Locators.BUTTON_MAIN_OFFER).text

        assert text_button_main == 'Оформить заказ'


    def test_login_from_profile_true(self, driver):

        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UsersData.USEREMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UsersData.USERPASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_MAIN_OFFER))
        text_button_main = driver.find_element(*Locators.BUTTON_MAIN_OFFER).text

        assert text_button_main == 'Оформить заказ'

    def test_login_from_registration_form_true(self, driver):

        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_REGISTRATION))
        driver.find_element(*Locators.LINK_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UsersData.USEREMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UsersData.USERPASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_MAIN_OFFER))
        text_button_main = driver.find_element(*Locators.BUTTON_MAIN_OFFER).text

        assert text_button_main == 'Оформить заказ'

    def test_login_from_forgot_password_form_true(self, driver):

        driver.find_element(*Locators.BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.LINK_FORGOT_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_FORGOT))
        driver.find_element(*Locators.LINK_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UsersData.USEREMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UsersData.USERPASSWORD)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_MAIN_OFFER))
        text_button_main = driver.find_element(*Locators.BUTTON_MAIN_OFFER).text

        assert text_button_main == 'Оформить заказ'

#