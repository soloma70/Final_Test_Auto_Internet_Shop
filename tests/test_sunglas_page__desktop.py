# -*- encoding=utf8 -*-

import pytest
from pages.test_sets import FramesSets
from pages.sunglass_page import SunglassPage


def test_amount_sunglass_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством очков в наименовании страницы"""

    page = SunglassPage(web_driver_desktop, 3)
    amount_total_sunglass = page.amount_total()
    amount_page_total = page.amount_page_total()
    amount_all_page = 0

    for i in range(amount_page_total):
        amount = page.amount_on_page(i)
        amount_all_page += amount

    assert amount_total_sunglass == amount_all_page, 'ERROR! Incorrect amount lens'


def test_pagination_sunglass_page(web_driver_desktop):
    """Тест проверяет прямой переход по страницам раздела (в пределах 5 страниц), а так же переход с помощью
    стрелок (в пределах 5 страниц) и сравнивает фактический URL с ожидаемым"""

    page = SunglassPage(web_driver_desktop, 5)
    amount_page_test = page.amount_page_visible(page.url)
    # Переход по прямой ссылке
    for i in range(amount_page_test):
        goto_url, current_url = page.get_page_urls(i)
        assert goto_url == current_url and page.find_prod_name().is_displayed(), 'ERROR! Incorrect transaction'

    page.get_url(page.url)
    # Переход кликом на правую стрелку
    for i in range(amount_page_test - 1):
        page_number = page.right_arrow_click()
        assert i + 2 == page_number and page.find_prod_name().is_displayed(), 'ERROR! Incorrect transaction'
    # Переход кликом на левую стрелку
    for i in range(amount_page_test - 2):
        page_number = page.left_arrow_click()
        assert amount_page_test - 1 - i == page_number and page.find_prod_name().is_displayed() \
            , 'ERROR! Incorrect transaction'


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@pytest.mark.parametrize("test_set", [FramesSets.guess, FramesSets.police, FramesSets.ray_ban, FramesSets.sky],
                         ids=[FramesSets.guess[11], FramesSets.police[11], FramesSets.ray_ban[11], FramesSets.sky[11]])
def test_filter_frames_page(web_driver_desktop, test_set):
    """Тест проверяет фильтры на странице и выборку согласно критериям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = SunglassPage(web_driver_desktop, 5)
    filters = page.filters
    filter_list = [fl.text for fl in filters]

    # Добавляем фильтры согласно тестовым наборам и получаем списки фильтров
    for i in range(len(filters)):
        page.filter_click_lens(i, test_set)

    # Получаем результат применения фильтров и сравниваем с тестовым набором
    search_result_brand, search_result_name = page.search_result()
    page.save_screen_browser(f'filter_frames_{test_set[11]}')
    assert search_result_name in test_set and \
           search_result_brand[0] in test_set[11]

    # Очищаем все фильтры
    page.clear_all_filter()


def test_sort_sunglass_page(web_driver_desktop):
    """Тест проверяет сортировку на 1-й, последней и 1-й рандомной странице по возрастанию и снижению цены (с проверкой цен),
    по новизне и популярности, распродажа, делает скриншоты.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = SunglassPage(web_driver_desktop, 10)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 1, True)

    for i in range(3):
        # Переход на страницу сортировки
        page.get_url(page.goto_page(page_num[i]))

        # Сортировка по снижению
        page.sorted_by_on_page(1)
        page.save_screen_browser(f'sort_sunglass_decrease_{i + 1}')
        list_price_decrease = page.get_sunglass_list_on_page()
        list_sort = sorted(list_price_decrease)
        list_sort.sort(reverse=True)
        assert list_price_decrease == list_sort, "ERROR! Position don't sorted"

        # Сортировка по новизне
        page.sorted_by_on_page(3)
        page.save_screen_browser(f'sort_sunglass_novelty_{i + 1}')

        # Сортировка по возрастанию
        page.sorted_by_on_page(2)
        page.save_screen_browser(f'sort_sunglass_increase_{i + 1}')
        list_price_increase = page.get_sunglass_list_on_page()
        list_sort = sorted(list_price_increase)
        assert list_price_increase == list_sort, "ERROR! Position don't sorted"

        # Сортировка по популярности
        page.sorted_by_on_page(0)
        page.save_screen_browser(f'sort_sunglass_popularity_{i + 1}')

        if i == 0:
            # Сортировка по распродаже
            page.sorted_by_on_page(4)
            page.save_screen_browser(f'sort_sunglass_sales_{i + 1}')
            present_banner = page.get_sunglass_list_sale_banner()
            assert all(present_banner), "ERROR! Position don't sorted"


def test_add_in_cart_sunglass_page(web_driver_desktop):
    """Тест проверяет добавление очков одной рандомной позиций с 1, последней и 4-х рандомных страниц,
    добавление в корзину с параметрами по умолчанию """

    page = SunglassPage(web_driver_desktop, 3)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 4, True)
    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()

    for i in range(6):
        page.get_url(page.goto_page(page_num[i]))
        # Получение номеров тестируемых оправ на странице
        frame_num = page.rand_prod_card(page.card_sunglass_len() - 1)
        # Добавление в корзину продукта с параметрами заказа по умолчанию
        page.add_cart_product(frame_num)
        # Получение количества позиций в корзине после добавления оправы
        amount_cart_after = page.amount_cart()
        assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"
        amount_cart_before = amount_cart_after

    page.win_scroll_begin()
    page.save_screen_browser('add_cart_6_sunglasses')

# Добавить тесты выборки по бренду, по полу, длине заушины, ширине мостика, ширине окуляра
