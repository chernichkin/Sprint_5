from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:
    def test_click_for_sauces_true(self, driver):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.STUFFING_SECTION))
        driver.find_element(*Locators.SAUCES_SECTION).click()
        class_parent_sauces = driver.find_element(*Locators.PARENT_SAUCES_SECTION).get_attribute('class')
        assert 'tab_tab_type' in class_parent_sauces

    def test_click_for_buns_true(self, driver):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.STUFFING_SECTION))
        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()
        class_parent_buns = driver.find_element(*Locators.PARENT_BUNS_SECTION).get_attribute('class')
        assert 'tab_tab_type' in class_parent_buns

    def test_click_for_stuffing_true(self, driver):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.STUFFING_SECTION))
        driver.find_element(*Locators.STUFFING_SECTION).click()
        class_parent_staf = driver.find_element(*Locators.PARENT_STAFFING_SECTION).get_attribute('class')
        assert 'tab_tab_type' in class_parent_staf