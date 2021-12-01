from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators, RegLocators, CabinetLocators


class Headers(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        self.url = LinsaUa.start_url
        driver.get(self.url)

    def start_img_click(self):
        self.driver.find_element(*StartLocators.logo_img).click()

    def search_field_click(self, search_value):
        self.search_field = self.driver.find_element(*StartLocators.search_field)
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.send_keys(Keys.ENTER)

    def callback_btn_click(self):
        self.driver.find_element(*StartLocators.callback_btn).click()
        sleep(1)

    def search_callback_submit(self) -> WebElement:
        return self.driver.find_element(*StartLocators.callback_form_submit)

    def callback_close(self):
        self.driver.find_element(*StartLocators.callback_form_close).click()

    def login_btn_click(self):
        self.driver.find_element(*RegLocators.login_btn).click()

    def registr_click(self):
        self.driver.find_element(*RegLocators.login_btn).click()
        self.driver.find_element(*RegLocators.reg_link).click()

    def input_auth_data(self, phone: str, passw: str):
        auth_login = self.driver.find_element(*RegLocators.login_name)
        auth_login.clear()
        auth_login.send_keys(phone)
        auth_passw = self.driver.find_element(*RegLocators.login_pass)
        auth_passw.clear()
        auth_passw.send_keys(passw)
        self.driver.find_element(*RegLocators.login_submit).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CabinetLocators.cabinet_name))


    def input_reg_data(self, name: str, phone: str, passw: str):
        reg_name = self.driver.find_element(*RegLocators.reg_name)
        reg_name.clear()
        reg_name.send_keys(name)
        reg_phone = self.driver.find_element(*RegLocators.reg_name)
        reg_phone.clear()
        reg_phone.send_keys(phone)
        auth_passw = self.driver.find_element(*RegLocators.login_pass)
        auth_passw.clear()
        auth_passw.send_keys(passw)
        self.driver.find_element(*RegLocators.reg_pesr_date).click()
        self.driver.find_element(*RegLocators.reg_submit).click()

    def wishlist_btn_click(self):
        self.driver.find_element(*StartLocators.wishlist_btns).click()
        sleep(1)

    def search_login_submit(self) -> WebElement:
        return self.driver.find_element(*RegLocators.login_submit)

    def login_close(self):
        self.driver.find_element(*RegLocators.login_close).click()

    def cart_btn_click(self):
        self.driver.find_element(*StartLocators.cart_btn).click()

    def lang_btn_click(self):
        self.driver.find_element(*StartLocators.lang_btn_active).click()

    def lang_uk_btn_click(self):
        self.driver.find_element(*StartLocators.lang_btn_uk).click()

    def lang_ru_btn_click(self):
        self.driver.find_element(*StartLocators.lang_btn_ru).click()

    def menu_click(self):
        self.driver.find_element(*StartLocators.menu_button).click()

    def menu_close_click(self):
        self.driver.find_element(*StartLocators.menu_button_close).click()

    def menu_points(self) -> int:
        points = len(self.driver.find_elements(*StartLocators.menu_points))
        return points

    def goto_menu_point(self, index: int):
        self.driver.find_element(*StartLocators.menu_button).click()
        sleep(1)
        self.driver.find_elements(*StartLocators.menu_points)[index].click()

