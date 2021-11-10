# -*- encoding=utf8 -*-
import pytest
from time import sleep
from pages.blog_page import BlogPage
from pages.locators import BlogLocators


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
    1-ю, среднюю (5) и последнюю (11) страницы, 1-ю, 5-ю и 9-ю новость на каждой странице"""

    page = BlogPage(web_driver_desktop, 5)
    # Из селектора новостей получаем номера 1-й и последней страницы, вычисляем среднюю страницу
    first_page_num = int(page.pagination[0].text)
    last_page_num = int(page.pagination[-2].text)
    middle_page_num = (last_page_num - first_page_num) // 2
    # Создаем список URL тестовых страниц
    test_page_urls = [
        page.pagination[0].get_attribute('href'),
        f"{page.pagination[0].get_attribute('href')}?page={middle_page_num}",
        page.pagination[-2].get_attribute('href')
    ]
    for k in range(3):
        web_driver_desktop.get(test_page_urls[k])
        sleep(1)
        # Создаем список URL тестовых новостей на странице
        test_news_urls = [
            web_driver_desktop.find_elements(*BlogLocators.news)[0].get_attribute('href'),
            web_driver_desktop.find_elements(*BlogLocators.news)[4].get_attribute('href'),
            web_driver_desktop.find_elements(*BlogLocators.news)[-1].get_attribute('href')
        ]
        assert test_page_urls[k] == web_driver_desktop.current_url
        for i in range(3):
            web_driver_desktop.get(test_news_urls[i])
            sleep(1)
            assert web_driver_desktop.find_element(*BlogLocators.news_name).is_displayed(), 'ERROR! Transaction is bad'


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


def test_pagination_arrow_blog_page(web_driver_desktop):
    """Тест проверяет пагинацию и переход на соответствующие страницы блога"""

    page = BlogPage(web_driver_desktop, 5)
    decl_urls = [page.pagination[i].get_attribute('href') for i in range(len(page.pagination))]

    # Проверка пагинации кликом стрелки вправо
    for index in range(3):
        web_driver_desktop.find_element(*BlogLocators.arrow_right).click()
        sleep(1)
        actual_url = web_driver_desktop.current_url
        assert decl_urls[index + 1] == actual_url, 'ERROR! Transaction is bad'

    sleep(2)
    decl_urls = decl_urls[2::-1]
    # Проверка пагинации кликом стрелки вправо
    for index in range(3):
        web_driver_desktop.find_element(*BlogLocators.arrow_left).click()
        sleep(1)
        actual_url = web_driver_desktop.current_url
        assert decl_urls[index] == actual_url, 'ERROR! Transaction is bad'
