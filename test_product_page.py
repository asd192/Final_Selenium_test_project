# pytest -s test_product_page.py

from .pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_go_to_login_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.calculating_the_formula_in_alert()
