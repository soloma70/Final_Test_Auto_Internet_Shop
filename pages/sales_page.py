from time import sleep
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.url_list import LinsaUa
from pages.locators import SalesLocators, ProductLocators
from selenium.webdriver.remote.webelement import WebElement


class SalesPage(BasePage):
    """Класс создает экземпляр страницы акций сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        self.url = LinsaUa.sales_url()
        driver.get(self.url)

        # Header elements
        self.start_img = driver.find_element(*SalesLocators.logo_img)

        # Sales Banners
        self.sales_banner_imgs = driver.find_elements(*SalesLocators.banner_imgs)
        self.sales_banner_btns = driver.find_elements(*SalesLocators.banner_btns)
        self.sales_product = driver.find_elements(*ProductLocators.products)

    def find_banner(self, index: int) -> WebElement:
        banner = self.driver.find_elements(*SalesLocators.banner_imgs)[index]
        return banner

    def goto_page_banner(self, index: int) -> [str, str]:
        url_banner = self.driver.find_elements(*SalesLocators.banner_btns)[index].get_attribute('href')
        self.driver.find_elements(*SalesLocators.banner_btns)[index].click()
        url_page = self.driver.current_url
        return url_banner, url_page

    def goto_banner(self, index: int):
        self.sales_banner_btns[index].click()

    def goto_product_page(self, index: int) -> [str, str]:
        url_banner = self.driver.find_elements(*ProductLocators.products)[index].get_attribute('href')
        self.driver.find_elements(*ProductLocators.products)[index].click()
        sleep(1)
        url_page = self.driver.current_url
        return url_banner, url_page