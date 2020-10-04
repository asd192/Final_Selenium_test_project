from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CLASS_NAME, "btn-group")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADRESS_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form button")
    NAME_PRODUCTS_PAGE = (By.CSS_SELECTOR, "#content_inner H1")
    NAME_PRODUCTS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_PRODUCT = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE_BASKET = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')
    SUCCESS_MESSAGE2 = (By.XPATH, 'empty')

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    MASSAGE_ABOUT_SUCCESS_ADD_TO_BUSKED = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1)>.alertinner>strong')
    MASSAGE_ABOUT_BUSKED_PRICE = (By.CSS_SELECTOR, '.alert-info>.alertinner>p>strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_PRODUCTS = (By.XPATH, '//*[@id="content_inner"]/div[1]/div/h2')
    BASKET_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p/a')
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
    BASKET_COST = (
    By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) strong')
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BOOK_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    BOOK_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
