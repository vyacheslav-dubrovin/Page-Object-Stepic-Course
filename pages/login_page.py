from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url, "URL is wrong"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.browser.find_element(*LoginPageLocators.SIGN_IN_FORM)
        assert login_form.text == "Войти", 'There is no login form'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form.text == "Зарегистрироваться", 'There is no register form'