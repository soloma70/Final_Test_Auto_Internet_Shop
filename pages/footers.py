from time import sleep
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators


class Footers(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        self.url = LinsaUa.start_url
        driver.get(self.url)

        self.footers_left = driver.find_elements(*StartLocators.footers_left_btns)
        self.footers_right = driver.find_elements(*StartLocators.footers_right_btns)


    def footers_left_click(self, index: int):
        self.driver.find_elements(*StartLocators.footers_left_btns)[index].click()

    def footers_right_click(self, index: int):
        self.driver.find_elements(*StartLocators.footers_right_btns)[index].click()

    def footers_bottom_left_click(self):
        self.driver.find_element(*StartLocators.footer_bottom_left_btn).click()

    def footers_bottom_right_click(self):
        self.driver.find_element(*StartLocators.footer_bottom_right_btn).click()

    def footers_middle_click_and_goto(self, index: int) -> str:
        self.driver.find_elements(*StartLocators.footer_middle_btns)[index].click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        current_url = self.driver.current_url
        self.driver.close()
        sleep(2)
        self.driver.switch_to.window(windows[0])
        return current_url
