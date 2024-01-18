from selenium.webdriver.common.by import By
import random
class Locators():
    PROFILE = (By.XPATH, ".//p[starts-with(text(),'Личн')]") #Кнопка личного кабинета
    LINK_REGISTRATION = (By.XPATH, ".//a[(@class = 'Auth_link__1fOlj') and (@href='/register')]") #Текст-ссылка на регистрацию
    LINK_LOGIN = (By.XPATH, ".//a[(@class = 'Auth_link__1fOlj') and (@href='/login')]") #Текст-ссылка на вход
    LINK_FORGOT_PASSWORD = (By.XPATH, ".//a[(@class = 'Auth_link__1fOlj') and (@href='/forgot-password')]") #Текст-ссылка на "Восстановить пароль"
    INPUT_NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")   #Поле ввода имени в форме регистрации
    INPUT_EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input") #Поле ввода email в форме регистрации
    INPUT_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") #Поле ввода пароля в форме регистрации
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']") #Кнопка регистрации
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  #Кнопка "Войти"
    BUTTON_FORGOT = (By.XPATH, "//button[text()='Восстановить']") #Кнопка "Восстановить"
    TEXT_INPUT_ERROR = (By.CLASS_NAME, 'input__error') #Надпись о неуспешной регистрации
    BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")  #Кнопка «Войти в аккаунт»
    BUTTON_MAIN_OFFER = (By.XPATH, "//button[text()='Оформить заказ']") #Кнопка «Оформить заказ»
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']") #Кнопка «Выйти"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") #Кнопка перехода в конструктор(главную)
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]") #Раздел «Соусы»
    PARENT_SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::*")
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]") #Раздел «Булки»
    PARENT_BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]/parent::*")
    STUFFING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]") #Раздел «Начинки»
    PARENT_STAFFING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::*") #Родитель раздела "Ночинки"
