from selenium.webdriver.common.by import By


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

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    PRICE = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    SUM_PRICES = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")