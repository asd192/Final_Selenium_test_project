from selenium.common.exceptions import NoSuchElementException
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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
