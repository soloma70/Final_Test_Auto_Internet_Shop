from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import CartLocators
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from random import randint


class CartPage(BasePage):
    """Класс создает экземпляр страницы Корзина (десктопная версия), переменные и методы поиска элеменов
    на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.cart_url()
        driver.get(self.url)

        self.prod_names = self.driver.find_elements(*CartLocators.in_cart_prod_name1)
        self.prod_content = self.driver.find_elements(*CartLocators.in_cart_prod_name2)

    def sum_in_cart(self) -> [float, float, float]:
        sum_cart_top = float(self.driver.find_element(*CartLocators.sum_cart_top).text.split()[0])
        sum_cart_bottom = float(self.driver.find_element(*CartLocators.sum_cart_bottom).text.split()[0])
        prods_sum = self.driver.find_elements(*CartLocators.in_cart_prod_sum)
        in_cart_prod_sum = sum([float(prod_sum.text.split()[0]) for prod_sum in prods_sum])
        return sum_cart_top, sum_cart_bottom, in_cart_prod_sum

    def param_lens(self, index: int) -> [str, str, str, str]:
        prod_name = self.driver.find_elements(*CartLocators.in_cart_prod_name1)[index].text
        prod_content = self.driver.find_elements(*CartLocators.in_cart_prod_name2)[index].text
        prod_brand = prod_content.split('\n')[0]
        lens_sph = (prod_content.split('\n')[1]).split()[2]
        lens_bc = (prod_content.split('\n')[2]).split()[3]
        return prod_name, prod_brand, lens_sph, lens_bc

    def param_prod(self, index: int) -> list:
        # prod_name1 = self.driver.find_elements(*CartLocators.in_cart_prod_name1)[index].text
        # prod_name2 = self.driver.find_elements(*CartLocators.in_cart_prod_name1)[index].text
        # prod_name = f'{prod_name1} {prod_name2}'
        prod_brand = self.driver.find_elements(*CartLocators.in_cart_brand)
        prod_sex = self.driver.find_elements(*CartLocators.in_cart_sex)
        prod_temple_length = self.driver.find_elements(*CartLocators.in_cart_temple_length)
        prod_bridge_width = self.driver.find_elements(*CartLocators.in_cart_bridge_width)
        prod_eyepiece_width = self.driver.find_elements(*CartLocators.in_cart_temple_length)
        return [prod_brand, prod_sex, prod_temple_length, prod_bridge_width, prod_eyepiece_width]

    def param_care(self, index: int) -> [str, str]:
        prod_name = self.driver.find_elements(*CartLocators.in_cart_prod_name1)[index].text
        prod_content = self.driver.find_elements(*CartLocators.in_cart_prod_name2)[index].text
        prod_brand = prod_content.split('\n')[0]
        return prod_name, prod_brand

    def checkout_click(self):
        self.driver.find_elements(*CartLocators.checkout)[1].click()

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

    def search_item_in_list(self, test_item: str, item_list: list) -> int:
        i = 0
        while test_item != item_list[i]:
            i += 1
        return i

    def goto_delivery(self):
        self.driver.find_element(*CartLocators.next_step_delivery).click()

    def input_delivery_np(self, city: str, branch: str):
        self.driver.find_element(*CartLocators.input_city).click()
        #
        city_list = self.driver.find_elements(*CartLocators.city_list)
        city_name = [name_city.text.strip() for name_city in city_list]
        index = self.search_item_in_list(city, city_name)
        city_list[index].click()
        sleep(1)
        self.driver.find_element(*CartLocators.dilivery_np).click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable((CartLocators.np_branch)))
        self.driver.find_element(*CartLocators.np_branch).click()
        #
        branch_list = self.driver.find_elements(*CartLocators.branch_list)
        num_brahch = [num.text.split('№')[1].split()[0] for num in branch_list]
        index = self.search_item_in_list(branch, num_brahch)
        branch_list[index].click()

    def goto_pay(self):
        self.driver.find_element(*CartLocators.next_step_pay).click()

    def input_pay_after_receiving(self, comment='', call='n'):
        self.driver.find_element(*CartLocators.pay_rec_order).click()
        self.driver.find_element(*CartLocators.comment_order).send_keys(comment)
        if call == 'n':
            self.driver.find_element(*CartLocators.dont_call).click()

    def goto_benefit(self):
        self.driver.find_element(*CartLocators.next_step_benefit).click()

    def input_benefit(self, promo_code='') -> WebElement:
        self.driver.find_element(*CartLocators.input_promo).send_keys(promo_code)
        self.driver.find_element(*CartLocators.confirm_promo).click()
        wrong_promo = self.driver.find_element(*CartLocators.wrong_promo)
        return wrong_promo
