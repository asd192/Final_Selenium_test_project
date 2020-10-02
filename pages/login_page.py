from .base_page import BasePage
from .locators import LoginPageLocators


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
