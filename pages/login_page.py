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
        assert login_form.text == "Войти" or login_form.text == "Log In", 'There is no login form'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form.text == "Зарегистрироваться" or register_form.text == "Register", 'There is no register form'

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password_repeat = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_email.send_keys(email)
        register_password.send_keys(password)
        register_password_repeat.send_keys(password)
        register_button.click()
