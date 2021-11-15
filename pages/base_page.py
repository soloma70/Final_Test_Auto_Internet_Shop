from time import sleep
from urllib.parse import urlparse
from selenium.webdriver import ActionChains
from pages.locators import CartLocators, ProductLocators, ProductLensLocators


class BasePage(object):
    """ Конструктор класса - метод init, получающий объект веб-драйвера, адрес страницы и время ожидания элемента"""

    def __init__(self, driver, url, wait=3):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(wait)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_url(self, url: str):
        self.driver.get(url)

    def save_screen_browser(self, name: str):
        self.driver.save_screenshot(f'screenshots\\{name}.png')

    def amount_cart(self) -> int:
        amount = int(self.driver.find_element(*CartLocators.amount_cart_header).text)
        return amount

    def add_cart_lens_def_par(self, index: int):
        element = self.driver.find_elements(*ProductLocators.products)[index]
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_elements(*ProductLocators.products_lens_buy)[index].click()
        self.driver.find_element(*ProductLensLocators.buy_btn).click()
        self.driver.find_element(*CartLocators.close_popup_cart).click()
        sleep(1)

    def add_cart_sunglass(self, index: int):
        element = self.driver.find_elements(*ProductLocators.products)[index]
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_elements(*ProductLocators.products_buy)[index].click()
        sleep(2)
        self.driver.find_element(*CartLocators.close_popup_cart).click()
        sleep(1)
