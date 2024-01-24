from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_text_in_empty_basket(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        empty_basket_text = empty_basket_text.text
        print(empty_basket_text)
        assert empty_basket_text == "Your basket is empty. Continue shopping" or empty_basket_text == "Ваша корзина пуста. Продолжить покупки", "Basket is not empty"
    def check_empty_basket_without_product(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product is in basket"
