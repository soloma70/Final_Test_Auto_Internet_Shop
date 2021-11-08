# -*- encoding=utf8 -*-
import pytest
from time import sleep
from pages.blog_page import BlogPage
from pages.locators import BlogLocators
from pages.url_list import LinsaUa
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.parametrize("index", [-2, 0, 3], ids=['last page', 'first page', 'middle page'])
def test_pagination_blog_page(web_driver_desktop, index):
    """Тест проверяет пагинацию и переход на соответствующие страницы блога"""

    page = BlogPage(web_driver_desktop, 5)

    # Проверка пагинации крайние значения и середина диапазона
    url_pag = web_driver_desktop.find_elements(*BlogLocators.pagination)[index].get_attribute('href')
    web_driver_desktop.find_elements(*BlogLocators.pagination)[index].click()
    sleep(1)
    url_page = web_driver_desktop.current_url
    assert url_pag == url_page, 'ERROR! Transaction is bad'


def test_pagination_arrow_blog_page(web_driver_desktop):
    """Тест проверяет пагинацию и переход на соответствующие страницы блога"""

    page = BlogPage(web_driver_desktop, 5)
    urls = [page.pagination[i].get_attribute('href') for i in range(len(page.pagination))]

    # Проверка пагинации кликом стрелки вправо
    for index in range(3):
        web_driver_desktop.find_element(*BlogLocators.arrow_right).click()
        sleep(1)
        url_page = web_driver_desktop.current_url
        assert urls[index+1] == url_page, 'ERROR! Transaction is bad'

    sleep(2)
    urls = urls[2::-1]
    # Проверка пагинации кликом стрелки вправо
    for index in range(3):
        web_driver_desktop.find_element(*BlogLocators.arrow_left).click()
        sleep(1)
        url_page = web_driver_desktop.current_url
        assert urls[index] == url_page, 'ERROR! Transaction is bad'

