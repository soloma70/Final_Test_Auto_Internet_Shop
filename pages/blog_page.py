from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import BlogLocators


class BlogPage(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        self.url = LinsaUa.blog_url()
        driver.get(self.url)

        # Header elements
        self.start_img = driver.find_element(*BlogLocators.logo_img)

        # News tegs
        self.news_tags = driver.find_elements(*BlogLocators.news_tags)
        self.news = driver.find_elements(*BlogLocators.news)
        self.pagination = driver.find_elements(*BlogLocators.pagination)

    def news_tag_blog(self, index: int) -> str:
        self.driver.find_elements(*BlogLocators.news_tags)[index].click()
        return self.driver.current_url

    def get_test_pages_urls(self) -> list:
        page_elem = self.pagination
        first_page_num = int(page_elem[0].text)
        last_page_num = int(page_elem[-2].text)
        middle_page_num = (last_page_num - first_page_num) // 2
        test_page_urls = [
            page_elem[0].get_attribute('href'),
            f"{page_elem[0].get_attribute('href')}?page={middle_page_num}",
            page_elem[-2].get_attribute('href')
        ]
        return test_page_urls

    def list_news_urls(self, a: int, b: int, c: int) -> list:
        urls = [
            self.driver.find_elements(*BlogLocators.news)[a].get_attribute('href'),
            self.driver.find_elements(*BlogLocators.news)[b].get_attribute('href'),
            self.driver.find_elements(*BlogLocators.news)[c].get_attribute('href')
        ]
        return urls

    def news_name(self) -> WebElement:
        element = self.driver.find_element(*BlogLocators.news_name)
        return element

    def page_elements(self):
        return self.pagination

    def arrow_right_click(self):
        self.driver.find_element(*BlogLocators.arrow_right).click()
        sleep(1)

    def arrow_left_click(self):
        self.driver.find_element(*BlogLocators.arrow_left).click()
        sleep(1)
