from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import FramesLocators, PaginLocators
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class FramesPage(BasePage):
    """Класс создает экземпляр страницы сайта Оправы (десктопная версия), переменные и методы поиска элеменов
    на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.frames_url()
        driver.get(self.url)

        # Filter elements
        self.filters = driver.find_elements(*FramesLocators.filters)

        # Sort elements
        self.sort_by = driver.find_elements(*FramesLocators.sort_by)

        # Card elements
        self.amount_total_on_page = driver.find_element(*FramesLocators.amount_frames)

        # Pagination
        self.pagination = driver.find_elements(*PaginLocators.pagination)


    def amount_on_page(self, index: int) -> int:
        self.driver.get(super().goto_page(index+1))
        amount_on_page = len(self.driver.find_elements(*FramesLocators.cards_frames_url))
        return amount_on_page

    def get_page_urls(self, index: int) -> [str, str]:
        goto_url = self.driver.find_elements(*PaginLocators.pagination)[index].get_attribute('href')
        self.driver.get(goto_url)
        current_url = self.driver.current_url
        return goto_url, current_url

    def find_frames_name(self):
        return self.driver.find_element(*FramesLocators.name)

    def right_arrow_click(self) -> int:
        self.driver.find_element(*PaginLocators.arrow_right).click()
        page_number = int(self.driver.current_url.split('=')[1])
        return page_number

    def left_arrow_click(self) -> int:
        self.driver.find_element(*PaginLocators.arrow_left).click()
        page_number = int(self.driver.current_url.split('=')[1])
        return page_number

    def filter_click_lens(self, index: int, test_set: list) -> list:
        self.driver.find_elements(*FramesLocators.filters)[index].click()
        filter_vals = self.driver.find_elements(*FramesLocators.filter_list[index])
        filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        if test_set[index] not in filter_val and test_set[index] != '' and filter_vals != []:
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,
                                     f'div.right-filter-cntrl.js-rf-cntrl-{index + 1}.slick-arrow').click()
            filter_vals = self.driver.find_elements(*FramesLocators.filter_list[index])
            filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]
            if test_set[index] not in filter_val and test_set[index] != '' and filter_vals != []:
                print()
                print(f'!!! Check test set {test_set[11]} - {test_set[index]} is absent among the available positions')

        if filter_vals != [] and test_set[index] != '':
            i = 0
            while filter_vals[i].get_attribute('title') != test_set[index]:
                i += 1
            else:
                filter_vals[i].click()
        return filter_val

    def search_result(self) -> [list, list]:
        search_result_brands = self.driver.find_elements(*FramesLocators.cards_frames_brand)
        search_result_brand = [search_result_brands[k].text for k in range(len(search_result_brands))]
        search_result_names = self.driver.find_elements(*FramesLocators.cards_frames_name)
        search_result_name = [search_result_names[k].text for k in range(len(search_result_names))]
        return search_result_brand, search_result_name

    def clear_all_filter(self):
        self.driver.find_element(*FramesLocators.clear_all_filters).click()

    def sorted_by_on_page(self, index: int):
        self.driver.find_elements(*FramesLocators.sort_by)[index].click()
        sleep(2)

    def get_frame_list_on_page(self) -> [list]:
        lens_price = self.driver.find_elements(*FramesLocators.card_frames_price)
        list_price = [int(lens_price[i].text.split()[0]) for i in range(8)]
        return list_price

    def card_frame_len(self) -> int:
        return len(self.driver.find_elements(*FramesLocators.cards_frames_url))-1

    def rand_frames_page(self, amount: int) -> [list]:
        page_num = [1, amount]
        for i in range(4):
            page_num.append(randint(2, amount-1))
            while page_num[-2] == page_num[-1]:
                page_num.append(randint(2, amount - 1))
        page_num.sort()
        return page_num

    def rand_frames_card(self, amount: int) -> int:
        index = randint(0, amount)
        return index

