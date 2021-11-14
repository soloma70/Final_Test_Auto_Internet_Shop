from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators


class Headers(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        url = LinsaUa.start_url
        driver.get(url)

        # Header elements
        self.start_img = driver.find_element(*StartLocators.logo_img)
        self.search_field = driver.find_element(*StartLocators.search_field)
        self.callback_btn = driver.find_element(*StartLocators.callback_btn)
        self.login_btn = driver.find_element(*StartLocators.login_btn)
        self.wishlist_btn = driver.find_element(*StartLocators.wishlist_btns)
        self.cart_btn = driver.find_element(*StartLocators.cart_btn)
        self.lang_btn_active = driver.find_element(*StartLocators.lang_btn_active)
        self.lang_uk_btn = driver.find_element(*StartLocators.lang_btn_uk)
        self.lang_ru_btn = driver.find_element(*StartLocators.lang_btn_ru)

        # Rightside Menu elements
        self.menu_btn = driver.find_element(*StartLocators.menu_button)
        self.menu_btn_close = driver.find_element(*StartLocators.menu_button_close)
        self.menu_points = driver.find_elements(*StartLocators.menu_points)

    def start_img_click(self):
        self.start_img.click()

    def search_field_click(self, search_value):
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.send_keys(Keys.ENTER)

    def callback_btn_click(self):
        self.callback_btn.click()

    def login_btn_click(self):
        self.login_btn.click()

    def wishlist_btn_click(self):
        self.wishlist_btn.click()

    def cart_btn_click(self):
        self.cart_btn.click()

    def lang_btn_click(self):
        self.lang_btn_active.click()

    def lang_uk_btn_click(self):
        self.lang_uk_btn.click()

    def lang_ru_btn_click(self):
        self.lang_ru_btn.click()

    def menu_btn_click(self):
        self.menu_btn.click()

    def menu_close_btn_click(self):
        self.menu_btn_close.click()