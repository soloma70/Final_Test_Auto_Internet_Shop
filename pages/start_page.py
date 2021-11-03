from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators
from selenium.webdriver.common.keys import Keys


class StartPage(BasePage):
    """Класс определяет параметры стартовой страницы сайте, свойства и функции поиска элеменов на странице
    в десктопной и мобильной версиях сайта, а так же некоторые вспомагательные функции """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        url = LinsaUa.start_url
        driver.get(url)

        # Десктоп-элементы
        # Элементы хедера
        self.start_img = driver.find_element(*StartLocators.logo_img)
        self.search_field = driver.find_element(*StartLocators.search_field)
        self.callback_btn = driver.find_element(*StartLocators.callback_btn)
        self.login_btn = driver.find_element(*StartLocators.login_btn)
        self.wishlist_btn = driver.find_element(*StartLocators.wishlist_btns)
        self.cart_btn = driver.find_element(*StartLocators.cart_btn)
        self.lang_btn_active = driver.find_element(*StartLocators.lang_btn_active)
        self.lang_uk_btn = driver.find_element(*StartLocators.lang_btn_uk)
        self.lang_ru_btn = driver.find_element(*StartLocators.lang_btn_ru)

        # Элементы бокового меню
        self.menu_btn = driver.find_element(*StartLocators.menu_button)
        self.menu_btn_close = driver.find_element(*StartLocators.menu_button_close)
        self.menu_points = driver.find_elements(*StartLocators.menu_points)

        # Элементы главного меню
        self.main_menu_points = driver.find_elements(*StartLocators.main_menu_points)

        # Элементы баннеров
        self.sales_banners = driver.find_elements(*StartLocators.sales_banners)
        self.all_sales_prods = driver.find_element(*StartLocators.all_sales_prods)

        # Элементы любимых брендов
        self.love_brands_sunglasses = driver.find_element(*StartLocators.love_brands_sunglasses)
        self.love_brands_lenses = driver.find_element(*StartLocators.love_brands_lenses)
        self.love_brands_accessories = driver.find_element(*StartLocators.love_brands_accessories)

        # Элементы регистрации
        self.reg_btn = driver.find_element(*StartLocators.registr_btn)
        self.add = driver.find_element(*StartLocators.registr_popup_add)
        self.close = driver.find_element(*StartLocators.registr_popup_close)

        # Элементы прокрутки страницы
        self.win_scroll_begin = driver.execute_script("window.scrollTo(0, 0)")
        self.win_scroll = driver.execute_script("window.scrollTo(0, 850)")
        self.win_scroll_b = driver.execute_script("window.scrollTo(0, 1200)")
        self.win_scroll_r = driver.execute_script("window.scrollTo(0, 1850)")




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

    def all_sales_prods_click(self):
        self.all_sales_prods.click()


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


