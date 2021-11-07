from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import SalesLocators
from selenium.webdriver.common.keys import Keys


class SalesPage(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        url = LinsaUa.sales_url()
        driver.get(url)

        # Header elements
        self.start_img = driver.find_element(*SalesLocators.logo_img)

        # Sales Banners
        self.sales_banner_imgs = driver.find_elements(*SalesLocators.sales_banner_imgs)
        self.sales_banner_btns = driver.find_elements(*SalesLocators.sales_banner_btns)
        self.sales_product = driver.find_elements(*SalesLocators.sales_products)
        self.sales_product_buy = driver.find_elements(*SalesLocators.sales_products_buy)