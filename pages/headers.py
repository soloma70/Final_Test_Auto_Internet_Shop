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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(StartLocators.callback_form_submit))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def input_callback_data(self, name: str, phone: str):
        print(name)
        element = self.driver.find_element(*StartLocators.callback_form_name)
        element.clear()
        element.send_keys(name)
        self.driver.find_element(*StartLocators.callback_form_phone).send_keys(phone)

    def search_callback_submit(self) -> WebElement:
        return self.driver.find_element(*StartLocators.callback_form_submit)

    def callback_close(self):
        self.driver.find_element(*StartLocators.callback_form_close).click()

    def login_btn_click(self):
        self.driver.find_element(*RegLocators.login_btn).click()

    def input_login_passw(self, login: str, passw: str):
        auth_login = self.driver.find_element(*RegLocators.login_name)
        auth_login.clear()
        auth_login.send_keys(login)
        auth_passw = self.driver.find_element(*RegLocators.login_pass)
        auth_passw.clear()
        auth_passw.send_keys(passw)

    def auth_submit(self):
        self.driver.find_element(*RegLocators.login_submit).click()

    def wait_download_cabinet(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CabinetLocators.cabinet_name))

    def answer_nonvalid_data(self) -> str:
        answer = self.driver.find_element(*RegLocators.login_answer).text
        return answer

    def auth_cancel(self):
        self.driver.find_element(*RegLocators.login_close).click()

    def registr_click(self):
        self.driver.find_element(*RegLocators.login_btn).click()
        self.driver.find_element(*RegLocators.reg_link).click()

    def input_reg_data(self, name: str, phone: str, passw: str):
        reg_name = self.driver.find_element(*RegLocators.reg_name)
        reg_name.clear()
        reg_name.send_keys(name)
        reg_phone = self.driver.find_element(*RegLocators.reg_phone)
        reg_phone.clear()
        reg_phone.send_keys(phone)
        auth_passw = self.driver.find_element(*RegLocators.login_pass)
        auth_passw.clear()
        auth_passw.send_keys(passw)
        self.driver.find_element(*RegLocators.reg_pers_data).click()

    def reg_submit(self):
        self.driver.find_element(*RegLocators.reg_submit).click()
        code_sms = input('Enter the received SMS code -> ')
        self.driver.find_element(*RegLocators.reg_sms).send_keys(code_sms)
        self.driver.find_element(*RegLocators.reg_sms_submit).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegLocators.start_shop_btn)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CabinetLocators.cabinet_name))

    def reg_cancel(self):
        self.driver.find_element(*RegLocators.registr_popup_close).click()

    def wishlist_btn_click(self):
        self.driver.find_element(*StartLocators.wishlist_btns).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegLocators.login_submit))

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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(StartLocators.menu_button_close))
        self.driver.find_elements(*StartLocators.menu_points)[index].click()

