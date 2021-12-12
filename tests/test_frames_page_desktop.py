# -*- encoding=utf8 -*-

import pytest
from pages.test_sets import FramesSets
from pages.product_page import ProductPage


@pytest.mark.smoke
@pytest.mark.positive
def test_amount_frames_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством оправ в наименовании страницы"""

    page = ProductPage(web_driver_desktop, 'fr', 3)
    amount_total_frames = page.amount_total()
    amount_page_total = page.amount_page_total()
    amount_all_page = 0

    for i in range(amount_page_total):
        if i != 0:
            page.get_url(page.goto_page(i + 1))
        amount = page.amount_on_page()
        amount_all_page += amount

    assert amount_total_frames == amount_all_page, 'ERROR! Incorrect amount lens'


@pytest.mark.smoke
@pytest.mark.positive
def test_pagination_frames_page(web_driver_desktop):
    """Тест проверяет прямой переход по страницам раздела (в пределах 5 страниц), а так же переход с помощью
    стрелок (в пределах 5 страниц) и сравнивает фактический URL с ожидаемым"""

    page = ProductPage(web_driver_desktop, 'fr')
    amount_page_test = page.amount_page_visible()
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


@pytest.mark.positive
@pytest.mark.parametrize("test_set", [FramesSets.sky, FramesSets.guess, FramesSets.police, FramesSets.ray_ban],
                         ids=[FramesSets.sky[6], FramesSets.guess[6], FramesSets.police[6], FramesSets.ray_ban[6]])
def test_filter_frames_page(web_driver_desktop, test_set):
    """Тест проверяет фильтры на странице и выборку согласно критериям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'fr')

    amount_filter = len(page.filters)
    # Добавляем фильтры согласно тестовым наборам и получаем списки фильтров
    for i in range(amount_filter):
        page.filter_click(i, test_set[i], 'fr')

    # Делаем скриншот
    page.save_screen_browser(f'filter_fr_{test_set[6]}')

    # Получаем результат применения фильтров и сравниваем с тестовым набором
    search_result_brand, search_result_name = page.search_result()
    assert test_set[5][0] in search_result_name and test_set[
        6] in search_result_brand, f'ERROR! Filtering error or Chek test set {test_set[6]}'

    # Очищаем все фильтры
    page.clear_all_filter()


@pytest.mark.positive
def test_filter_single_positive_fr_page(web_driver_desktop):
    """Тест проверяет фильтр на странице отдельно по брендам, полу, длинне заушника, ширине мостика и ширине окуляра
    и выборку согласно критерию фильтрации.
    В зависимости от прокруток ленты используются от 5 до 1 параметра фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'fr')

    for i, filter_sets in enumerate(FramesSets.filter_set_positive):

        for _, filter_set in enumerate(filter_sets):
            # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
            page.filter_click(i, filter_set, 'fr')
            # Делаем скриншот
            page.save_screen_browser(f'filter_pos_single_fr_{filter_set}')
            # Получаем результат применения фильтров и сравниваем с тестовым набором
            search_result = page.search_result_single(i)
            assert filter_set in search_result and all(search_result), 'ERROR! Filtering error'

            # Очищаем все фильтры
            page.clear_all_filter()


@pytest.mark.negative
def test_filter_single_negative_fr_page(web_driver_desktop):
    """Тест проверяет фильтр на странице по брендам, полу, длинне заушника, ширине мостика и ширине окуляра
    и выборку согласно критерию фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'fr')

    for i, filter_sets in enumerate(FramesSets.filter_set_negative):

        for _, filter_set in enumerate(filter_sets):
            if filter_set:
                # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
                page.filter_click(i, filter_set, 'fr')
                # Делаем скриншот
                page.save_screen_browser(f'filter_neg_single_fr_{filter_set}')
                assert page.filter_prod_not_found() == 'Товаров не найдено', 'ERROR! Filtering error'

                # Очищаем все фильтры
                page.clear_all_filter()


@pytest.mark.positive
def test_sort_frames_page(web_driver_desktop):
    """Тест проверяет сортировку на 1-й, последней и одной (1) рандомной странице по возрастанию и снижению цены
    (с проверкой цен), по новизне и популярности, распродажа (только на 1-й странице, дальше при сортировке включается
    позиции без распродажи???), делает скриншоты.
    Комментарий: Сортировка организована по ценам без учета скидки (old price) - баг или фича?
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'fr', 10)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 1, True)
    # page_num = [1, 45, 66]
    for i in range(3):
        # Переход на страницу сортировки (не перегружаем 1-ю страницу)
        if i != 0:
            page.get_url(page.goto_page(page_num[i]))

        # Сортировка по снижению
        page.sorted_by_on_page(1)
        page.save_screen_browser(f'sort_frames_decrease_{page_num[i]}')
        list_price_decrease = page.get_prod_list_on_page()
        list_sort = sorted(list_price_decrease)
        list_sort.sort(reverse=True)
        assert list_price_decrease == list_sort, "ERROR! Position don't sorted"

        # Сортировка по новизне
        page.sorted_by_on_page(3)
        page.save_screen_browser(f'sort_frames_novelty_{page_num[i]}')

        # Сортировка по возрастанию
        page.sorted_by_on_page(2)
        page.save_screen_browser(f'sort_frames_increase_{page_num[i]}')
        list_price_increase = page.get_prod_list_on_page()
        list_sort = sorted(list_price_increase)
        print('-' * 20)
        print(list_price_increase)
        print(list_sort)
        assert list_price_increase == list_sort, "ERROR! Position don't sorted"

        # Сортировка по популярности
        page.sorted_by_on_page(0)
        page.save_screen_browser(f'sort_frames_popularity_{page_num[i]}')

        if i == 0:
            # Сортировка по распродаже
            page.sorted_by_on_page(4)
            page.save_screen_browser(f'sort_frames_sales_{page_num[i]}')
            present_banner = page.get_product_list_sale_banner()
            assert any(present_banner), "ERROR! Position don't sorted"


@pytest.mark.smoke
@pytest.mark.positive
def test_add_in_cart_frames_page(web_driver_desktop):
    """Тест проверяет добавление оправ 1-й рандомной позиций с 1, последней и 4-х рандомных страниц,
    добавление в корзину с параметрами по умолчанию """

    page = ProductPage(web_driver_desktop, 'fr', 3)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 4, True)
    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()

    for i in range(6):
        # Переход на страницу сортировки (не перегружаем 1-ю страницу)
        if i != 0:
            page.get_url(page.goto_page(page_num[i]))
        # Получение номеров тестируемых оправ на странице
        frame_num = page.rand_prod_card(page.card_prod_len() - 1)
        # Добавление в корзину продукта с параметрами заказа по умолчанию
        page.add_cart_product(frame_num)
        # Получение количества позиций в корзине после добавления оправы
        amount_cart_after = page.amount_cart()
        assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"
        amount_cart_before = amount_cart_after

    page.win_scroll_begin()
    page.save_screen_browser('add_cart_6_frames')
