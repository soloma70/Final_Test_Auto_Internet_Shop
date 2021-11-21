# -*- encoding=utf8 -*-

import pytest
from pages.test_sets import SunglassSets
from pages.sunglass_page import SunglassPage


def test_amount_sunglass_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством очков в наименовании страницы"""

    page = SunglassPage(web_driver_desktop, 3)
    amount_total_sunglass = page.amount_total()
    amount_page_total = page.amount_page_total()
    amount_all_page = 0

    for i in range(amount_page_total):
        if i != 0:
            page.get_url(page.goto_page(i + 1))
        amount = page.amount_on_page()
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


@pytest.mark.parametrize("test_set",
                         [SunglassSets.versace, SunglassSets.police, SunglassSets.ray_ban, SunglassSets.furla,
                          SunglassSets.polaroid],
                         ids=[SunglassSets.versace[9], SunglassSets.police[9], SunglassSets.ray_ban[9],
                              SunglassSets.furla[9], SunglassSets.polaroid[9]])
def test_positive_filter_sg_page(web_driver_desktop, test_set):
    """Тест проверяет фильтры на странице и выборку согласно критериям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = SunglassPage(web_driver_desktop, 5)
    filters = page.filters

    # Убираем всплывающий баннер
    if test_set == SunglassSets.versace:
        page.pass_popup_banner()

    # Добавляем фильтры согласно тестовым наборам и получаем списки фильтров
    for i in range(len(filters)):
        page.filter_click(i, test_set[i])

    # Делаем скриншот
    page.save_screen_browser(f'filter_pos_sg_{test_set[9]}')

    # Получаем результат применения фильтров и сравниваем с тестовым набором
    search_result_brand, search_result_name = page.search_result()
    assert search_result_name == test_set[8] and search_result_brand[0] == test_set[9], \
        f'ERROR! Filtering error or Chek test set {test_set[9]}'

    # Очищаем все фильтры
    page.clear_all_filter()


def test_positive_filter_single_sg_page(web_driver_desktop):
    """Тест проверяет фильтр на странице отдельно по брендам, полу, длинне заушника, ширине мостика и ширине окуляра
    и выборку согласно критерию фильтрации.
    В зависимости от прокруток ленты используются от 5 до 1 параметра фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = SunglassPage(web_driver_desktop, 5)

    for i in range(5):
        filter_set = SunglassSets.filter_set_positive[i]
        # Убираем всплывающий баннер
        if i == 0:
            page.pass_popup_banner()

        for j in range(len(filter_set)):
            # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
            page.filter_click(i, filter_set[j])
            # Делаем скриншот
            page.save_screen_browser(f'filter_pos_single_sg_{filter_set[j]}')
            # Получаем результат применения фильтров и сравниваем с тестовым набором
            search_result = page.search_result_single(i)
            assert filter_set[j] in search_result and all(search_result), f'ERROR! Filtering error'

            # Очищаем все фильтры
            page.clear_all_filter()


def test_negative_filter_single_sg_page(web_driver_desktop):
    """Тест проверяет фильтр на странице по брендам, полу, длинне заушника, ширине мостика и ширине окуляра
    и выборку согласно критерию фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = SunglassPage(web_driver_desktop, 5)

    for i in range(5):
        filter_set = SunglassSets.filter_set_negative[i]
        # Убираем всплывающий баннер
        if i == 0:
            page.pass_popup_banner()

        for j in range(len(filter_set)):
            if filter_set[j]:
                # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
                page.filter_click(i, filter_set[j])
                # Делаем скриншот
                page.save_screen_browser(f'filter_neg_single_sg_{filter_set[j]}')
                assert page.filter_prod_not_found() == 'Товаров не найдено', f'ERROR! Filtering error'

                # Очищаем все фильтры
                page.clear_all_filter()


def test_sort_sunglass_page(web_driver_desktop):
    """Тест проверяет сортировку на 1-й, последней и одной (1) рандомной странице по возрастанию
    и снижению цены (с проверкой цен), по новизне и популярности, распродажа (только на 1-й странице,
    дальше при сортировке включается позиции без распродажи???), делает скриншоты.
    Комментарий: Сортировка организована по ценам без учета скидки (old price) - баг или фича?
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = SunglassPage(web_driver_desktop, 10)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 1, True)

    for i in range(3):
        # Переход на страницу сортировки (не перегружаем 1-ю страницу)
        if i != 0:
            page.get_url(page.goto_page(page_num[i]))

        # Сортировка по снижению
        page.sorted_by_on_page(1)
        page.save_screen_browser(f'sort_sg_decrease_{page_num[i]}')
        list_price_decrease = page.get_prod_list_on_page()
        list_sort = sorted(list_price_decrease)
        list_sort.sort(reverse=True)
        assert list_price_decrease == list_sort, "ERROR! Position don't sorted"

        # Сортировка по новизне
        page.sorted_by_on_page(3)
        page.save_screen_browser(f'sort_sg_novelty_{page_num[i]}')

        # Сортировка по возрастанию
        page.sorted_by_on_page(2)
        page.save_screen_browser(f'sort_sg_increase_{page_num[i]}')
        list_price_increase = page.get_prod_list_on_page()
        list_sort = sorted(list_price_increase)
        assert list_price_increase == list_sort, "ERROR! Position don't sorted"

        # Сортировка по популярности
        page.sorted_by_on_page(0)
        page.save_screen_browser(f'sort_sg_popularity_{page_num[i]}')

        if i == 0:
            # Сортировка по распродаже
            page.sorted_by_on_page(4)
            page.save_screen_browser(f'sort_sg_sales_{page_num[i]}')
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
    page.save_screen_browser('add_cart_6_sg')


def test_us_filter_sg_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить..." проверяет фильтр по брендам, полу, длинне заушника, ширине мостика и ширине окуляра,
    сортирует выбранные позиции возрастанию цены, выбирает рандомные очки и добавляет в корзину.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = SunglassPage(web_driver_desktop, 5)

    for i in range(5):
        filter_set = SunglassSets.filter_set_uc[i]
        # Убираем всплывающий баннер
        if i == 0:
            page.pass_popup_banner()

        for j in range(len(filter_set)):
            # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
            page.filter_click(i, filter_set[j])
            # Получаем результат применения фильтров и сравниваем с тестовым набором
            search_result_brand = page.search_result_single(i)
            assert filter_set[j] in search_result_brand and all(search_result_brand), f'ERROR! Filtering error'

            # Сортировка по возрастанию
            page.sorted_by_on_page(2)
            list_price_increase = page.get_prod_list_on_page()
            list_sort = sorted(list_price_increase)
            assert list_price_increase == list_sort, "ERROR! Position don't sorted"

            # Получение количества позиций в корзине перед добавлением
            amount_cart_before = page.amount_cart()
            # Получение номеров тестируемых оправ на странице
            frame_num = page.rand_prod_card(page.card_prod_len() - 1)
            # Добавление в корзину продукта с параметрами заказа по умолчанию
            page.add_cart_product(frame_num)
            # Получение количества позиций в корзине после добавления оправы
            amount_cart_after = page.amount_cart()
            assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"
            amount_cart_before = amount_cart_after

            page.win_scroll_begin()
            page.save_screen_browser(f'uc_add_cart_found_fr_{filter_set[j]}')

            # Очищаем все фильтры
            page.clear_all_filter()
