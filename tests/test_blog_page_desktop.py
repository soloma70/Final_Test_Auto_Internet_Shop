# -*- encoding=utf8 -*-

import pytest
from pages.blog_page import BlogPage


@pytest.mark.smoke
@pytest.mark.positive
def test_news_tags_blog_page(web_driver_desktop):
    """Тест проверяет теги новостей и переход на соответствующие страницы блога с разных страниц тегов"""

    page = BlogPage(web_driver_desktop, 5)
    decl_urls = [page.news_tags[i].get_attribute('href') for i in range(len(page.news_tags))]

    for index, decl_url in enumerate(decl_urls):
        actual_url = page.news_tag_blog(index)
        assert decl_url == actual_url, 'ERROR! Transaction is bad'


@pytest.mark.positive
def test_news_blog_page(web_driver_desktop):
    """Тест проверяет блок новостей и переход на соответствующие страницы блога
    1-ю, среднюю (5) и последнюю (11) страницы, 1-ю, 5-ю и последнюю новость на каждой странице"""

    page = BlogPage(web_driver_desktop, 5)
    # Создаем список URL тестовых страниц
    test_page_urls = page.get_test_pages_urls()
    for page_url in test_page_urls:
        page.get_url(page_url)

        # Создаем список URL тестовых новостей на странице
        test_news_urls = page.list_news_urls(0, 4, -1)
        assert page_url == web_driver_desktop.current_url

        for news_url in test_news_urls:
            page.get_url(news_url)
            assert page.news_name().is_displayed(), 'ERROR! Transaction is bad'


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("index", [-2, 0, 3], ids=['last page', 'first page', 'middle page'])
def test_pagination_blog_page(web_driver_desktop, index):
    """Тест проверяет пагинацию и переход на соответствующие страницы блога"""

    page = BlogPage(web_driver_desktop, 5)
    # Проверка пагинации крайние значения и середина диапазона
    decl_url = page.page_elements()[index].get_attribute('href')
    page.page_elements()[index].click()
    actual_url = web_driver_desktop.current_url
    assert decl_url == actual_url, 'ERROR! Transaction is bad'


@pytest.mark.smoke
@pytest.mark.positive
def test_pagination_arrow_blog_page(web_driver_desktop):
    """Тест проверяет пагинацию и переход на соответствующие страницы блога"""

    page = BlogPage(web_driver_desktop, 5)

    # Получение списка объявленых URL и проверка пагинации кликом стрелки вправо
    decl_urls = [page.pagination[i].get_attribute('href') for i in range(len(page.pagination))]
    for index in range(3):
        page.arrow_right_click()
        actual_url = web_driver_desktop.current_url
        assert decl_urls[index + 1] == actual_url, 'ERROR! Transaction is bad'

    # Переворот списка и проверка пагинации кликом стрелки влево
    decl_urls = decl_urls[2::-1]
    for index in range(3):
        page.arrow_left_click()
        actual_url = web_driver_desktop.current_url
        assert decl_urls[index] == actual_url, 'ERROR! Transaction is bad'
