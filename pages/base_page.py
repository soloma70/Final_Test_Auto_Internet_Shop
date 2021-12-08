from time import sleep
from urllib.parse import urlparse
from random import randint
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.locators import CartLocators, ProductLocators, ProductLensLocators, PaginLocators


class BasePage(object):
    """ Конструктор класса - метод init, получающий объект веб-драйвера, адрес страницы и время ожидания элемента"""

    def __init__(self, driver, url, wait=3):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(wait)

    def win_scroll_begin(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def win_scroll(self):
        self.driver.execute_script("window.scrollTo(0, 3500)")

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_url(self, url: str):
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def find_prod_name(self):
        return self.driver.find_element(*ProductLocators.name)

    def amount_total(self) -> int:
        return int(self.driver.find_element(*ProductLocators.amount_prod).text)

    def amount_page_total(self) -> int:
        return int(self.driver.find_elements(*PaginLocators.pagination)[-1].text)

    def amount_on_page(self) -> int:
        amount_on_page = len(self.driver.find_elements(*ProductLocators.cards_prod_url))
        return amount_on_page

    def amount_page_visible(self) -> int:
        pagination = self.driver.find_elements(*PaginLocators.pagination)
        return len(pagination)

    def get_page_urls(self, index: int) -> [str, str]:
        goto_url = self.driver.find_elements(*PaginLocators.pagination)[index].get_attribute('href')
        self.driver.get(goto_url)
        current_url = self.driver.current_url
        return goto_url, current_url

    def right_arrow_click(self) -> int:
        self.driver.find_element(*PaginLocators.arrow_right).click()
        page_number = int(self.driver.current_url.split('=')[1])
        return page_number

    def left_arrow_click(self) -> int:
        self.driver.find_element(*PaginLocators.arrow_left).click()
        page_number = int(self.driver.current_url.split('=')[1])
        return page_number

    def goto_page(self, num: int) -> str:
        if num == 1:
            goto_url = self.url
        else:
            goto_url = f'{self.url}?page={num}'
        return goto_url

    def save_screen_browser(self, name: str):
        self.driver.save_screenshot(f'screenshots\\{name}.png')

    def amount_cart(self) -> int:
        amount = int(self.driver.find_element(*CartLocators.amount_cart_header).text)
        return amount

    def add_cart_product(self, index: int):
        element = self.driver.find_elements(*ProductLocators.products)[index]
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_elements(*ProductLocators.products_buy)[index].click()
        sleep(2)
        self.driver.find_element(*CartLocators.close_popup_cart).click()
        sleep(1)

    def add_cart_lens_def_par(self, index: int):
        element = self.driver.find_elements(*ProductLocators.products)[index]
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_elements(*ProductLocators.products_lens_buy)[index].click()
        self.driver.find_element(*ProductLensLocators.buy_btn).click()
        self.driver.find_element(*CartLocators.close_popup_cart).click()
        sleep(1)

    @staticmethod
    def rand_prod_page(amount_page: int, amount_rand_page: int, last_page=False) -> list[int]:
        if not last_page:
            page_num = [1]
        else:
            page_num = [1, amount_page]
        while len(page_num) < amount_rand_page + 2:
            page_num.append(randint(0, amount_page))
            page_num = list(set(page_num))
        page_num.sort()
        return page_num

    @staticmethod
    def rand_prod_card(amount: int) -> int:
        index = randint(0, amount)
        return index

    def card_prod_len(self) -> int:
        return len(self.driver.find_elements(*ProductLocators.cards_prod_url))

    def get_prod_list_on_page(self) -> list:
        """ Метод собирает со страницы продукта цены со скидкой (actual) и без скидки (old), формирует список
        из цен old (если две цены) и цен actual (если цена одна). Сортировка на сойте осуществляется по old
        (если две цены) и цен actual (если цена одна)
        Возвращает список цен в соответствии с условиями сортировки"""

        amount = self.card_prod_len()
        list_price = []
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
            except NoSuchElementException:
                old_price = 0
            list_pre.append([old_price, actual_price])

        list_price = []
        for i in range(iter_card):
            if list_pre[i][0] == 0:
                list_price.append(list_pre[i][1])
            else:
                list_price.append(list_pre[i][0])
        return list_price
