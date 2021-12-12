# -*- encoding=utf8 -*-

import pytest
from pages.cabinet import CabinetPage
from pages.care_page import CarePage
from pages.product_page import ProductPage
from pages.lens_page import LensPage
from pages.cart_page import CartPage
from pages.test_sets import LensSets, SendOrderSets, FramesSets, SunglassSets, CareSets, AuthSets


@pytest.mark.integration
@pytest.mark.positive
def test_us_filter_buy_lens_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить линзы бренда INTEROJO, линейки Fusion, левая -4.00, правая -2.75"
    осуществляет поиск по брендам, линейкам, типу линзы, режиму замены, базовой кривизне, диаметру и диоптрийности,
    сортирует выбранные позиции возрастанию цены, выбирает линзы и добавляет в корзину, применяя указанные параметры,
    и оформляет заказ.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = LensPage(web_driver_desktop, 5)

    us_sets_mas = LensSets.filter_set_uc
    for i, us_sets in enumerate(us_sets_mas):

        for _, us_set in enumerate(us_sets):
            # Добавляем фильтр по бренду согласно тестовому набору и получаем список фильтров
            page.filter_click_lens(i, us_set)
            # Получаем результат применения 2-х фильтров (по бренду и линейке) и сравниваем с тестовым набором
            if 0 <= i <= 1:
                search_result = ', '.join(page.search_result_single(i)).lower()
                assert us_set.lower() in search_result, f'ERROR! Filtering error'

    # Сортировка по возрастанию
    page.sorted_by_on_page(2)
    list_price_increase = page.get_lens_list_on_page(page.amount_on_page())
    list_sort = sorted(list_price_increase)
    assert list_price_increase == list_sort, "ERROR! Position don't sorted"

    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()
    # Добавление в корзину 1-го найденого продукта с параметрами в us_set, переход в корзину, получение суммы заказа
    page.add_cart_lens(0)
    add_cart_sum = page.add_param_lens(us_sets_mas)
    status_add_prod = page.add_success()
    assert status_add_prod == 'Товар добавлен в корзину', "ERROR! Wishlist don't add"

    # Получение количества позиций в корзине после добавления оправы
    amount_cart_after = page.amount_cart()
    assert amount_cart_before + 2 == amount_cart_after, "ERROR! Product don't add to cart"

    # Инициализация экземпляра корзины
    page = CartPage(web_driver_desktop, 10)
    # Получение данных из корзины
    sum_cart_top, sum_cart_bottom, in_cart_prod_sum = page.sum_in_cart()
    # Сравнение суммы выбраных линз и сумм в корзине
    assert add_cart_sum == sum_cart_top and sum_cart_bottom == sum_cart_top and sum_cart_bottom == in_cart_prod_sum
    # Получение данных по линзам из корзины по имени, бренду, sph, bc и сравнение с тестовым набором
    for seq_num in range(len(page.prod_names)):
        prod_name, prod_brand, lens_sph, lens_bc = page.param_lens(seq_num)
        assert us_sets_mas[1][0].lower() in prod_name.lower()
        assert us_sets_mas[0][0].lower() in prod_brand.lower()
        assert us_sets_mas[6][seq_num] in lens_sph
        assert us_sets_mas[4][0] in lens_bc

    # Переход на страницу оформления заказа и заполнения всех данных
    page.save_screen_browser(f'us_1_cart_chekout_{us_sets_mas[0][0]}')
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.save_screen_browser(f'us_2_data_chekout_{us_sets_mas[0][0]}')
    page.goto_delivery()
    page.input_delivery_np(SendOrderSets.nova_poshta[0][0], SendOrderSets.nova_poshta[0][1])
    page.save_screen_browser(f'us_3_delivery_chekout_{us_sets_mas[0][0]}')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser(f'us_4_pay_chekout_{us_sets_mas[0][0]}')
    page.goto_benefit()
    page.save_screen_browser(f'us_5_confitm_chekout_{us_sets_mas[0][0]}')

    # Переход в корзину и ее очистка
    page.goto_header_cart()
    page.clear_all_cart()


@pytest.mark.integration
@pytest.mark.positive
def test_us_filter_buy_fr_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить оправу бренда CARRERA, мужскую, длина заушника/ширина мостика/ширина окуляра
    145/20/50" осуществляет поиск по брендам, полу, длинне заушника, ширине мостика и ширине окуляра,
    сортирует выбранные позиции возрастанию цены, выбирает рандомную из найденных оправ и добавляет в корзину и
    оформляет заказ.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'fr')

    us_sets = FramesSets.filter_set_uc
    for i, us_set in enumerate(us_sets):

        # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
        page.filter_click(i, us_set, 'fr')
        # Получаем результат применения фильтров и сравниваем с тестовым набором
        search_result_brand = page.search_result_single(i)
        if us_set[i] != '':
            assert us_set in search_result_brand, 'ERROR! Filtering error'

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

    page.save_screen_browser(f'uc_add_cart_fr_{us_sets[0]}')

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
            if us_sets[i] != '':
                assert us_sets[i] in prod_content[i]

    # Переход на страницу оформления заказа и заполнения всех данных
    page.save_screen_browser(f'us_1_cart_chekout_{us_sets[0]}')
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.save_screen_browser(f'us_2_data_chekout_{us_sets[0]}')
    page.goto_delivery()
    page.input_delivery_courier(SendOrderSets.courier[1][0], SendOrderSets.courier[1][1], SendOrderSets.courier[1][2],
                                SendOrderSets.courier[1][3])
    page.save_screen_browser(f'us_3_delivery_chekout_{us_set[0]}')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser(f'us_4_pay_chekout_{us_sets[0]}')
    page.goto_benefit()
    page.save_screen_browser(f'us_5_confitm_chekout_{us_sets[0]}')

    # Переход в корзину и ее очистка
    page.goto_header_cart()
    page.clear_all_cart()


@pytest.mark.integration
@pytest.mark.positive
def test_us_filter_buy_sg_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить сонцезащитные очки бренда VOGUE, женские, длина заушника/ширина мостика/
    ширина окуляра 160/138/40" осуществляет поиск по брендам, полу, длинне заушника, ширине мостика и ширине окуляра,
    сортирует выбранные позиции возрастанию цены, выбирает рандомные из найденных очков и добавляет в корзину и
    оформляет заказ.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = ProductPage(web_driver_desktop, 'sg')

    us_sets = SunglassSets.filter_set_uc
    for i, us_set in enumerate(us_sets):

        # Убираем всплывающий баннер
        if i == 0:
            page.pass_popup_banner()

        # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
        page.filter_click(i, us_set, 'sg')
        # Получаем результат применения фильтров и сравниваем с тестовым набором
        search_result_brand = page.search_result_single(i)
        if us_set != '':
            assert us_set in search_result_brand, 'ERROR! Filtering error'

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

    page.save_screen_browser(f'uc_add_cart_sg_{us_sets[0]}')

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
            if us_sets[i] != '':
                assert us_sets[i] in prod_content[i]

    # Переход на страницу оформления заказа и заполнения всех данных
    page.save_screen_browser(f'us_1_cart_chekout_{us_sets[0]}')
    page.checkout_click()
    page.input_data(SendOrderSets.name, SendOrderSets.email, SendOrderSets.phone)
    page.save_screen_browser(f'us_2_data_chekout_{us_sets[0]}')
    page.goto_delivery()
    page.input_delivery_courier(SendOrderSets.courier[0][0], SendOrderSets.courier[0][1], SendOrderSets.courier[0][2],
                                SendOrderSets.courier[0][3])
    page.save_screen_browser(f'us_3_delivery_chekout_{us_sets[0]}')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser(f'us_4_pay_chekout_{us_sets[0]}')
    page.goto_benefit()
    page.save_screen_browser(f'us_5_confitm_chekout_{us_sets[0]}')

    # Переход в корзину и ее очистка
    page.goto_header_cart()
    page.clear_all_cart()


@pytest.mark.integration
@pytest.mark.positive
def test_us_filter_buy_care_page(web_driver_desktop):
    """Тест UC "Я хочу найти и купить..." проверяет фильтр по брендам, объему и типу, сортирует
    выбранные позиции возрастанию цены, выбирает рандомную позицию и добавляет в корзину и оформляет заказ.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!"""

    page = CarePage(web_driver_desktop, 7)

    us_set = CareSets.filter_set_uc
    for i in range(len(us_set) - 1):
        # Добавляем фильтр по бренду согласно тестовым наборам и получаем списки фильтров
        page.filter_click(i, us_set[i])
        # Получаем результат применения фильтров и сравниваем с тестовым набором
        if us_set[i] != '' and i <= 1:
            search_result_brand = page.search_result_single(i)
            assert us_set[i] in search_result_brand, 'ERROR! Filtering error'

    # Сортировка по возрастанию
    page.sorted_by_on_page(2)
    list_price_increase = page.get_care_list_on_page()
    list_sort = sorted(list_price_increase)
    assert list_price_increase == list_sort, "ERROR! Position don't sorted"

    # Получение количества позиций в корзине перед добавлением
    amount_cart_before = page.amount_cart()
    # Добавление в корзину 1-го продукта с параметрами заказа по умолчанию
    page.add_cart_care(0)
    add_cart_sum = page.add_param_care(CareSets.set_vol)
    status_add_prod = page.add_success()
    assert status_add_prod == 'Товар добавлен в корзину', "ERROR! Wishlist don't add"

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

    # Переход в корзину и ее очистка
    page.goto_header_cart()
    page.clear_all_cart()


@pytest.mark.integration
@pytest.mark.positive
def test_us_cabinet_search_wishlist_cart_buy(web_driver_auth_desktop):
    """Тест UC "Я хочу найти и купить..." авторизуется в кабинете, находит линзы и раствор для линз через поиск и
    добавляет их в корзину с тестовыми параметрами, находит с помощью фильтров оправу и очки, добавляет их в
    список желаний, переносит из списка желаний в корзину и оформляет заказ.
    ВНИМАНИЕ!!! Необходимо убрать курсор мышки из поля страницы браузера!
    БАГ!!! Через поиск можно найти частично линзы и уходовые средства, ни оправы, ни очки не ищет
    БАГ!!! Из списка желаний с помощью кнопки "Купить" невозможно добавить в корзину линзы и уходовые ср-ва,
    только через ссылку.
    БАГ!!! D корзину добавляются суммы в целых грн., а в корзине по этим же позициям суммы в грн. и коп.,
    соответственно, итог тоже с коп."""

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() in AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Переход на страницу Личные данные и добавление емейл и дня рождения
    page.goto_cabinet_menu(1)
    page.add_email(AuthSets.auth_email)
    page.add_birthday(AuthSets.birthday)
    page.save_personal_data()
    page.save_screen_browser('us_buy_change_personal_data')
    # Проверка соответствия введеных данных тестовому набору
    list_data = page.list_personal_data()
    assert list_data[3] == AuthSets.auth_email, 'ERROR! Bad last add email'
    assert list_data[4] == AuthSets.birthday, 'ERROR! Bad last add email'

    # Переход на страницу Адреса доставки и добавление адреса из тестового набора
    page.goto_cabinet_menu(4)
    page.add_new_adress(AuthSets.adress[0][0], AuthSets.adress[0][1], AuthSets.adress[0][2], AuthSets.adress[0][3])
    page.inst_default_address()
    page.save_screen_browser('us_buy_add_adress')
    # Проверка соответствия последнего введеного адреса тестовому набору
    last_add_adress = page.list_last_add_adress()
    assert last_add_adress == AuthSets.adress[0], 'ERROR! Bad last add adress'

    # Переход на страницу Список желаний и добавление нового списка
    page.goto_cabinet_menu(2)
    status_add = page.add_new_wishlist(AuthSets.test_wish_list)
    page.save_screen_browser('us_buy_add_wishlist')
    assert status_add == 'Успешно', "ERROR! Wishlist don't add"

    # Добавление в wishlist оправы из тестового списка по первым 3 фильтрам
    page = ProductPage(web_driver_auth_desktop, 'fr')
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
    # Добавление первой найденной оправы в wishlist
    status_add_prod = page.add_prod_wishlist(AuthSets.test_wish_list)
    assert status_add_prod == 'Успешно', "ERROR! Wishlist don't add"

    # Добавление в wishlist солнечных очков из тестового списка по первым 3 фильтрам
    page = ProductPage(web_driver_auth_desktop, 'sg')
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
    # Добавление первых найденных очков в wishlist
    status_add_prod = page.add_prod_wishlist(AuthSets.test_wish_list)
    assert status_add_prod == 'Успешно', "ERROR! Wishlist don't add"

    # Добавление в корзину линз из тестового списка через поиск
    page = LensPage(web_driver_auth_desktop)
    page.search_field_click(f'линзы {LensSets.filter_set_uc[1][0]}')
    # Добавление первых найденных линз в корзину
    page.add_cart_lens(0)
    add_cart_sum_lens = page.add_param_lens(LensSets.filter_set_uc)
    status_add_prod = page.add_success()
    assert status_add_prod == 'Товар добавлен в корзину', "ERROR! Wishlist don't add"

    # Добавление в wishlist и корзину многофункционального р-ра из тестового списка  через поиск
    page = CarePage(web_driver_auth_desktop)
    page.search_field_click(f'{CareSets.filter_set_uc[3]}')
    # Добавление в корзину 1-го продукта с параметрами заказа по умолчанию
    page.add_cart_care(0)
    add_cart_sum_care = page.add_param_care(CareSets.set_vol)
    status_add_prod = page.add_success()
    assert status_add_prod == 'Товар добавлен в корзину', "ERROR! Wishlist don't add"

    # Переход в wishlist через кнопку в хедере, переход в тестовый список
    page = CabinetPage(web_driver_auth_desktop)
    page.goto_wishlist_header()
    page.goto_wishlist(AuthSets.test_wish_list)
    page.save_screen_browser('us_buy_product_wishlist')

    # Добавление продуктов из wishlist в корзину
    add_cart_sum_frames, status_add_frames = page.wishlist_buy_frames(0)
    assert status_add_frames == 'Товар добавлен в корзину', "ERROR! Wishlist don't add"
    add_cart_sum_sunglass, status_add_sunglass = page.wishlist_buy_sunglass(0)
    assert status_add_sunglass == 'Товар добавлен в корзину', "ERROR! Wishlist don't add"
    page.goto_header_cart()

    # Инициализация экземпляра корзины
    page = CartPage(web_driver_auth_desktop, 10)
    # Получение данных из корзины
    page.save_screen_browser('us_buy_cart_1_auth_user')
    page.win_scroll(900)
    page.save_screen_browser('us_buy_cart_2_auth_user')
    sum_cart_top, sum_cart_bottom, in_cart_prod_sum = page.sum_in_cart()
    # Сравнение суммы выбраных продуктов и сумм в корзине
    add_cart_sum = add_cart_sum_lens + add_cart_sum_care + add_cart_sum_frames + add_cart_sum_sunglass
    assert in_cart_prod_sum in (sum_cart_top, sum_cart_bottom), 'ERROR! Еhe amounts in the basket are not equal'
    assert int(add_cart_sum) == int(in_cart_prod_sum), 'ERROR! Amount add products != amount in cart'

    # Переход на страницу оформления заказа и заполнения всех данных
    page.save_screen_browser('us_buy_chekout_1_auth_user')
    page.checkout_click()
    page.save_screen_browser('us_buy_chekout_2_auth_user')
    page.goto_delivery()
    page.delivery_courier()
    page.save_screen_browser('us_buy_chekout_3_auth_user')
    page.goto_pay()
    page.input_pay_after_receiving()
    page.save_screen_browser('us_buy_chekout_4_auth_user')
    page.goto_benefit()
    page.save_screen_browser('us_buy_chekout_5_auth_user')

    # Переход и очистка корзины
    page.goto_header_cart()
    page.clear_all_cart()

    # Удаление тестового списка wishlist
    page = CabinetPage(web_driver_auth_desktop)
    page.goto_cabinet_menu(2)
    status_del = page.delete_wishlist(AuthSets.test_wish_list)
    assert status_del == 'Успешно', "ERROR! Wishlist don't add"

    # Удаление адреса и дня рождения
    page.goto_cabinet_menu(1)
    page.clear_email_birthday_lang()

    # Удаление последнего добавленного адреса
    page.goto_cabinet_menu(4)
    page.delete_adress(-1)
