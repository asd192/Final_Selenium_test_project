import time
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators


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

    def should_not_be_success_message(self):
        """упадет, как только увидит искомый элемент"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE2), \
            "Success message is presented, but should not be"

    def checks_that_the_element_disappears(self):
        """будет ждать до тех пор, пока элемент не исчезнет"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The element did not disappear, but should"

    def add_book_to_cart(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET_BUTTON), "Add to cart button is not presented"
        button = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_the_puzzle(self):
        self.solve_quiz_and_get_code()

    def should_be_add_message(self):
        assert self.is_element_present(
            *BasketPageLocators.ADD_TO_BASKET_MESSAGE), "Added to cart message is not presented"

    def cart_cost_should_be_equal_price_of_the_book(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_COST) == self.is_element_present(
            *BasketPageLocators.BOOK_PRICE), \
            "Prices of books are not the same"

    def names_of_books_should_be_equal(self):
        assert self.is_element_present(*BasketPageLocators.BOOK_NAME_IN_MESSAGE) == self.is_element_present(
            *BasketPageLocators.BOOK_NAME), \
            "Book names are not the same"

    def added_to_cart_message_is_presented(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ADD_TO_BASKET_MESSAGE), "Added to cart message is presented"

    def success_message_should_disappear(self):
        assert self.is_disappeared(
            *BasketPageLocators.ADD_TO_BASKET_MESSAGE), "Added to cart message not disappeared"







    def add_product_to_basket(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def get_product_name(self):
        name = self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME)
        return name

    def get_product_price(self):
        price = self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)
        return price

    def should_be_massage_about_success_adding_to_busked(self, product_name):
        assert product_name == self.get_text_from_element(*ProductPageLocators.MASSAGE_ABOUT_SUCCESS_ADD_TO_BUSKED), \
            'Massage about added to busked not found'

    def should_be_correct_price_after_adding_to_busked(self, product_price):
        assert product_price == self.get_text_from_element(*ProductPageLocators.MASSAGE_ABOUT_BUSKED_PRICE), \
            'Incorrect price in busked massage'
