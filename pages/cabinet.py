from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import CartLocators
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class CabinetPage(BasePage):
    """Класс создает экземпляр страницы Кабинет пользователя (десктопная версия), переменные и методы поиска элеменов
    на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.cart_url()
        driver.get(self.url)

        self.prod_names = self.driver.find_elements(*CartLocators.in_cart_prod_name)
        self.prod_content = self.driver.find_elements(*CartLocators.in_cart_prod_content)