from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators


class Footers(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        url = LinsaUa.start_url
        driver.get(url)

        # Footers elements
        self.footers_left_btns = driver.find_elements(*StartLocators.footers_left_btns)
        self.footers_right_btns = driver.find_elements(*StartLocators.footers_right_btns)