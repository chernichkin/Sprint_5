from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:
    def test_click_for_sauces_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_LOG).send_keys("chernichkin_4@yandex.ru")
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD_LOG).send_keys("111111")
        driver.find_element(By.XPATH, Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_MAIN)))
        driver.find_element(By.XPATH, Locators.SAUCES_SECTION).click()
        class_parent_sauces = driver.find_element(By.XPATH, Locators.PARENT_SAUCES_SECTION).get_attribute('class')

        assert 'tab_tab_type' in class_parent_sauces

        driver.quit()

    def test_click_for_buns_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_LOG).send_keys("chernichkin_4@yandex.ru")
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD_LOG).send_keys("111111")
        driver.find_element(By.XPATH, Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_MAIN)))
        driver.find_element(By.XPATH, Locators.BUNS_SECTION_SECTION).click()
        class_parent_buns = driver.find_element(By.XPATH, Locators.PARENT_BUNS_SECTION).get_attribute('class')

        assert 'tab_tab_type' in class_parent_buns

        driver.quit()

    def test_click_for_stuffing_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_LOG).send_keys("chernichkin_4@yandex.ru")
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD_LOG).send_keys("111111")
        driver.find_element(By.XPATH, Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_MAIN)))
        driver.find_element(By.XPATH, Locators.STUFFING_SECTION).click()
        class_parent_staf = driver.find_element(By.XPATH, Locators.PARENT_STAFFING_SECTION).get_attribute('class')

        assert 'tab_tab_type' in class_parent_staf

        driver.quit()
