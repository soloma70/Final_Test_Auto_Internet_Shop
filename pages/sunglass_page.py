from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import SunglassLocators, ProductLocators
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class SunglassPage(BasePage):
    """Класс создает экземпляр страницы сайта Сонцезащитные очки (десктопная версия), переменные и методы
    поиска элеменов на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.sunglass_url()
        driver.get(self.url)

        # Filter elements
        self.filters = driver.find_elements(*SunglassLocators.filters)

        # Sort elements
        self.sort_by = driver.find_elements(*SunglassLocators.sort_by)

    def amount_on_page(self, index: int) -> int:
        self.driver.get(super().goto_page(index + 1))
        amount_on_page = len(self.driver.find_elements(*ProductLocators.cards_prod_url))
        return amount_on_page

    def filter_click_lens(self, index: int, test_set: list) -> list:
        self.driver.find_elements(*SunglassLocators.filters)[index].click()
        filter_vals = self.driver.find_elements(*SunglassLocators.filter_list[index])
        filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        if test_set[index] not in filter_val and test_set[index] != '' and filter_vals != []:
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,
                                     f'div.right-filter-cntrl.js-rf-cntrl-{index + 1}.slick-arrow').click()
            filter_vals = self.driver.find_elements(*SunglassLocators.filter_list[index])
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
        search_result_brands = self.driver.find_elements(*ProductLocators.cards_prod_brand)
        search_result_brand = [search_result_brands[k].text for k in range(len(search_result_brands))]
        search_result_names = self.driver.find_elements(*ProductLocators.cards_prod_name)
        search_result_name = [search_result_names[k].text for k in range(len(search_result_names))]
        return search_result_brand, search_result_name

    def clear_all_filter(self):
        self.driver.find_element(*SunglassLocators.clear_all_filters).click()

    def sorted_by_on_page(self, index: int):
        self.driver.find_elements(*SunglassLocators.sort_by)[index].click()
        sleep(2)

    def card_sunglass_len(self) -> int:
        return len(self.driver.find_elements(*ProductLocators.cards_prod_url))

    def get_sunglass_list_on_page(self) -> list:
        """ Метод собирает со страницы продукта цены со скидкой (actual) и без скидки (old), формирует список
        из цен old (если две цены) и цен actual (если цена одна). Сортировка на сойте осуществляется по old
        (если две цены) и цен actual (если цена одна)
        Возвращает список цен в соответствии с условиями сортировки"""

        amount = self.card_sunglass_len()
        if amount <= 8:
            list_price = self.part_card_price(
                amount, ProductLocators.block_1, ProductLocators.price_act, ProductLocators.price_old)
        if amount > 8:
            list_price = self.part_card_price(
                8, ProductLocators.block_1, ProductLocators.price_act, ProductLocators.price_old)
            list_price += self.part_card_price(
                amount - 8, ProductLocators.block_2, ProductLocators.price_act, ProductLocators.price_old)
        return list_price

    def part_card_price(self, iter_card: int, block: str, price_act: str, price_old: str) -> list:
        """ Метод формирует список цен на продукты со страницы продукта. Так как некоторые цены отсутствуют у продукта,
        применяется блок try-except для обработки исключения, предотвращения аварийного завершения кода
        и формирования правильного списка цен"""

        list_pre = []
        for i in range(iter_card):
            full_price_act = f'{block} > div:nth-child({i + 1}) > {price_act}'
            full_price_old = f'{block} > div:nth-child({i + 1}) > {price_old}'
            actual_price = int(self.driver.find_element(By.CSS_SELECTOR, full_price_act).text.split()[0])
            try:
                old_price = int(self.driver.find_element(By.CSS_SELECTOR, full_price_old).text.split()[0])
            except:
                old_price = 0
            list_pre.append([old_price, actual_price])

        list_price = []
        for i in range(iter_card):
            if list_pre[i][0] == 0:
                list_price.append(list_pre[i][1])
            else:
                list_price.append(list_pre[i][0])
        return list_price

    def get_sunglass_list_sale_banner(self) -> list:
        """ Метод собирает со страницы продукта наличие/отсутсвие баннера с % скидки, формирует и возвращает
        список True/False"""

        amount = self.card_sunglass_len()
        if amount <= 8:
            list_banner = self.part_card_banner(
                amount, ProductLocators.block_1, ProductLocators.sale_banner)
        if amount > 8:
            list_banner = self.part_card_banner(
                8, ProductLocators.block_1, ProductLocators.sale_banner)
            list_banner += self.part_card_banner(
                amount - 8, ProductLocators.block_2, ProductLocators.sale_banner)
        return list_banner

    def part_card_banner(self, iter_card: int, block: str, banner: str) -> list:
        """ Метод формирует список True/False в зависимости от того, есть баннер скидки у продукта или нет.
        Так как у некоторых продуктов может не быть баннера, применяется блок try-except для обработки исключения,
        предотвращения аварийного завершения кода и формирования правильного списка"""

        list_banner = []
        for i in range(iter_card):
            sale_banner = f'{block} > div:nth-child({i + 1}) > {banner}'
            try:
                sale_banner = self.driver.find_element(By.CSS_SELECTOR, sale_banner).is_displayed()
            except:
                sale_banner = False
            list_banner.append(sale_banner)
        return list_banner
