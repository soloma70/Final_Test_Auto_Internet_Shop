# -*- encoding=utf8 -*-

import pytest
from pages.care_page import CarePage
from pages.product_page import ProductPage
from pages.lens_page import LensPage
from pages.cart_page import CartPage
from pages.test_sets import LensSets, SendOrderSets, FramesSets, SunglassSets, CareSets


@pytest.mark.functional
@pytest.mark.positive
def test_us_filter_lens_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить линзы бренда INTEROJO, линейки Fusion, левая -4.00, правая -2.75"
    осуществляет поиск по брендам, линейкам, типу линзы, режиму замены, базовой кривизне, диаметру и диоптрийности,
    сортирует выбранные позиции возрастанию цены, выбирает линзы и добавляет в корзину, применяя указанные параметры.
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
    page = CartPage(web_driver_desktop, 10)
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
    page.save_screen_browser(f'us_1_cart_chekout_{us_set[0][0]}')
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.save_screen_browser(f'us_2_data_chekout_{us_set[0][0]}')
    page.goto_delivery()
    page.input_delivery_np(SendOrderSets.nova_poshta[0][0], SendOrderSets.nova_poshta[0][1])
    page.save_screen_browser(f'us_3_delivery_chekout_{us_set[0][0]}')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser(f'us_4_pay_chekout_{us_set[0][0]}')
    page.goto_benefit()
    page.save_screen_browser(f'us_5_confitm_chekout_{us_set[0][0]}')


@pytest.mark.integration
@pytest.mark.positive
def test_us_filter_fr_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить оправу бренда CARRERA, мужскую, длина заушника/ширина мостика/ширина окуляра
    145/20/50" осуществляет поиск по брендам, полу, длинне заушника, ширине мостика и ширине окуляра,
    сортирует выбранные позиции возрастанию цены, выбирает рандомную из найденных оправ и добавляет в корзину.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'fr')

    us_set = FramesSets.filter_set_uc
    for i in range(len(us_set)):

        # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
        page.filter_click(i, us_set[i], 'fr')
        # Получаем результат применения фильтров и сравниваем с тестовым набором
        search_result_brand = page.search_result_single(i)
        if us_set[i] != '':
            assert us_set[i] in search_result_brand, f'ERROR! Filtering error'

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

    page.save_screen_browser(f'uc_add_cart_fr_{us_set[0]}')

    # Очищаем все фильтры
    page.clear_all_filter()

    # Инициализация экземпляра корзины
    page = CartPage(web_driver_desktop, 10)
    # Получение данных из корзины
    sum_cart_top, sum_cart_bottom, in_cart_prod_sum = page.sum_in_cart()
    # Сравнение суммы выбраных продуктов и сумм в корзине
    assert sum_cart_bottom == sum_cart_top and sum_cart_bottom == in_cart_prod_sum
    # Получение данных по продуктам из корзины по имени, бренду и сравнение с тестовым набором
    for seq_num in range(len(page.prod_names)):
        prod_content = page.param_prod(seq_num)
        for i in range(len(prod_content)):
            if us_set[i] != '':
                assert us_set[i] in prod_content[i]

    # Переход на страницу оформления заказа и заполнения всех данных
    page.save_screen_browser(f'us_1_cart_chekout_{us_set[0]}')
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.save_screen_browser(f'us_2_data_chekout_{us_set[0]}')
    page.goto_delivery()
    page.input_delivery_courier(SendOrderSets.courier[1][0], SendOrderSets.courier[1][1], SendOrderSets.courier[1][2],
                                SendOrderSets.courier[1][3])
    page.save_screen_browser(f'us_3_delivery_chekout_{us_set[0]}')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser(f'us_4_pay_chekout_{us_set[0]}')
    page.goto_benefit()
    page.save_screen_browser(f'us_5_confitm_chekout_{us_set[0]}')


@pytest.mark.integration
@pytest.mark.positive
def test_us_filter_sg_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить сонцезащитные очки бренда VOGUE, женские, длина заушника/ширина мостика/
    ширина окуляра 160/138/40" осуществляет поиск по брендам, полу, длинне заушника, ширине мостика и ширине окуляра,
    сортирует выбранные позиции возрастанию цены, выбирает рандомные из найденных очков и добавляет в корзину.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'sg')

    us_set = SunglassSets.filter_set_uc
    for i in range(len(us_set)):

        # Убираем всплывающий баннер
        if i == 0:
            page.pass_popup_banner()

        # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
        page.filter_click(i, us_set[i], 'sg')
        # Получаем результат применения фильтров и сравниваем с тестовым набором
        search_result_brand = page.search_result_single(i)
        if us_set[i] != '':
            assert us_set[i] in search_result_brand, f'ERROR! Filtering error'

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
    # Получение количества позиций в корзине после добавления очков
    amount_cart_after = page.amount_cart()
    assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"

    page.save_screen_browser(f'uc_add_cart_sg_{us_set[0]}')

    # Очищаем все фильтры
    page.clear_all_filter()

    # Инициализация экземпляра корзины
    page = CartPage(web_driver_desktop, 10)
    # Получение данных из корзины
    sum_cart_top, sum_cart_bottom, in_cart_prod_sum = page.sum_in_cart()
    # Сравнение суммы выбраных продуктов и сумм в корзине
    assert sum_cart_bottom == sum_cart_top and sum_cart_bottom == in_cart_prod_sum
    # Получение данных по продуктам из корзины по имени, бренду и сравнение с тестовым набором
    for seq_num in range(len(page.prod_names)):
        prod_content = page.param_prod(seq_num)
        for i in range(len(prod_content)):
            if us_set[i] != '':
                assert us_set[i] in prod_content[i]

    # Переход на страницу оформления заказа и заполнения всех данных
    page.save_screen_browser(f'us_1_cart_chekout_{us_set[0]}')
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.save_screen_browser(f'us_2_data_chekout_{us_set[0]}')
    page.goto_delivery()
    page.input_delivery_courier(SendOrderSets.courier[0][0], SendOrderSets.courier[0][1], SendOrderSets.courier[0][2],
                                SendOrderSets.courier[0][3])
    page.save_screen_browser(f'us_3_delivery_chekout_{us_set[0]}')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser(f'us_4_pay_chekout_{us_set[0]}')
    page.goto_benefit()
    page.save_screen_browser(f'us_5_confitm_chekout_{us_set[0]}')


@pytest.mark.integration
@pytest.mark.positive
def test_us_filter_care_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить..." проверяет фильтр по брендам, объему и типу, сортирует
    выбранные позиции возрастанию цены, выбирает рандомную позицию и добавляет в корзину.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = CarePage(web_driver_desktop, 7)

    us_set = CareSets.filter_set_uc
    for i in range(len(us_set)):

        # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
        page.filter_click(i, us_set[i])
        # Получаем результат применения фильтров и сравниваем с тестовым набором
        if us_set[i] != '' and i <= 1:
            search_result_brand = page.search_result_single(i)
            assert us_set[i] in search_result_brand, f'ERROR! Filtering error'

    # Сортировка по возрастанию
    page.sorted_by_on_page(2)
    list_price_increase = page.get_care_list_on_page()
    list_sort = sorted(list_price_increase)
    assert list_price_increase == list_sort, "ERROR! Position don't sorted"

    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()
    # Получение номера продукта на странице
    frame_num = page.rand_prod_card(page.card_prod_len() - 1)
    # Добавление в корзину 1-го продукта с параметрами заказа по умолчанию
    add_cart_sum = page.add_cart_care(frame_num, CareSets.set_vol)
    # Получение количества позиций в корзине после добавления оправы
    amount_cart_after = page.amount_cart()
    assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"

    page.save_screen_browser(f'uc_add_cart_care_{CareSets.filter_set_uc[0]}')

    # Инициализация экземпляра корзины
    page = CartPage(web_driver_desktop, 10)
    # Получение данных из корзины
    sum_cart_top, sum_cart_bottom, in_cart_prod_sum = page.sum_in_cart()
    # Сравнение суммы выбраных продуктов и сумм в корзине
    assert add_cart_sum == sum_cart_top and sum_cart_bottom == sum_cart_top and sum_cart_bottom == in_cart_prod_sum
    # Получение данных по продуктам из корзины по имени, бренду и сравнение с тестовым набором
    for seq_num in range(len(page.prod_names)):
        prod_name, prod_brand = page.param_care(seq_num)
        assert us_set[0].lower() in prod_brand.lower()

    # Переход на страницу оформления заказа и заполнения всех данных
    page.save_screen_browser(f'us_1_cart_chekout_{us_set[0]}')
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.save_screen_browser(f'us_2_data_chekout_{us_set[0]}')
    page.goto_delivery()
    page.input_delivery_np(SendOrderSets.nova_poshta[1][0], SendOrderSets.nova_poshta[1][1])
    page.save_screen_browser(f'us_3_delivery_chekout_{us_set[0]}')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser(f'us_4_pay_chekout_{us_set[0]}')
    page.goto_benefit()
    page.save_screen_browser(f'us_5_confitm_chekout_{us_set[0]}')
