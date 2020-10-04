from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # корректный url адрес
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert 'login' in self.browser.current_url, "The login link is not provided or is differen"

    def should_be_login_form(self):
        # есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "The login form is not provided"

    def should_be_register_form(self):
        # есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.FORM_REGISTER), "The form for registration in the system is not provided"

    def register_new_user(self, email, password):
        """принимает две строки и регистрирует пользователя"""
        email = str(time.time()) + "@fakemail.org"
        password = 'qpWO0mRaI'
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS_INPUT)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()