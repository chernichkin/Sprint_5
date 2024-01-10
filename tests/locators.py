
class Locators():
    PROFILE = ".//p[starts-with(text(),'Личн')]" #Кнопка личного кабинета
    LINK_REGISTRATION = ".//a[(@class = 'Auth_link__1fOlj') and (@href='/register')]" #Текст-ссылка на регистрацию
    LINK_LOGIN = ".//a[(@class = 'Auth_link__1fOlj') and (@href='/login')]" #Текст-ссылка на вход
    LINK_FORGOT_PASSWORD = ".//a[(@class = 'Auth_link__1fOlj') and (@href='/forgot-password')]" #Текст-ссылка на "Восстановить пароль"
    INPUT_NAME = ".//fieldset[1]//input"  #Поле ввода имени в форме регистрации
    INPUT_EMAIL_REG = ".//fieldset[2]//input" #Поле ввода email в форме регистрации
    INPUT_PASSWORD_REG = ".//fieldset[3]//input" #Поле ввода пароля в форме регистрации
    BUTTON_REGISTRATION = ".//button[text()='Зарегистрироваться']" #Кнопка регистрации
    BUTTON_LOGIN = "//button[text()='Войти']" #Кнопка "Войти"
    BUTTON_FORGOT = "//button[text()='Восстановить']" #Кнопка "Восстановить"
    TEXT_INPUT_ERROR_CLASS_NAME = 'input__error' #Надпись о неуспешной регистрации
    BUTTON_MAIN = "//section[2]/div/button" #Кнопка «Войти в аккаунт» на главной или "Оформить заказ"
    BUTTON_EXIT = "//button[text()='Выход']" #Кнопка «Выйти"
    BUTTON_CONSTRUCTOR = "//p[text()='Конструктор']" #Кнопка перехода в конструктор(главную)
    INPUT_PASSWORD_LOG = INPUT_EMAIL_REG #Поле ввода пароля для входа
    INPUT_EMAIL_LOG = INPUT_NAME #Поле ввода email для входа
    SAUCES_SECTION = "//span[contains(text(),'Соусы')]" # Раздел «Соусы»
    PARENT_SAUCES_SECTION = "//div/main/section[1]/div[1]/div[2]"
    BUNS_SECTION = "//span[contains(text(),'Булки')]" # Раздел «Булки»
    PARENT_BUNS_SECTION = "//div/main/section[1]/div[1]/div[1]"
    STUFFING_SECTION = "//span[contains(text(),'Начинки')]"
    PARENT_STAFFING_SECTION = "//div/main/section[1]/div[1]/div[3]"