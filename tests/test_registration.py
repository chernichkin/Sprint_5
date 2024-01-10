from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Ошибка при входе

#Успешный логин
class TestRegistration:
    def test_registration_is_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.LINK_REGISTRATION)))
        driver.find_element(By.XPATH, Locators.LINK_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_REGISTRATION)))

        driver.find_element(By.XPATH, Locators.INPUT_NAME).send_keys("Anton")
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_REG).send_keys("anton_chernichkin_4@yandex.ru")
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD_REG).send_keys("123456")

        driver.find_element(By.XPATH, Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_LOGIN)))
        text_button = driver.find_element(By.XPATH, Locators.BUTTON_LOGIN).text

        assert text_button == 'Войти'

        driver.quit()

    def test_registration_is_false_with_bad_password(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.LINK_REGISTRATION)))
        driver.find_element(By.XPATH, Locators.LINK_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.BUTTON_REGISTRATION)))

        driver.find_element(By.XPATH, Locators.INPUT_NAME).send_keys("Anton")
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL_REG).send_keys("anton_chernichkin_41411@yandex.ru")
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD_REG).send_keys("123")

        driver.find_element(By.XPATH, Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, Locators.TEXT_INPUT_ERROR_CLASS_NAME)))
        text_button = driver.find_element(By.CLASS_NAME, Locators.TEXT_INPUT_ERROR_CLASS_NAME).text

        assert text_button == 'Некорректный пароль'

        driver.quit()
