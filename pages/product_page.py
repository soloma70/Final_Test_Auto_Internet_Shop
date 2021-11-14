from time import sleep
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import SalesLocators, ProductLocators
from selenium.webdriver.remote.webelement import WebElement


class ProductPage(BasePage):
    """Класс создает экземпляр страницы акций сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

