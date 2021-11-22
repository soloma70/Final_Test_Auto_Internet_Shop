# -*- encoding=utf8 -*-

import pytest
from pages.test_sets import LensSets, SendOrderSets
from pages.lens_page import LensPage
from pages.cart_page import CartPage


def test_amount_lens_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством линз в наименовании страницы"""

    page = LensPage(web_driver_desktop, 5)
    amount_total_lens = page.amount_total()
    amount_page_total = page.amount_page_total()
    amount_all_page = 0

    for i in range(amount_page_total):
        if i != 0:
            page.get_url(page.goto_page(i + 1))
        amount = page.amount_on_page()
        amount_all_page += amount

    assert amount_total_lens == amount_all_page, 'ERROR! Incorrect amount lens'


def test_pagination_lens_page(web_driver_desktop):
    """Тест проверяет прямой переход по страницам раздела, а так же переход с помощью стрелок и сравнивает
    фактический URL с ожидаемым"""

    page = LensPage(web_driver_desktop, 5)
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


@pytest.mark.parametrize("test_set", [LensSets.O2O2, LensSets.sauflon, LensSets.interogo, LensSets.cooper_vision],
                         ids=[LensSets.O2O2[1], LensSets.sauflon[8], LensSets.interogo[8], LensSets.cooper_vision[8]])
def test_filter_lens_page(web_driver_desktop, test_set):
    """Тест проверяет фильтры на странице и выборку согласно критериям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 5)
    filters = page.filters

    # Добавляем фильтры согласно тестовым наборам и получаем списки фильтров
    for i in range(len(filters)):
        page.filter_click_lens(i, test_set[i])

    # Делаем скриншот
    page.save_screen_browser(f'filter_lens_{test_set[8]}')

    # Получаем результат применения фильтров и сравниваем с тестовым набором
    search_result_brand, search_result_name = page.search_result()
    assert search_result_name[0] == test_set[7] and search_result_brand[0] in test_set[8], \
        f'ERROR! Filtering error or Chek test set {test_set[8]}'

    # Очищаем все фильтры
    page.clear_all_filter()


def test_positive_filter_single_lens_page(web_driver_desktop):
    """Тест проверяет фильтр на странице отдельно по брендам, линейкам, типу линзы, режиму замены, базовой кривизне,
    диаметру и диоптрийности и выборку согласно критерию фильтрации.
    В зависимости от прокруток ленты используются от 2 - 3 параметра фильтрации.
    Проверяються только первые два критерия фильтрации (остальные нет возможности проверить).
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 5)

    for i in range(7):
        filter_set = LensSets.filter_set_positive[i]

        for j in range(len(filter_set)):
            # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
            page.filter_click_lens(i, filter_set[j])
            # Делаем скриншот
            page.save_screen_browser(f'filter_pos_single_lens_{filter_set[j]}')
            # Получаем результат применения 2-х фильтров (по бренду и линейке) и сравниваем с тестовым набором
            if 0 <= i <= 1:
                search_result = ', '.join(page.search_result_single(i)).lower()
                assert filter_set[j].lower() in search_result, f'ERROR! Filtering error'

            # Очищаем все фильтры
            page.clear_all_filter()


def test_negative_filter_single_lens_page(web_driver_desktop):
    """Тест проверяет фильтр на странице отдельно по брендам, линейкам, типу линзы, режиму замены, базовой кривизне,
    диаметру и диоптрийности и выборку согласно критерию фильтрации.
    Комментарий: Отсутствует тестовый набор для проверки, есть линзы по всем категориям фильтрации.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 5)

    for i in range(7):
        filter_set = LensSets.filter_set_negative[i]

        for j in range(len(filter_set)):
            if filter_set[j]:
                # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
                page.filter_click_lens(i, filter_set[j])
                # Делаем скриншот
                page.save_screen_browser(f'filter_neg_single_lens_{filter_set[j]}')
                assert page.filter_prod_not_found() == 'Товаров не найдено', f'ERROR! Filtering error'

                # Очищаем все фильтры
                page.clear_all_filter()


def test_sort_lens_page(web_driver_desktop):
    """Тест проверяет сортировку на 1-й странице по возрастанию и снижению цены (с проверкой цен), по новизне
    и популярности, делает скриншоты. Сортировка организована по ценам за 1 шт.
    Комментарий: Сортировка работает корректно только на 1-й странице для первых 8 позиций, далее не логична.
    Есть линзы, у которых цена указана за несколько штук, но при делении цены на к-во шт. получаем цену за 1 шт.,
    которая находится не на своем месте:
    стр 1, по снижению: [475, 460, 446, 429, 429, 424, 359, 345, 889/3=296, 340, 335, 319, 828/3=276, 314, 305, 304]
    стр 1, по возрастанию: [495, 510, 510, 600, 639, 750, 750, 789, 810, 849, 930, 960, 990, 990, 1080, 1089] - норм.
    Возможен баг!!!
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 10)
    # Получение списка рандомных страниц для теста
    page_num = page.rand_prod_page(page.amount_page_total(), 1, True)

    for i in range(1):
        # Переход на страницу сортировки (не перегружаем 1-ю страницу)
        if i != 0:
            page.get_url(page.goto_page(page_num[i]))

        # Сортировка по снижению
        page.sorted_by_on_page(1)
        page.save_screen_browser(f'sort_lens_decrease_{page_num[i]}')
        list_price_decrease = page.get_lens_list_on_page(8)
        list_sort = sorted(list_price_decrease)
        list_sort.sort(reverse=True)
        assert list_price_decrease == list_sort, "'ERROR! Position don't sorted"

        # Сортировка по новизне
        page.sorted_by_on_page(3)
        page.save_screen_browser(f'sort_lens_novelty_{page_num[i]}')

        # Сортировка по возрастанию
        page.sorted_by_on_page(2)
        page.save_screen_browser(f'sort_lens_increase_{page_num[i]}')
        list_price_increase = page.get_lens_list_on_page(16)
        list_sort = sorted(list_price_increase)
        assert list_price_increase == list_sort, "'ERROR! Position don't sorted"

        # Сортировка по популярности
        page.sorted_by_on_page(0)
        page.save_screen_browser(f'sort_lens_popularity_{page_num[i]}')


def test_add_lens_in_cart_lens_page(web_driver_desktop):
    """Тест проверяет добавление линз с 2-х рандомных позиций с 1-й, 3-й и 5-й карточки, переход на страницу
    линз и добавление их в корзину с параметрами по умолчанию (сложная проверка с изменениями диоптрий,
    кривизны, типа упаковки и количества в отдельных тестах), делает скриншот"""

    page = LensPage(web_driver_desktop, 5)
    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()
    print()
    for j in range(0, 5, 2):
        # Переход на страницу и получение номеров тестируемых линз на странице
        if j != 0:
            page.get_url(page.goto_page(j + 1))

        card_num = page.rand_lens_card(page.amount_on_page(), 3)

        for i in range(2):
            # Добавление в корзину продукта с параметрами заказа по умолчанию
            page.add_cart_lens_def_par(card_num[i] - 1)
            # Получение количества позиций в корзине после добавления линз
            amount_cart_after = page.amount_cart()
            assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"
            amount_cart_before = amount_cart_after
            page.get_url(page.goto_page(j + 1))

    page.win_scroll_begin()
    page.save_screen_browser('add_cart_6_lens')


def test_us_filter_lens_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить..." проверяет фильтр по брендам, линейкам, типу линзы, режиму замены,
    базовой кривизне, диаметру и диоптрийности, сортирует выбранные позиции возрастанию цены,
    выбирает линзы и добавляет в корзину, применяя указанные параметры.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 5)
    us_set = LensSets.filter_set_uc

    for i in range(6):

        for j in range(len(us_set[i])):
            # Добавляем фильтр по бренду согласно тестовому набору и получаем список фильтров
            page.filter_click_lens(i, us_set[i][j])
            # Получаем результат применения 2-х фильтров (по бренду и линейке) и сравниваем с тестовым набором
            if 0 <= i <= 1:
                search_result = ', '.join(page.search_result_single(i)).lower()
                assert us_set[i][j].lower() in search_result, f'ERROR! Filtering error'

    # Сортировка по возрастанию
    page.sorted_by_on_page(2)
    list_price_increase = page.get_lens_list_on_page(page.amount_on_page())
    list_sort = sorted(list_price_increase)
    assert list_price_increase == list_sort, "ERROR! Position don't sorted"

    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()
    # Добавление в корзину 1-го найденого продукта с параметрами в us_set, переход в корзину, получение суммы заказа
    add_cart_sum = page.add_cart_lens(0, us_set)
    # Инициализация экземпляра корзины
    page = CartPage(web_driver_desktop, 5)
    # Получение данных из корзины
    sum_cart_top, sum_cart_bottom, in_cart_prod_sum = page.sum_in_cart()
    # Сравнение суммы выбраных линз и сумм в корзине
    assert add_cart_sum == sum_cart_top and sum_cart_bottom == sum_cart_top and sum_cart_bottom == in_cart_prod_sum
    # Получение данных по линзам из корзины по имени, бренду, sph, bc и сравнение с тестовым набором
    for seq_num in range(len(page.prod_names)):
        prod_name, prod_brand, lens_sph, lens_bc = page.param_lens(seq_num)
        assert us_set[1][0].lower() in prod_name.lower()
        assert us_set[0][0].lower() in prod_brand.lower()
        assert us_set[6][seq_num] in lens_sph
        assert us_set[4][0] in lens_bc

    # Переход на страницу оформления заказа и заполнения всех данных
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.input_delivery_np(SendOrderSets.nova_poshta[0][0], SendOrderSets.nova_poshta[0][1],)




    # page.get_url(page.url)
    # # Получение количества позиций в корзине после добавления линз
    # amount_cart_after = page.amount_cart()
    # page.save_screen_browser(f'uc_add_cart_lens_{us_set[1]}')
    # assert amount_cart_before + 2 == amount_cart_after, "ERROR! Product don't add to cart"
