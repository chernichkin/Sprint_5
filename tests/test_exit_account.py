from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from use_data import UsersData

class TestExitFromProfile:
    def test_exit_from_profile_true(self, driver, login):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_MAIN_OFFER))
        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 6).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_EXIT)))
        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_LOGIN)))
        text_button = driver.find_element(*Locators.BUTTON_LOGIN).text

        assert text_button == "Войти"