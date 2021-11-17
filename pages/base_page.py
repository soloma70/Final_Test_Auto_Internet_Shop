from time import sleep
from urllib.parse import urlparse
from selenium.webdriver import ActionChains
from pages.locators import CartLocators, ProductLocators, ProductLensLocators, PaginLocators
from random import randint


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

    def find_prod_name(self):
        return self.driver.find_element(*ProductLocators.name)

    def amount_total(self) -> int:
        return int(self.driver.find_element(*ProductLocators.amount_prod).text)

    def amount_page_total(self) -> int:
        return int(self.driver.find_elements(*PaginLocators.pagination)[-1].text)

    def amount_page_visible(self, url: str) -> int:
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
            goto_url =  f'{self.url}?page={num}'
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

    def rand_prod_page(self, amount: int) -> list[int]:
        page_num = [1, amount]
        for i in range(4):
            page_num.append(randint(2, amount - 1))
            while page_num[-2] == page_num[-1]:
                page_num.append(randint(2, amount - 1))
        page_num.sort()
        return page_num

    def rand_prod_card(self, amount: int) -> int:
        index = randint(0, amount)
        return index