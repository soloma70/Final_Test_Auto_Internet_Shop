from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import LensLocators, ProductLocators
from time import sleep
from selenium.webdriver.common.by import By
from random import randint


class LensPage(BasePage):
    """Класс создает экземпляр страницы акций сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=5):
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

        # Card elements
        self.amount_total_on_page = driver.find_element(*LensLocators.amount_lens)
        self.cards_lens_url = driver.find_elements(*LensLocators.cards_lens_url)
        self.card_lens_amount = driver.find_elements(*LensLocators.card_lens_amount)
        self.card_lens_price = driver.find_elements(*LensLocators.card_lens_price)

        # Pagination
        self.pagination = driver.find_elements(*LensLocators.pagination)

    def amount_on_page(self, index: int) -> int:
        self.driver.get(self.driver.find_elements(*LensLocators.pagination)[index].get_attribute('href'))
        amount_on_page = len(self.driver.find_elements(*LensLocators.cards_lens_url))
        return amount_on_page

    def get_page_urls(self, index: int) -> [str, str]:
        goto_url = self.driver.find_elements(*LensLocators.pagination)[index].get_attribute('href')
        self.driver.get(goto_url)
        current_url = self.driver.current_url
        return goto_url, current_url

    def right_arrow_click(self) -> int:
        self.driver.find_element(*LensLocators.arrow_right).click()
        page_number = int(self.driver.current_url.split('=')[1])
        return page_number

    def left_arrow_click(self) -> int:
        self.driver.find_element(*LensLocators.arrow_left).click()
        page_number = int(self.driver.current_url.split('=')[1])
        return page_number

    def filter_click_lens(self, index: int, test_set: list) -> list:
        self.driver.find_elements(*LensLocators.filters)[index].click()
        filter_vals = self.driver.find_elements(*LensLocators.filter_list[index])
        filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        if test_set[index] not in filter_val and test_set[index] != '' and filter_vals != []:
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, f'div.right-filter-cntrl.js-rf-cntrl-{index}.slick-arrow').click()
            filter_vals = self.driver.find_elements(*LensLocators.filter_list[index])
            filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        if filter_vals != [] and test_set[index] != '':
            i = 0
            while filter_vals[i].get_attribute('title') != test_set[index]:
                i += 1
            else:
                filter_vals[i].click()
        return filter_val

    def search_result(self) -> [list, list]:
        search_result_brands = self.driver.find_elements(*LensLocators.cards_lens_name_brand)
        search_result_brand = [search_result_brands[k].text for k in range(len(search_result_brands))]
        search_result_names = self.driver.find_elements(*LensLocators.cards_lens_name)
        search_result_name = [search_result_names[k].text for k in range(len(search_result_names))]
        return search_result_brand, search_result_name

    def clear_all_filter(self):
        self.driver.find_element(*LensLocators.clear_all_filters).click()

    def sorted_by_on_page(self, index: int):
        self.driver.find_elements(*LensLocators.sort_by)[index].click()

    def get_lens_list_on_page(self) -> [list]:
        lens_price = self.driver.find_elements(*LensLocators.card_lens_price)
        list_price = [int(lens_price[i].text.split()[0]) for i in range(8)]
        return list_price

    def rand_lens_card(self, amount: int) ->list:
        index = [randint(0, amount), randint(0, amount), randint(0, amount)]
        return index

    def find_lens_name(self):
        return self.driver.find_element(*LensLocators.name)