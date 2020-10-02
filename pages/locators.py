from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "#1register_form")
