from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators, StartLocatorsMobile
from selenium.webdriver.common.keys import Keys


class StartPage(BasePage):
    """Класс определяет параметры стартовой страницы сайте, свойства и функции поиска элеменов на странице
    в десктопной и мобильной версиях сайта, а так же некоторые вспомагательные функции """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        url = LinsaUa.start_url
        driver.get(url)

        # Header elements
        self.start_img_mobile = driver.find_element(*StartLocatorsMobile.logo_img_mobile)
        self.search_field_img = driver.find_element(*StartLocatorsMobile.search_field_img)
        self.wishlist_btn = driver.find_element(*StartLocatorsMobile.wishlist_btns)
        self.cart_btn = driver.find_element(*StartLocatorsMobile.cart_btn)

        # RightSide Menu elements
        self.menu_btn = driver.find_element(*StartLocatorsMobile.menu_button)
        self.menu_btn_close = driver.find_element(*StartLocatorsMobile.menu_button_close)
        self.lang_btn_active = driver.find_element(*StartLocators.lang_btn_active)
        self.lang_btn = driver.find_element(*StartLocators.lang_btn_uk)
        self.menu_points = driver.find_elements(*StartLocatorsMobile.menu_points_main)  # 13
        self.menu_points_hidden = driver.find_elements(*StartLocatorsMobile.menu_points_hidden)  # 7

        # Banners elements
        self.sales_banners = driver.find_elements(*StartLocatorsMobile.sales_banners)
        self.all_sales_prods = driver.find_element(*StartLocatorsMobile.all_sales_prods)

        # Love Brands elements
        self.love_brands_sunglasses = driver.find_element(*StartLocatorsMobile.love_brands_sunglasses)
        self.love_brands_lenses = driver.find_element(*StartLocatorsMobile.love_brands_lenses)
        self.love_brands_accessories = driver.find_element(*StartLocatorsMobile.love_brands_accessories)
        self.vogue = driver.find_element(*StartLocatorsMobile.img_vogue)
        self.rayban = driver.find_element(*StartLocatorsMobile.img_rayban)
        self.carrera = driver.find_element(*StartLocatorsMobile.img_carrera)
        self.avisor = driver.find_element(*StartLocatorsMobile.img_avizor)
        self.menicon = driver.find_element(*StartLocatorsMobile.img_menicon)
        self.okvision = driver.find_elements(*StartLocatorsMobile.img_okvision)

        # Registration elements
        self.reg_btn = driver.find_element(*StartLocatorsMobile.registr_btn)
        self.add = driver.find_element(*StartLocatorsMobile.registr_popup_add)
        self.close = driver.find_element(*StartLocatorsMobile.registr_popup_close)

        # Blog elements
        self.blog_card_1 = driver.find_element(*StartLocatorsMobile.blog_card_1)
        self.blog_card_2 = driver.find_element(*StartLocatorsMobile.blog_card_2)

        # # Footers elements
        self.footers_left_btns = driver.find_elements(*StartLocators.footers_left_btns)
        self.footers_right_btns = driver.find_elements(*StartLocators.footers_right_btns)

    def start_img_click(self):
        self.start_img_mobile.click()

    def search_field_click_close(self):
        self.search_field_img.click()
        self.driver.find_element(*StartLocatorsMobile.search_field_close).click()

    def search_field_click_search(self, search_value):
        self.search_field_img.click()
        self.search_field = self.driver.find_element(*StartLocatorsMobile.search_field)
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.send_keys(Keys.ENTER)

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
