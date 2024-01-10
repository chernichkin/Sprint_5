from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestExitFromProfile:
    def test_exit_from_profile_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_LOG).send_keys("chernichkin_4@yandex.ru")
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD_LOG).send_keys("111111")
        driver.find_element(By.XPATH, Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_MAIN)))
        driver.find_element(By.XPATH, Locators.PROFILE).click()
        WebDriverWait(driver, 6).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_EXIT)))
        driver.find_element(By.XPATH, Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_LOGIN)))
        text_button = driver.find_element(By.XPATH, Locators.BUTTON_LOGIN).text

        assert text_button == "Войти"

        driver.quit()


TestExitFromProfile().test_exit_from_profile_true()