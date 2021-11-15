# -*- encoding=utf8 -*-

import pytest
from pages.test_sets import LensSets
from time import sleep
from pages.lens_page import LensPage


def test_amount_lens_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством линз в наименовании страницы"""

    page = LensPage(web_driver_desktop, 5)
    amount_lens = int(page.amount_total_on_page.text)
    amount_page = int(page.pagination[-1].text)
    amount_total = 0
    for i in range(amount_page):
        amount_total += page.amount_on_page(i)

    assert amount_lens == amount_total, 'ERROR! Incorrect amount lens'


def test_pagination_lens_page(web_driver_desktop):
    """Тест проверяет прямой переход по страницам раздела, а так же переход с помощью стрелок и сравнивает
    фактический URL с ожидаемым"""

    page = LensPage(web_driver_desktop, 5)
    amount_page_url = page.pagination
    # Переход по прямой ссылке
    for i in range(len(amount_page_url)):
        goto_url, current_url = page.get_page_urls(i)
        assert goto_url == current_url and page.find_lens_name().is_displayed(), 'ERROR! Incorrect transaction'

    page = LensPage(web_driver_desktop, 5)
    amount_page_url = page.pagination
    # Переход кликом на правую стрелку
    for i in range(len(amount_page_url) - 1):
        page_number = page.right_arrow_click()
        assert i + 2 == page_number and page.find_lens_name().is_displayed(), 'ERROR! Incorrect transaction'
    # Переход кликом на левую стрелку
    for i in range(len(amount_page_url) - 2):
        page_number = page.left_arrow_click()
        assert (len(amount_page_url) - 1) - i == page_number and page.find_lens_name().is_displayed() \
            , 'ERROR! Incorrect transaction'


@pytest.mark.parametrize("test_set", [LensSets.O2O2, LensSets.sauflon, LensSets.interogo, LensSets.cooper_vision],
                         ids=[LensSets.O2O2[1], LensSets.sauflon[8], LensSets.interogo[8], LensSets.cooper_vision[8]])
def test_filter_lens_page(web_driver_desktop, test_set):
    """Тест проверяет фильтры на странице и выборку согласно критериям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 5)
    filters = page.filters

    # Добавляем фильтры согласно тестовым наборам и получаем списки фильтров
    for i in range(len(filters)):
        page.filter_click_lens(i, test_set)

    # Получаем результат применения фильтров и сравниваем с тестовым набором
    search_result_brand, search_result_name = page.search_result()
    page.save_screen_browser(f'test_filter_lens_{test_set[8]}')
    assert search_result_name[0] in test_set[7] and \
           search_result_brand[0] in test_set[8]

    # Очищаем все фильтры
    page.clear_all_filter()


def test_sort_lens_page(web_driver_desktop):
    """Тест проверяет сортировку на странице по возрастанию и снижению цены (с проверкой цен),
    по новизне и популярности, делает скриншоты.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 10)
    print()
    # Сортировка по снижению
    page.sorted_by_on_page(1)
    sleep(3)
    page.save_screen_browser('test_sort_lens_decrease')
    list_price = page.get_lens_list_on_page()
    list_sort = sorted(list_price)
    list_sort.sort(reverse=True)
    assert list_price == list_sort, "'ERROR! Position don't sorted"
    # Сортировка по новизне
    page.sorted_by_on_page(3)
    sleep(3)
    page.save_screen_browser('test_sort_lens_novelty')
    # Сортировка по возрастанию
    page.sorted_by_on_page(2)
    sleep(3)
    page.save_screen_browser('test_sort_lens_increase')
    list_price = page.get_lens_list_on_page()
    list_sort = sorted(list_price)
    assert list_price == list_sort, "'ERROR! Position don't sorted"
    # Сортировка по популярности
    page.sorted_by_on_page(0)
    sleep(3)
    page.save_screen_browser('test_sort_lens_popularity')


@pytest.mark.parametrize("url_page", ['', '?page=3', '?page=5'], ids=['page 1', 'page 3', 'page 5'])
def test_add_lens_in_cart_lens_page(web_driver_desktop, url_page):
    """Тест проверяет добавление линз с 3-х рандомных позиций с 1-й, 3-й и 5-й карточки, переход на страницу
    линз и добавление их в корзину с параметрами по умолчанию (сложная проверка с изменениями диоптрий,
    кривизны, типа упаковки и количества в отдельных тестах)"""

    page = LensPage(web_driver_desktop, 5)
    page.get_url(f'{page.url}{url_page}')
    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()
    # Получение номеров тестируемых линз на странице
    index = page.rand_lens_card(len(page.cards_lens_url))
    # Добавление в корзину продукта с параметрами заказа по умолчанию
    for i in range(3):
        page.add_cart_lens_def_par(index[i])
        # Получение количества позиций в корзине после добавления линз
        amount_cart_after = page.amount_cart()
        assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"
        amount_cart_before = amount_cart_after
        page.get_url(page.url)
