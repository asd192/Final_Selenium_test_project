from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def product_not_in_basket(self):
        """ожидание, что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
            "there are products in the cart but they should not"

    def text_about_the_absence_of_products_in_the_shopping_cart(self):
        """проверка наличия ссылки, чтобы убедиться, что корзина пуста"""
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            "there is no text indicating that the trash is empty"
