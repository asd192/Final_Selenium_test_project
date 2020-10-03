import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators
from .locators import MainPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """перехват исключний"""
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        """проверка местной alert-капчи"""

        # читаем число x и вычисляем
        alert = self.browser.switch_to.alert
        alert_num = float(alert.text.split(' ')[2])
        alert_num = math.log(abs(12 * math.sin(alert_num)))

        # отправка результата
        prompt_alert = self.browser.switch_to.alert
        prompt_alert.send_keys(str(alert_num))
        prompt_alert.accept()

        # проверяем следующий alert на ожидаемый результат(что ответ верный)
        alert_result = self.browser.switch_to.alert
        alert_result_text = alert_result.text
        print(alert_result_text)
        assert 'Поздравляем' in alert_result_text, "Alert: the result doesn't match"
        alert_result.accept()

    def is_not_element_present(self, how, what, timeout=4):
        """проверяет, что элемент не появляется на странице в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """проверяет, что какой-то элемент исчезает"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """переход на страницу авторизации"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        """переход на страницу авторизации"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
            "Login link is not presented"

    def go_to_basket(self):
        """переход в корзину"""
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        """проверка, что user залогинен"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"