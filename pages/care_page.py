from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import CareLocators, ProductLocators, CartLocators
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class CarePage(BasePage):
    """Класс создает экземпляр страницы сайта Растворы и капли (десктопная версия), переменные и методы
    поиска элеменов на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.care_url()
        driver.get(self.url)

        # Filter elements
        self.filters = driver.find_elements(*ProductLocators.filters)

        # Sort elements
        self.sort_by = driver.find_elements(*ProductLocators.sort_by)

    def filter_click(self, index: int, test_set: str):
        self.driver.find_elements(*ProductLocators.filters)[index].click()
        filter_vals = self.driver.find_elements(*CareLocators.filter_list[index])
        filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        while test_set not in filter_val and (test_set != '' or filter_vals != []):
            self.driver.find_element(By.CSS_SELECTOR,
                                     f'div.right-filter-cntrl.js-rf-cntrl-{index}.slick-arrow').click()
            filter_vals = self.driver.find_elements(*CareLocators.filter_list[index])
            filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        if filter_vals != [] and test_set != '':
            i = 0
            while filter_vals[i].get_attribute('title') != test_set:
                i += 1
            else:
                filter_vals[i].click()

    def search_result(self) -> [str, str]:
        search_result_brands = self.driver.find_elements(*ProductLocators.cards_prod_brand)
        search_result_brand = [search_result_brands[k].text for k in range(len(search_result_brands))]
        search_result_names = self.driver.find_elements(*ProductLocators.cards_prod_name)
        search_result_name = [search_result_names[k].text for k in range(len(search_result_names))]
        return search_result_brand, search_result_name

    def search_result_single(self, index: int) -> list:
        search_result = self.driver.find_elements(*CareLocators.card_prod_filters_care[index])
        search_result = [search_result[k].text for k in range(len(search_result))]
        return search_result

    def filter_prod_not_found(self) -> str:
        return self.driver.find_element(*ProductLocators.card_prod_not_found).text

    def clear_all_filter(self):
        self.driver.find_element(*ProductLocators.clear_all_filters).click()

    def sorted_by_on_page(self, index: int):
        self.driver.find_elements(*ProductLocators.sort_by)[index].click()
        sleep(2)

    def add_cart_care(self, index: int, volume: str):
        element = self.driver.find_elements(*ProductLocators.products)[index]
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_elements(*ProductLocators.products_lens_buy)[index].click()
        #
        self.driver.find_element(*CareLocators.choice_volume).click()
        list_volume = self.driver.find_elements(*CareLocators.list_volume)
        sleep(1)
        self.choise_param(volume, list_volume)
        #
        add_cart_sum = int(self.driver.find_element(*CareLocators.add_cart_sum).text)
        #
        self.driver.find_element(*CareLocators.buy_btn).click()
        self.driver.find_element(*CartLocators.close_popup_cart).click()
        sleep(1)
        return add_cart_sum

    def choise_param(self, us_set: str, list_it: list):
        i = 0
        while us_set != list_it[i].text:
            i += 1
        list_it[i].click()

    def get_care_list_on_page(self) -> [list]:
        amount_card = len(self.driver.find_elements(*CareLocators.card_care_amount))
        list_price = self.part_card_price_care(amount_card, CareLocators.loc_begin, CareLocators.loc_price1,
                                               CareLocators.loc_price2)
        return list_price

    def part_card_price_care(self, iter_card: int, loc_begin: str, loc_price_1: str, loc_price_2: str) -> list:
        """ Метод формирует список цен на продукты со страницы продукта. Так как некоторые цены отсутствуют у продукта,
        применяется блок try-except для обработки исключения, предотвращения аварийного завершения кода
        и формирования правильного списка цен"""

        list_price = []
        if iter_card < 8:
            for i in range(iter_card):
                price = self.search_price_care(1, i + 1, loc_begin, loc_price_1, loc_price_2)
                list_price.append(int(price.text.split()[0]))
        elif iter_card >= 8:
            for i in range(8):
                price = self.search_price_care(1, i + 1, loc_begin, loc_price_1, loc_price_2)
                list_price.append(int(price.text.split()[0]))
            for i in range(iter_card - 8):
                price = self.search_price_care(2, i + 1, loc_begin, loc_price_1, loc_price_2)
                list_price.append(int(price.text.split()[0]))
        return list_price

    def search_price_care(self, i1: int, i2: int, loc_b: str, loc_p_1: str, loc_p_2: str) -> WebElement:
        try:
            elem_price = self.driver.find_element(By.CSS_SELECTOR,
                                                  f'{loc_b} > div:nth-child({i1}) > div:nth-child({i2}) > {loc_p_1}')
        except NoSuchElementException:
            elem_price = self.driver.find_element(By.CSS_SELECTOR,
                                                  f'{loc_b} > div:nth-child({i1}) > div:nth-child({i2}) > {loc_p_2}')
        return elem_price

