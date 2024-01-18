from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from use_data import UsersData

class TestMoveProfile:
    def test_move_profile_true(self, driver, login):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_MAIN_OFFER))
        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_EXIT)))
        exit_text = driver.find_element(*Locators.BUTTON_EXIT).text

        assert exit_text == "Выход"
