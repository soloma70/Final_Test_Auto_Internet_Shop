from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import LensLocators, ProductLensLocators


class LensPage(BasePage):
    """Класс создает экземпляр страницы акций сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        self.url = LinsaUa.lens_url()
        driver.get(self.url)

        # Header elements
        self.start_img = driver.find_element(*LensLocators.logo_img)

        # Filter elements
        self.filters = driver.find_elements(*LensLocators.filters)
        self.filters = driver.find_elements(*LensLocators.filters)