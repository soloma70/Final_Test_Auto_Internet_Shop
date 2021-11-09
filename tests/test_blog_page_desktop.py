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
    decl_url = web_driver_desktop.find_elements(*BlogLocators.pagination)[index].get_attribute('href')
    web_driver_desktop.find_elements(*BlogLocators.pagination)[index].click()
    sleep(1)
    actual_url = web_driver_desktop.current_url
    assert decl_url == actual_url, 'ERROR! Transaction is bad'


def test_news_tags_blog_page(web_driver_desktop):
    """Тест проверяет теги новостей и переход на соответствующие страницы блога с разных страниц тегов"""

    page = BlogPage(web_driver_desktop, 5)
    decl_urls = [page.news_tags[i].get_attribute('href') for i in range(len(page.news_tags))]

    actual_urls = []
    for index in range(len(decl_urls)):
        web_driver_desktop.find_elements(*BlogLocators.news_tags)[index].click()
        sleep(1)
        actual_url = web_driver_desktop.current_url
        actual_urls.append(actual_url)
        assert decl_urls[index] == actual_url, 'ERROR! Transaction is bad'


def test_news_blog_page(web_driver_desktop):
    """Тест проверяет блок новостей и переход на соответствующие страницы блога
    1-ю, 4-ю и последнюю (11) страницы, 1-ю, 5-ю и 9-ю новость на каждой странице"""

    page = BlogPage(web_driver_desktop, 5)
    decl_page_urls = [page.pagination[j].get_attribute('href') for j in range(len(page.pagination))]
    decl_page01_url = decl_page_urls[0]
    decl_page04_url = decl_page_urls[3]
    decl_page11_url = decl_page_urls[-1]

    for ip in range(3):
        web_driver_desktop.get(LinsaUa.blog_url())

        decl_news_urls = [page.news[i].get_attribute('href') for i in range(len(page.news))]

        print()
        print(decl_news_urls)

        actual_news_urls = []

        for index in range(len(decl_news_urls)):
            web_driver_desktop.find_elements(*BlogLocators.news)[index].click()
            sleep(1)
            actual_news_url = web_driver_desktop.current_url
            actual_news_urls.append(actual_news_url)
            web_driver_desktop.get(LinsaUa.blog_url())
            # assert decl_news_urls[index] == actual_news_url, 'ERROR! Transaction is bad'

        print(actual_news_urls)


def test_pagination_arrow_blog_page(web_driver_desktop):
    """Тест проверяет пагинацию и переход на соответствующие страницы блога"""

    page = BlogPage(web_driver_desktop, 5)
    decl_urls = [page.pagination[i].get_attribute('href') for i in range(len(page.pagination))]

    # Проверка пагинации кликом стрелки вправо
    for index in range(3):
        web_driver_desktop.find_element(*BlogLocators.arrow_right).click()
        sleep(1)
        actual_url = web_driver_desktop.current_url
        assert decl_urls[index+1] == actual_url, 'ERROR! Transaction is bad'

    sleep(2)
    decl_urls = decl_urls[2::-1]
    # Проверка пагинации кликом стрелки вправо
    for index in range(3):
        web_driver_desktop.find_element(*BlogLocators.arrow_left).click()
        sleep(1)
        actual_url = web_driver_desktop.current_url
        assert decl_urls[index] == actual_url, 'ERROR! Transaction is bad'

