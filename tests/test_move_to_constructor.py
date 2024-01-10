from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestMoveProfile:
    def test_move_profile_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_LOG).send_keys("chernichkin_4@yandex.ru")
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD_LOG).send_keys("111111")
        driver.find_element(By.XPATH, Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_MAIN)))
        driver.find_element(By.XPATH, Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_EXIT)))
        driver.find_element(By.XPATH, Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_MAIN)))
        text_button_main = driver.find_element(By.XPATH, Locators.BUTTON_MAIN).text

        assert text_button_main == 'Оформить заказ'

        driver.quit()

TestMoveProfile().test_move_profile_true()