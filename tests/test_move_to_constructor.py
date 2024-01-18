from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from use_data import UsersData

class TestMoveToConstructor:
    def test_move_to_constructor_true(self, driver, login):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_MAIN_OFFER))
        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_EXIT)))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_MAIN_OFFER)))
        text_button_main = driver.find_element(*Locators.BUTTON_MAIN_OFFER).text

        assert text_button_main == 'Оформить заказ'