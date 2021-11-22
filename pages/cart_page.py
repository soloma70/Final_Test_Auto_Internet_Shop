from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import LensLocators, ProductLocators, ProductLensLocators, CartLocators
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from random import randint


class CartPage(BasePage):
    """Класс создает экземпляр страницы Корзина (десктопная версия), переменные и методы поиска элеменов
    на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.cart_url()
        driver.get(self.url)

        self.prod_names = self.driver.find_elements(*CartLocators.in_cart_prod_names)
        self.prod_content = self.driver.find_elements(*CartLocators.in_cart_prod_brands)

    def sum_in_cart(self) -> [int, int, int]:
        sum_cart_top = int(self.driver.find_element(*CartLocators.sum_cart_top).text.split()[0])
        sum_cart_bottom = int(self.driver.find_element(*CartLocators.sum_cart_bottom).text.split()[0])
        prods_sum = self.driver.find_elements(*CartLocators.in_cart_prod_sum)
        in_cart_prod_sum = sum([int(prod_sum.text.split()[0]) for prod_sum in prods_sum])
        return sum_cart_top, sum_cart_bottom, in_cart_prod_sum

    def param_lens(self, index: int) -> [str, str, str, str]:
        prod_name = self.driver.find_elements(*CartLocators.in_cart_prod_names)[index].text
        prod_content = self.driver.find_elements(*CartLocators.in_cart_prod_brands)[index].text
        prod_brand = prod_content.split('\n')[0]
        lens_sph = (prod_content.split('\n')[1]).split()[2]
        lens_bc = (prod_content.split('\n')[2]).split()[3]
        # self.checkout_click()
        return prod_name, prod_brand, lens_sph, lens_bc

    def checkout_click(self):
        self.driver.find_element(*CartLocators.checkout).click()

    def input_data(self, name: str, email: str, phone: str):
        input_name = self.driver.find_element(*CartLocators.input_name)
        input_name.clear()
        input_name.send_keys(name)
        input_email = self.driver.find_element(*CartLocators.input_email)
        input_email.clear()
        input_email.send_keys(email)
        input_phone = self.driver.find_element(*CartLocators.input_phone)
        input_phone.clear()
        input_phone.send_keys(phone)
        sleep(1)
        self.driver.find_element(*CartLocators.next_step_delivery).click()

    def search_item_in_list(self, test_item: str, item_list: list) -> int:
        i = 0
        while test_item != item_list[i]:
            i += 1
        return i

    def input_delivery_np(self, city: str, branch: str):
        self.driver.find_element(*CartLocators.input_city).click()
        #
        city_list = self.driver.find_elements(*CartLocators.city_list)
        city_name = [name_city.text.strip() for name_city in city_list]
        index = self.search_item_in_list(city, city_name)
        city_list[index].click()
        #
        self.driver.find_element(*CartLocators.dilivery_np).click()
        self.driver.find_element(*CartLocators.np_branch).click()
        #
        branch_list = self.driver.find_elements(*CartLocators.branch_list)
        num_brahch = [num.text.split('№')[1].split()[0] for num in branch_list]
        index = self.search_item_in_list(branch, num_brahch)
        branch_list[index].click()
        sleep(1)
        #
        self.driver.find_element(*CartLocators.next_step_pay).click()
        sleep(5)






