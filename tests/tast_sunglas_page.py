# -*- encoding=utf8 -*-

import pytest
from pages.test_sets import FramesSets
from pages.sunglass_page import SunglassPage


def test_amount_sunglass_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством очков в наименовании страницы"""

    page = SunglassPage(web_driver_desktop, 3)
    amount_sunglass = int(page.amount_total_on_page.text)
    amount_page = int(page.pagination[-1].text)
    amount_total = 0
    print()
    print(amount_sunglass)

    for i in range(amount_page):
        amount = page.amount_on_page(i)
        amount_total += amount

    print(amount_total)
    assert amount_sunglass == amount_total, 'ERROR! Incorrect amount lens'


def test_pagination_frames_page(web_driver_desktop):
    """Тест проверяет прямой переход по страницам раздела (в пределах 5 страниц), а так же переход с помощью
    стрелок (в пределах 5 страниц) и сравнивает фактический URL с ожидаемым"""

    page = FramesPage(web_driver_desktop, 5)
    amount_page_url = page.pagination
    # Переход по прямой ссылке
    for i in range(len(amount_page_url)):
        goto_url, current_url = page.get_page_urls(i)
        assert goto_url == current_url and page.find_frames_name().is_displayed(), 'ERROR! Incorrect transaction'

    page = FramesPage(web_driver_desktop, 5)
    amount_page_url = page.pagination
    # Переход кликом на правую стрелку
    for i in range(len(amount_page_url) - 1):
        page_number = page.right_arrow_click()
        assert i + 2 == page_number and page.find_frames_name().is_displayed(), 'ERROR! Incorrect transaction'
    # Переход кликом на левую стрелку
    for i in range(len(amount_page_url) - 2):
        page_number = page.left_arrow_click()
        assert (len(amount_page_url) - 1) - i == page_number and page.find_frames_name().is_displayed() \
            , 'ERROR! Incorrect transaction'


@pytest.mark.parametrize("test_set", [FramesSets.guess, FramesSets.police, FramesSets.ray_ban, FramesSets.sky],
                         ids=[FramesSets.guess[11], FramesSets.police[11], FramesSets.ray_ban[11], FramesSets.sky[11]])
def test_filter_frames_page(web_driver_desktop, test_set):
    """Тест проверяет фильтры на странице и выборку согласно критериям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = FramesPage(web_driver_desktop, 5)
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


def test_sort_frames_page(web_driver_desktop):
    """Тест проверяет сортировку на странице по возрастанию и снижению цены (с проверкой цен),
    по новизне и популярности, делает скриншоты.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = FramesPage(web_driver_desktop, 10)
    # Сортировка по снижению
    page.sorted_by_on_page(1)
    page.save_screen_browser('sort_frames_decrease')
    list_price = page.get_frame_list_on_page()
    list_sort = sorted(list_price)
    list_sort.sort(reverse=True)
    assert list_price == list_sort, "'ERROR! Position don't sorted"
    # Сортировка по новизне
    page.sorted_by_on_page(3)
    page.save_screen_browser('sort_frames_novelty')
    # Сортировка по возрастанию
    page.sorted_by_on_page(2)
    page.save_screen_browser('sort_frames_increase')
    list_price = page.get_frame_list_on_page()
    list_sort = sorted(list_price)
    assert list_price == list_sort, "'ERROR! Position don't sorted"
    # Сортировка по популярности
    page.sorted_by_on_page(0)
    page.save_screen_browser('sort_frames_popularity')
    # Сортировка по распродаже
    page.sorted_by_on_page(4)
    page.save_screen_browser('sort_frames_sales')


def test_add_in_cart_frames_page(web_driver_desktop):
    """Тест проверяет добавление оправ 1-й рандомной позиций с 1, последней и 4-х рандомных страниц,
    добавление в корзину с параметрами по умолчанию """

    page = FramesPage(web_driver_desktop, 3)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_frames_page(int(page.pagination[-1].text)-1)
    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()

    for i in range(6):
        page.get_url(page.goto_page(page_num[i]))
        # Получение номеров тестируемых оправ на странице
        frame_num = page.rand_frames_card(page.card_frame_len())
        # Добавление в корзину продукта с параметрами заказа по умолчанию
        page.add_cart_product(frame_num)
        # Получение количества позиций в корзине после добавления оправы
        amount_cart_after = page.amount_cart()
        assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"
        amount_cart_before = amount_cart_after

    page.win_scroll_begin()
    page.save_screen_browser('add_cart_6_frames')


# Добавить тесты выборки по бренду, по полу, длине заушины, ширине мостика, ширине окуляра