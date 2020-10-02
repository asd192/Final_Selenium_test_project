import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def calculating_the_formula_in_alert(self):
        """расчет местной капчи в alert"""
        product_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        product_button.click()

        # вычисление выражения solve_quiz_and_get_code
        self.solve_quiz_and_get_code()

        # название товара совпадает с названием товара в сообщении(корзине)
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCTS_PAGE).text == \
               self.browser.find_element(*ProductPageLocators.NAME_PRODUCTS_MESSAGE).text, \
            "The name in the message does not match the product name"
        # стоимость товра в корзине совпадает с стоимостью товара
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text, \
            "The cost of the basket does not match the cost of the product"
