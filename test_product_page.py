from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="fixing this bug right now")
def test_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.add_product_to_basket()
    page.check_the_product_name()
    page.check_price()

@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.add_product_to_basket()
    page.should_dissapear_of_success_message()

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link_on_product_page(browser, link):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.should_be_login_link()

@pytest.mark.parametrize('link', links)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open(browser, link)
    page.go_to_login_page()

