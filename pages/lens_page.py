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
        self.brands = driver.find_elements(*LensLocators.filter_list[0])
        self.lines = driver.find_elements(*LensLocators.filter_list[1])
        self.type_lens = driver.find_elements(*LensLocators.filter_list[2])
        self.repl_mode = driver.find_elements(*LensLocators.filter_list[3])
        self.base_curv = driver.find_elements(*LensLocators.filter_list[4])
        self.diameter = driver.find_elements(*LensLocators.filter_list[5])
        self.dioptr = driver.find_elements(*LensLocators.filter_list[6])

        # Sort elements
        self.sort_by = driver.find_elements(*LensLocators.sort_by)