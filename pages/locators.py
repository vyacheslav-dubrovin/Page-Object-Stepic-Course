from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    SIGN_IN_FORM = (By.CSS_SELECTOR, "#login_form > h2")
    SIGN_IN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    FORGOT_PASSWORD = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/p/a")
    SIGN_IN_BUTTON = (By.NAME, "login_submit")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form > h2")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")