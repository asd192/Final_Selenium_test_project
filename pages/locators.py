from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CLASS_NAME, "btn-group")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form button")
    NAME_PRODUCTS_PAGE = (By.CSS_SELECTOR, "#content_inner H1")
    NAME_PRODUCTS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_PRODUCT = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE_BASKET = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_PRODUCTS = (By.XPATH, '//*[@id="content_inner"]/div[1]/div/h2')
    BASKET_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p/a')
