from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import LensLocators, ProductLocators, ProductLensLocators


class LensPage(BasePage):
    """Класс создает экземпляр страницы сайта Линзы (десктопная версия), переменные и методы поиска элеменов
    на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.lens_url()
        driver.get(self.url)

        # Filter elements
        self.filters = driver.find_elements(*ProductLocators.filters)

        # Sort elements
        self.sort_by = driver.find_elements(*ProductLocators.sort_by)

    def filter_click_lens(self, index: int, test_set: list):
        self.driver.find_elements(*ProductLocators.filters)[index].click()
        filter_vals = self.driver.find_elements(*LensLocators.filter_list[index])
        filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        while test_set not in filter_val and test_set != '' and filter_vals != []:
            self.driver.find_element(By.CSS_SELECTOR,
                                     f'div.right-filter-cntrl.js-rf-cntrl-{index}.slick-arrow').click()
            filter_vals = self.driver.find_elements(*LensLocators.filter_list[index])
            filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        if filter_vals != [] and test_set != '':
            i = 0
            while filter_vals[i].get_attribute('title') != test_set:
                i += 1
            filter_vals[i].click()

    def search_result(self) -> [str, str]:
        search_result_brands = self.driver.find_elements(*LensLocators.cards_lens_brand)
        search_result_brand = [search_result_brands[k].text for k in range(len(search_result_brands))]
        search_result_names = self.driver.find_elements(*LensLocators.cards_lens_name)
        search_result_name = [search_result_names[k].text for k in range(len(search_result_names))]
        return search_result_brand, search_result_name

    def search_result_single(self, index: int) -> list:
        search_result = self.driver.find_elements(*LensLocators.card_lens_filters[index])
        search_result = [search_result[k].text for k in range(len(search_result))]
        return search_result

    def filter_prod_not_found(self) -> str:
        return self.driver.find_element(*ProductLocators.card_prod_not_found).text

    def clear_all_filter(self):
        self.driver.find_element(*ProductLocators.clear_all_filters).click()

    def sorted_by_on_page(self, index: int):
        self.driver.find_elements(*ProductLocators.sort_by)[index].click()
        sleep(1)
        # WebDriverWait(self.driver, 10).until(EC.invisibility_of_element()))

    def get_lens_list_on_page(self, amount_card: int) -> [list]:
        lens_price = self.driver.find_elements(*LensLocators.card_lens_price)
        list_price = [int(lens_price[i].text.split()[0]) for i in range(amount_card)]
        return list_price

    @staticmethod
    def rand_lens_card(amount_card: int, amount_rand_card: int) -> list[int]:
        card_num = [randint(0, amount_card)]
        while len(card_num) < amount_rand_card:
            card_num.append(randint(0, amount_card))
            card_num = list(set(card_num))
        card_num.sort()
        return card_num

    def add_cart_lens(self, index: int):
        element = self.driver.find_elements(*ProductLocators.products)[index]
        ActionChains(self.driver).move_to_element(element).perform()
        sleep(0.5)
        self.driver.find_elements(*ProductLocators.products_lens_buy)[index].click()

    def add_param_lens(self, us_set: list) -> float:
        # Страница линзы
        self.driver.find_element(*ProductLensLocators.diff_eyes).click()
        sleep(0.7)
        #
        # WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ProductLensLocators.dioptr_left)).click()
        self.driver.find_element(*ProductLensLocators.dioptr_left).click()
        dioptr_left_list = self.driver.find_elements(*ProductLensLocators.dioptr_left_list)
        self.choise_param(us_set[6][0], dioptr_left_list)
        sleep(0.7)
        #
        self.driver.find_element(*ProductLensLocators.dioptr_right).click()
        dioptr_right_list = self.driver.find_elements(*ProductLensLocators.dioptr_right_list)
        self.choise_param(us_set[6][1], dioptr_right_list)
        sleep(0.7)
        #
        self.driver.find_element(*ProductLensLocators.curv_left).click()
        curv_left_list = self.driver.find_elements(*ProductLensLocators.curv_left_list)
        self.choise_param(us_set[4][0], curv_left_list)
        sleep(0.7)
        #
        self.driver.find_element(*ProductLensLocators.curv_right).click()
        curv_right_list = self.driver.find_elements(*ProductLensLocators.curv_right_list)
        self.choise_param(us_set[4][0], curv_right_list)
        sleep(0.7)
        #
        if len(us_set) == 8:
            self.driver.find_element(*ProductLensLocators.curv_left).click()
            curv_left_list = self.driver.find_elements(*ProductLensLocators.curv_left_list)
            self.choise_param(us_set[7][0], curv_left_list)
            sleep(0.5)
            #
            self.driver.find_element(*ProductLensLocators.curv_right).click()
            curv_right_list = self.driver.find_elements(*ProductLensLocators.curv_right_list)
            self.choise_param(us_set[7][0], curv_right_list)
        #
        self.driver.find_element(*ProductLensLocators.pack_mul_left).click()
        sleep(0.5)
        self.driver.find_element(*ProductLensLocators.pack_mul_right).click()
        #
        add_cart_sum = float(self.driver.find_element(*ProductLensLocators.add_cart_sum).text)
        #
        self.driver.find_element(*ProductLensLocators.buy_btn).click()
        return add_cart_sum
