from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import SunglassLocators, ProductLocators
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def pass_popup_banner(self):
        self.driver.find_elements(*SunglassLocators.filters)[0].click()

        # sleep(6)
        # self.driver.find_element(By.CSS_SELECTOR,
        #                       'div.close-btn-x-new-dot.click-lgwg-dot-close-lock.animClass03').click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(By.ID('visualBlockWidgetLGWGPopff808d04311853ba8d1fa98b93462108')))
        self.driver.get(self.url)

    def filter_click(self, index: int, test_set: str):
        self.driver.find_elements(*SunglassLocators.filters)[index].click()
        filter_vals = self.driver.find_elements(*SunglassLocators.filter_list[index])
        filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        while test_set not in filter_val and test_set != '' and filter_vals != []:
            self.driver.find_element(By.CSS_SELECTOR,
                                     f'div.right-filter-cntrl.js-rf-cntrl-{index + 1}.slick-arrow').click()
            filter_vals = self.driver.find_elements(*SunglassLocators.filter_list[index])
            filter_val = [filter_vals[k].get_attribute('title') for k in range(len(filter_vals))]

        if filter_vals != [] and test_set != '':
            i = 0
            while filter_vals[i].get_attribute('title') != test_set:
                i += 1
            else:
                filter_vals[i].click()

    def search_result(self) -> [list, list]:
        search_result_brands = self.driver.find_elements(*ProductLocators.cards_prod_brand)
        search_result_brand = [search_result_brands[k].text for k in range(len(search_result_brands))]
        search_result_names = self.driver.find_elements(*ProductLocators.cards_prod_name)
        search_result_name = [search_result_names[k].text for k in range(len(search_result_names))]
        return search_result_brand, search_result_name

    def clear_all_filter(self):
        self.driver.find_element(*ProductLocators.clear_all_filters).click()

    def sorted_by_on_page(self, index: int):
        self.driver.find_elements(*SunglassLocators.sort_by)[index].click()
        sleep(2)



    def get_sunglass_list_sale_banner(self) -> list:
        """ Метод собирает со страницы продукта наличие/отсутсвие баннера с % скидки, формирует и возвращает
        список True/False"""

        amount = self.card_prod_len()
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
            except NoSuchElementException:
                sale_banner = False
            list_banner.append(sale_banner)
        return list_banner
