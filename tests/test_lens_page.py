# -*- encoding=utf8 -*-
import pytest
from pages.test_sets import LensSets
from time import sleep
from pages.lens_page import LensPage
from pages.locators import LensLocators, ProductLensLocators
from pages.url_list import LinsaUa
from selenium.webdriver.common.action_chains import ActionChains


def test_amount_lens_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством линз в наименовании страницы"""

    page = LensPage(web_driver_desktop, 5)
    amount_lens = int(page.amount_total.text)
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
        assert goto_url == current_url and web_driver_desktop.find_element(*LensLocators.name).is_displayed() \
            , 'ERROR! Incorrect transaction'

    page = LensPage(web_driver_desktop, 5)
    amount_page_url = page.pagination
    # Переход кликом на правую стрелку
    for i in range(len(amount_page_url) - 1):
        page_number = page.right_arrow_click()
        assert i + 2 == page_number and web_driver_desktop.find_element(*LensLocators.name).is_displayed() \
            , 'ERROR! Incorrect transaction'
    # Переход кликом на левую стрелку
    for i in range(len(amount_page_url) - 2):
        page_number = page.left_arrow_click()
        assert (len(amount_page_url) - 1) - i == page_number and web_driver_desktop.find_element(
            *LensLocators.name).is_displayed() \
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


    # # Получаем результат применения фильтров и сравниваем с тестовым набором
    # search_result_brand, search_result_name = page.search_result()
    # assert search_result_name[0] in test_set[7] and \
    #        search_result_brand[0] in test_set[8]
    #
    # # Очищаем все фильтры
    # page.clear_all_filter()
    #
    # for k in range(len(filter_list)):
    #      = web_driver_desktop.find_elements(*L)
    #
    #
    #
    #     for j in range(len(filter_list[k])):
    #         print(filter_list[k][j].get_attribute('href'))

    #
    # for l in range(len(sort_by)):
    #     print(sort_by[l].get_attribute('href'))

    # cards_lens_url = page.cards_lens_url
    # card_lens_amount = page.card_lens_amount
    # card_lens_price = page.card_lens_price
    # print(len(cards_lens_url))
    # print(len(card_lens_amount))
    # print(len(card_lens_price))
    #
    # # Проверка функции сортировки
    # # Сортировка по убыванию, сортировка по возрастанию
    #
    # sort_by = page.sort_by
    # url_list_sort_by = []
    # for i in range(len(sort_by)):
    #     web_driver_desktop.find_elements(*LensLocators.sort_by)[i].click()
    #     sleep(2)
    #
    #     url_list = web_driver_desktop.find_elements(*LensLocators.cards_lens_url)
    #     url_list_act = []
    #     for j in range(len(url_list)):
    #         url = web_driver_desktop.find_elements(*LensLocators.cards_lens_url)[j].get_attribute('href')
    #         url_list_act.append(url)
    #
    #     url_list_sort_by.append(url_list_act)
    #
    # print(url_list_sort_by[0])
    # print(url_list_sort_by[1])
    # print(url_list_sort_by[2])
    # print(url_list_sort_by[3])
