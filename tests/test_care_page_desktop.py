# -*- encoding=utf8 -*-

import pytest
from pages.test_sets import CareSets
from pages.care_page import CarePage


@pytest.mark.smokie
@pytest.mark.positive
def test_amount_care_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством средств в наименовании страницы"""

    page = CarePage(web_driver_desktop, 3)
    amount_total_care = page.amount_total()
    amount_page_total = page.amount_page_total()
    amount_all_page = 0

    for i in range(amount_page_total):
        if i != 0:
            page.get_url(page.goto_page(i + 1))
        amount = page.amount_on_page()
        amount_all_page += amount

    assert amount_total_care == amount_all_page, 'ERROR! Incorrect amount lens'


@pytest.mark.smokie
@pytest.mark.positive
def test_pagination_care_page(web_driver_desktop):
    """Тест проверяет прямой переход по страницам раздела (в пределах 4 страниц), а так же переход с помощью
    стрелок (в пределах 4 страниц) и сравнивает фактический URL с ожидаемым"""

    page = CarePage(web_driver_desktop, 5)
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


@pytest.mark.positive
@pytest.mark.parametrize("test_set",
                         [CareSets.soleko, CareSets.alcon, CareSets.olmi],
                         ids=[CareSets.soleko[4], CareSets.alcon[4], CareSets.olmi[5]])
def test_positive_filter_care_page(web_driver_desktop, test_set):
    """Тест проверяет фильтры на странице и выборку согласно критериям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = CarePage(web_driver_desktop, 5)

    amount_filters = len(page.filters)
    # Добавляем фильтры согласно тестовым наборам и получаем списки фильтров
    for i in range(amount_filters):
        page.filter_click(i, test_set[i])

    # Делаем скриншот
    page.save_screen_browser(f'filter_pos_care_{test_set[5]}')

    # Получаем результат применения фильтров и сравниваем с тестовым набором
    search_result_brand, search_result_name = page.search_result()

    assert search_result_name == test_set[3] and search_result_brand[0] == test_set[4], \
        f'ERROR! Filtering error or Chek test set {test_set[4]}'

    # Очищаем все фильтры
    page.clear_all_filter()


@pytest.mark.positive
def test_filter_single_positive_care_page(web_driver_desktop):
    """Тест проверяет фильтр на странице отдельно по брендам, объему и типу средства
    и выборку согласно критерию фильтрации (по типу средств не делается).
    В зависимости от прокруток ленты используются до 4 параметров фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = CarePage(web_driver_desktop, 5)

    amount_filter = len(page.filters)
    for i in range(amount_filter):
        filter_set = CareSets.filter_set_positive[i]

        for j in range(len(filter_set)):
            # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
            page.filter_click(i, filter_set[j])
            # Делаем скриншот
            page.save_screen_browser(f'filter_pos_single_care_{filter_set[j]}')
            # Получаем результат применения фильтров и сравниваем с тестовым набором
            if i < 2:
                search_result = page.search_result_single(i)
                assert filter_set[j] in search_result and all(search_result), f'ERROR! Filtering error'

            # Очищаем все фильтры
            page.clear_all_filter()


@pytest.mark.negative
def test_filter_negative_single_care_page(web_driver_desktop):
    """Тест проверяет фильтр на странице по брендам, полу, длинне заушника, ширине мостика и ширине окуляра
    и выборку согласно критерию фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = CarePage(web_driver_desktop, 5)

    amount_filter = len(page.filters)
    for i in range(amount_filter):
        filter_set = CareSets.filter_set_negative[i]

        for j in range(len(filter_set)):
            if filter_set[j]:
                # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
                page.filter_click(i, filter_set[j])
                # Делаем скриншот
                page.save_screen_browser(f'filter_neg_single_care_{filter_set[j]}')
                assert page.filter_prod_not_found() == 'Товаров не найдено', f'ERROR! Filtering error'

                # Очищаем все фильтры
                page.clear_all_filter()


@pytest.mark.positive
def test_sort_care_page(web_driver_desktop):
    """Тест проверяет сортировку на 1-й, последней и одной (1) рандомной странице по возрастанию
    и снижению цены (с проверкой цен), по новизне и популярности, делает скриншоты.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = CarePage(web_driver_desktop, 10)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 1, True)

    for i in range(3):
        # Переход на страницу сортировки (не перегружаем 1-ю страницу)
        if i != 0:
            page.get_url(page.goto_page(page_num[i]))

        # Сортировка по снижению
        page.sorted_by_on_page(1)
        page.save_screen_browser(f'sort_care_decrease_{page_num[i]}')
        list_price_decrease = page.get_care_list_on_page()
        list_sort = sorted(list_price_decrease)
        list_sort.sort(reverse=True)
        assert list_price_decrease == list_sort, "ERROR! Position don't sorted"

        # Сортировка по новизне
        page.sorted_by_on_page(3)
        page.save_screen_browser(f'sort_care_novelty_{page_num[i]}')

        # Сортировка по возрастанию
        page.sorted_by_on_page(2)
        page.save_screen_browser(f'sort_care_increase_{page_num[i]}')
        list_price_increase = page.get_care_list_on_page()
        list_sort = sorted(list_price_increase)
        assert list_price_increase == list_sort, "ERROR! Position don't sorted"

        # Сортировка по популярности
        page.sorted_by_on_page(0)
        page.save_screen_browser(f'sort_care_popularity_{page_num[i]}')


@pytest.mark.smokie
@pytest.mark.positive
def test_add_in_cart_care_page(web_driver_desktop):
    """Тест проверяет добавление одной рандомной позиций с 1, последней и 1-й рандомной страницы,
    добавление в корзину с параметрами по умолчанию """

    page = CarePage(web_driver_desktop, 3)
    # Получение списка рандомной страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 1, True)

    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()

    for i in range(3):
        # Переход на страницу сортировки (не перегружаем 1-ю страницу)
        if i != 0:
            page.get_url(page.goto_page(page_num[i]))
        # Получение номеров продуктов на странице
        care_num = page.rand_prod_card(page.card_prod_len() - 1)

        # Добавление в корзину продукта с параметрами заказа по умолчанию
        page.add_cart_lens_def_par(care_num)
        # Получение количества позиций в корзине после добавления оправы
        amount_cart_after = page.amount_cart()

        assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"
        amount_cart_before = amount_cart_after

    page.win_scroll_begin()
    page.save_screen_browser('add_cart_3_care')
