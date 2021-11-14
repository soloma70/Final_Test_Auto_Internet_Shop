from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators


class StartPage(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        self.url = LinsaUa.start_url
        driver.get(self.url)

        # Main Menu elements
        self.main_menu_points = driver.find_elements(*StartLocators.main_menu_points)

        # Banners elements
        self.sales_banners = driver.find_elements(*StartLocators.sales_banners)
        self.all_sales_prods = driver.find_element(*StartLocators.all_sales_prods)

        # Love Brands elements
        self.love_brands_sunglasses = driver.find_element(*StartLocators.love_brands_sunglasses)
        self.love_brands_lenses = driver.find_element(*StartLocators.love_brands_lenses)
        self.love_brands_accessories = driver.find_element(*StartLocators.love_brands_accessories)
        self.vogue = driver.find_element(*StartLocators.img_vogue)
        self.rayban = driver.find_element(*StartLocators.img_rayban)
        self.avisor = driver.find_element(*StartLocators.img_avizor)
        self.menicon = driver.find_element(*StartLocators.img_menicon)
        self.okvision = driver.find_elements(*StartLocators.img_okvision)

        # Registration elements
        self.reg_btn = driver.find_element(*StartLocators.registr_btn)
        self.add = driver.find_element(*StartLocators.registr_popup_add)
        self.close = driver.find_element(*StartLocators.registr_popup_close)

        # Blog elements
        self.blog_card_1 = driver.find_element(*StartLocators.blog_card_1)
        self.blog_card_2 = driver.find_element(*StartLocators.blog_card_2)
        self.blog_card_3 = driver.find_element(*StartLocators.blog_card_3)

        # Scroll elements
        self.win_scroll_begin = driver.execute_script("window.scrollTo(0, 0)")
        self.win_scroll = driver.execute_script("window.scrollTo(0, 850)")

    def all_sales_prods_click(self):
        self.all_sales_prods.click()
