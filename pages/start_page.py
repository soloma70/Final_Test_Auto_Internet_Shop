from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators
from selenium.webdriver.common.keys import Keys


class StartPage(BasePage):
    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        url = LinsaUa.start_url
        driver.get(url)

        # Search descktop elements
        self.start_img = driver.find_element(*StartLocators.logo_img)
        self.search_field = driver.find_element(*StartLocators.search_field)
        self.callback_btn = driver.find_element(*StartLocators.callback_btn)
        self.login_btn = driver.find_element(*StartLocators.login_btn)
        self.wishlist_btn = driver.find_elements(*StartLocators.wishlist_btns)
        self.cart_btn = driver.find_element(*StartLocators.cart_btn)
        self.lang_btn = driver.find_element(*StartLocators.lang_btn)
        self.menu_btn = driver.find_element(*StartLocators.menu_button)

        # Search mobile elements
        self.start_img_mobile = driver.find_element(*StartLocators.logo_img_mobile)
        self.search_field_mobile = driver.find_element(*StartLocators.search_field_mobile)
        # self.wishlist_btn_mobile = driver.find_element(*StartLocators.wishlist_btn_mobile)
        # self.cart_btn_mobile = driver.find_element(*StartLocators.cart_btn_mobile)
        # self.menu_btn_mobile = driver.find_element(*StartLocators.menu_button_mobile)

    def start_img_click(self):
        self.start_img.click()

    def search_field_click(self, search_value):
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.send_keys(Keys.ENTER)

    # Вспомагательные функции для добавления различных строк
    def generate_string(n):
        return "x" * n

    def russian_chars():
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def chinese_chars():
        return '的一是不了人我在有他这为之大来以个中上们'

    def special_chars():
        return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

    def start_img_click_mobile(self):
        self.start_img_mobile.click()


