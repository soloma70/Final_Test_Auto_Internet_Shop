# -*- encoding=utf8 -*-

import pytest
from pages.start_page_mobile import StartPage
from pages.locators import StartLocatorsMobile
from pages.test_sets import RegSets, AuthSets
from pages.url_list import LinsaUa
from pages.aux_metods import AuxMetods


@pytest.mark.smoke
@pytest.mark.positive
def test_start_page(web_driver_mobile):
    """Тест проверяет кликабельность лого сайта и перезагрузку его стартовой страницы"""

    page_start = StartPage(web_driver_mobile)
    page_start.start_img_click()
    assert page_start.get_relative_link() in ('/', '/uk/'), 'Transition error'


@pytest.mark.positive
@pytest.mark.parametrize("test_search", ['линзы', 'lens', 123], ids=['search ru', 'search en', 'search digit'])
def test_search_positive_start_page(web_driver_mobile, test_search):
    """Тест проверяет работу поиска с различными позитивными данными"""

    page = StartPage(web_driver_mobile, 5)
    page.search_field_click_search(test_search)
    amount = page.amount_found_result()
    assert amount > 0, 'Field "Search" working unsucсess'


@pytest.mark.negative
@pytest.mark.parametrize("test_search",
                         ['123456', AuxMetods.generate_string(255), AuxMetods.generate_string(1001)
                             , AuxMetods.russian_chars(), AuxMetods.russian_chars().upper(), AuxMetods.chinese_chars()
                             , AuxMetods.special_chars()]
    , ids=['any', '255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'chinese', 'specials'])
def test_search_negative_start_page(web_driver_mobile, test_search):
    """Тест проверяет поле поиска с различными негативными данными и корректность обработки запроса"""

    page = StartPage(web_driver_mobile, 5)
    page.search_field_click_search(test_search)
    amount = page.amount_found_result()
    assert amount == 0, 'Field "Search" working unsucсess'


@pytest.mark.positive
def test_wishlist_btn_start_page(web_driver_mobile):
    """Тест проверяет кликабельность "Список желаний" без авторизации"""

    page = StartPage(web_driver_mobile, 5)
    page.wishlist_btn_click()
    title = page.wait_login_title()
    assert title.is_displayed() and title.text == 'Вход', 'Transition error'
    page.login_close()


@pytest.mark.smoke
@pytest.mark.positive
def test_cart_start_page(web_driver_mobile):
    """Тест проверяет кликабельность "Корзина" без авторизации"""

    page = StartPage(web_driver_mobile, 5)
    page.cart_btn_click()
    assert page.get_relative_link() in ('/ru/cart/', '/uk/cart/'), 'Transition error'
    page.get_url(page.url)


@pytest.mark.positive
def test_menu_start_page(web_driver_mobile):
    """Тест проверяет кликабельность меню и переход на соответствующие страницы меню, закрытие меню"""

    page = StartPage(web_driver_mobile, 5)
    page.menu_btn_click()
    page.menu_close_click()
    assert page.get_relative_link() == '/' or page.get_relative_link() == '/uk/', 'Transition error'

    # Проверка переключения языков
    page.menu_btn_click()
    page.lang_btn_active_click()
    page.lang_btn_click()
    assert page.get_relative_link() == '/uk/', 'Transition error'

    page.menu_btn_click()
    page.lang_btn_active_click()
    page.lang_btn_click()
    assert page.get_relative_link() == '/', 'Transition error'

    # Перебор в цикле пунктов меню
    menu_points = page.menu_points
    menu_points_hidden = page.menu_points_hidden

    for index in range(len(menu_points) - len(menu_points_hidden)):
        page.menu_btn_click()
        page.menu_points_main_click(index)
        assert page.get_relative_link() in (
            LinsaUa.main_menu_urls[index][0], LinsaUa.main_menu_urls[index][1]), 'Transition error'
        page.get_url(page.url)

    for index in range(len(menu_points_hidden)):
        page.menu_btn_click()
        page.menu_points_hidden_click(index)
        assert page.get_relative_link() in (
            LinsaUa.left_menu_urls[index][0], LinsaUa.left_menu_urls[index][1]), 'Transition error'
        page.get_url(page.url)


def test_authorization_valid_data_start_page(web_driver_mobile):
    """Тест проверяет авторизацию с валидными данными, переход в кабинет, переход на соответствующие
    страницы кабинета, выход из кабинета возможен только POST запросом к API.
    Найден баг: кнопка на выход из кабинета невидима, элемент в DOM присутствует, но не рабочий"""

    page = StartPage(web_driver_mobile, 5)
    page.menu_btn_click()
    page.menu_autor_click()
    page.wait_login_title()
    page.input_autor_data(AuthSets.auth_phone, AuthSets.auth_passw)
    page.menu_autor_submit()
    user_name = page.wait_download_cabinet()
    assert page.get_relative_link() in (LinsaUa.cabinet[0][0], LinsaUa.cabinet[1][0]), 'Transition error'
    assert user_name == AuthSets.auth_name

    amount_tab = page.amount_tab_cabinet_menu()
    for index in range(1, amount_tab):
        url_menu = page.goto_cabinet_menu(index)
        assert url_menu in (LinsaUa.cabinet[index][0], LinsaUa.cabinet[index][0]), 'Transition error'


@pytest.mark.positive
def test_banners_start_page(web_driver_mobile):
    """Тест проверяет кликабельность баннеров и переход на соответствующие страницы, а так же не нулевое
    количество продуктов"""

    page = StartPage(web_driver_mobile, 5)

    # Перебор в цикле баннеры
    for index in range(3):
        page.banner_points_click(index)
        amount_products = page.amount_products()
        assert page.get_relative_link() in (
            LinsaUa.banners_urls[index][0], LinsaUa.banners_urls[index][1]), 'Transition error'
        assert amount_products > 0, 'Amount = 0, are not positions'
        page.get_url(page.url)


@pytest.mark.smoke
@pytest.mark.positive
def test_action_banners_start_page(web_driver_mobile):
    """Тест проверяет кликабельность акционного баннера и переход на соответствующую страницу,
    добавление 1-й акционной позиции в корзину"""

    page = StartPage(web_driver_mobile, 5)
    page.all_sales_prods_click()
    assert page.get_relative_link() in (LinsaUa.main_menu_urls[0][0], LinsaUa.main_menu_urls[1][0]), 'Transition error'
    page.get_url(page.url)

    # Добавление в корзину 1-го акционного продукта
    amount_cart_before = page.amount_cart_mobile()
    page.sales_banner_first_position()
    page.add_cart_product_def_par()
    page.close_cart_popup()
    page.get_url(page.url)
    amount_cart_after = page.amount_cart_mobile()
    assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"


@pytest.mark.positive
def test_love_brands_start_page(web_driver_mobile):
    """Тест проверяет кликабельность баннеров "Любимые бренды" и отображение соответствующих им элементов в ленте"""

    page = StartPage(web_driver_mobile)
    page.move_to_element_love_blands()
    page.goto_love_brands_lenses()
    page.save_screen_browser('love_barnds_lenses_mob')
    page.goto_love_brands_accessories()
    page.save_screen_browser('love_barnds_acces_mob')
    page.goto_love_brands_sunglasses()
    page.save_screen_browser('love_barnds_sg_mob')


@pytest.mark.smoke
@pytest.mark.positive
def test_registration_start_page(web_driver_mobile):
    """Тест проверяет кликабельность и заполнение полей формы регистрации на стартовой странице """

    page = StartPage(web_driver_mobile)
    page.registration_btn()
    assert page.registration_popup_win().is_displayed(), 'ERROR! PopUp Registration is not displayed'
    page.input_reg_data_mobile(RegSets.reg_name, RegSets.reg_phone, RegSets.reg_passw)
    page.save_screen_browser('registration_popup_mob')
    page.registration_close()
    web_driver_mobile.execute_script("window.scrollTo(0, 0)")


@pytest.mark.positive
def test_blogs_start_page(web_driver_mobile):
    """Тест проверяет кликабельность блоков в разделе "Оптический блог"
    и корректность перехода по ссылкам """

    page = StartPage(web_driver_mobile)

    list_blog_titles = page.blog_card_titles()

    # Click for card 1
    page.goto_blog(1)
    blog_title_1 = page.blog_title()
    page.get_url(page.url)

    # Click for card 2
    page.goto_blog(2)
    blog_title_2 = page.blog_title()
    page.get_url(page.url)

    # Click for card 3
    page.goto_blog(3)
    blog_title_3 = page.blog_title()
    page.get_url(page.url)

    list_title = [blog_title_1, blog_title_2, blog_title_3]

    # Click for btn 'Больше новостей'
    web_driver_mobile.find_element(*StartLocatorsMobile.blog_btn).click()
    blog_url = page.get_relative_link()
    page.get_url(page.url)

    assert list_blog_titles == list_title, f'ERROR! Bad transaction: {list_blog_titles} != {list_title}'
    assert blog_url in (
        LinsaUa.main_menu_urls[5][0], LinsaUa.main_menu_urls[5][1]), f'ERROR! Bad transaction for {blog_url}'


@pytest.mark.positive
def test_footer_start_page(web_driver_mobile):
    """Тест проверяет кликабельность блоков в footers
    и корректность перехода по ссылкам """

    page = StartPage(web_driver_mobile, 10)
    pages_footers = []
    footers_left = page.footers_left_btns
    footers_right = page.footers_right_btns

    for index in range(len(footers_left)):
        page.goto_footer_left(index)
        pages_footers.append(page.get_relative_link())
        page.get_url(page.url)

    for index in range(len(footers_right)):
        page.goto_footer_right(index)
        pages_footers.append(page.get_relative_link())
        page.get_url(page.url)

    page.goto_footer_bottom_left()
    pages_footers.append(page.get_relative_link())
    page.get_url(page.url)

    page.goto_footer_bottom_right()
    pages_footers.append(page.get_relative_link())
    page.get_url(page.url)

    for index in range(2):
        page.goto_footer_middle(index)
        windows = web_driver_mobile.window_handles
        web_driver_mobile.switch_to.window(windows[1])
        pages_footers.append(web_driver_mobile.current_url)
        web_driver_mobile.close()
        web_driver_mobile.switch_to.window(windows[0])
        page.get_url(page.url)

    # Переход на страницу инстаграм не проверяется, требует логин инстаграм
    for index in range(11):
        assert pages_footers[index] in (LinsaUa.footers_menu_urls[index][0], LinsaUa.footers_menu_urls[index][
            1]), f'ERROR! Bad transaction for {pages_footers[index]}'
