from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import BlogLocators
from selenium.webdriver.common.keys import Keys


class SalesPage(BasePage):
    """Класс создает экземпляр страницы акций сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        url = LinsaUa.blog_url()
        driver.get(url)

        # Header elements
        self.start_img = driver.find_element(*BlogLocators.logo_img)

        # Sales Banners
        self.sales_banner_imgs = driver.find_elements(*BlogLocators.banner_imgs)
        self.sales_banner_btns = driver.find_elements(*BlogLocators.banner_btns)