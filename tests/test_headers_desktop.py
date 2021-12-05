# -*- encoding=utf8 -*-

import pytest
from pages.headers import Headers
from pages.locators import StartLocators, RegLocators
from pages.url_list import LinsaUa
from pages.aux_metods import AuxMetods


@pytest.mark.smokie
@pytest.mark.positive
def test_start_page(web_driver_desktop):
    """Тест проверяет кликабельность лого сайта и перезагрузку его стартовой страницы"""

    page = Headers(web_driver_desktop)
    page.start_img_click()
    assert page.get_relative_link() == '/' or \
           page.get_relative_link() == '/uk/', 'Transition error'


@pytest.mark.smokie
@pytest.mark.positive
@pytest.mark.parametrize("test_search", ['линзы', 'lens', 'ClearLux', 'линзы O2O2 Toric', 123]
    , ids=['lens_ru', 'lens_en', 'ClearLux', 'O2O2_Toric', 'digit'])
def test_search_start_page(web_driver_desktop, test_search):
    """Тест проверяет работу поиска с различными позитивными данными, делает скриншот"""

    page = Headers(web_driver_desktop, 5)
    page.search_field_click(test_search)
    page.save_screen_browser(f'test_serch_{test_search}')
    amount = int(web_driver_desktop.find_element(*StartLocators.search_result).text)
    assert amount > 0, 'Field "Search" working unsucсess'


@pytest.mark.negative
@pytest.mark.parametrize("test_search",
                         ['123456', AuxMetods.generate_string(255), AuxMetods.generate_string(1001)
                             , AuxMetods.russian_chars(), AuxMetods.russian_chars().upper(), AuxMetods.chinese_chars()
                             , AuxMetods.special_chars()]
    , ids=['any', '255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'chinese', 'specials'])
def test_search_start_page(web_driver_desktop, test_search):
    """Тест проверяет поле поиска с различными негативными данными и корректность обработки запроса"""

    page = Headers(web_driver_desktop, 5)
    page.search_field_click(test_search)
    amount = int(web_driver_desktop.find_element(*StartLocators.search_result).text)
    assert amount == 0, 'Field "Search" working unsucсess'


@pytest.mark.positive
def test_callback_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Перезвоните мне" и загрузку формы обратного звонка, после чего закрывает ее"""

    page = Headers(web_driver_desktop, 5)
    page.callback_btn_click()
    assert page.search_callback_submit().is_enabled(), 'Transition error'
    page.callback_close()


@pytest.mark.smokie
@pytest.mark.positive
def test_login_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Вход" """

    page = Headers(web_driver_desktop, 5)
    page.login_btn_click()
    assert web_driver_desktop.find_element(*RegLocators.login_submit).is_enabled(), 'Transition error'
    web_driver_desktop.find_element(*RegLocators.login_close).click()


@pytest.mark.positive
def test_wishlist_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Список желаний" без авторизации"""

    page = Headers(web_driver_desktop, 5)
    page.wishlist_btn_click()
    assert page.search_login_submit().is_enabled(), 'Transition error'
    page.login_close()


@pytest.mark.smokie
@pytest.mark.positive
def test_cart_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Корзина" без авторизации"""

    page = Headers(web_driver_desktop, 5)
    page.cart_btn_click()
    assert page.get_relative_link() == '/ru/cart/' \
           or page.get_relative_link() == '/uk/cart/', 'Transition error'
    page.get_url(page.url)


@pytest.mark.smokie
@pytest.mark.positive
def test_lang_start_page(web_driver_desktop):
    """Тест проверяет переключение языков сайта Рус и Укр"""

    page = Headers(web_driver_desktop, 5)
    page.lang_btn_click()
    page.lang_uk_btn_click()
    assert page.get_relative_link() == '/uk/', 'Transition error'
    page.lang_btn_click()
    page.lang_ru_btn_click()
    assert page.get_relative_link() == '/', 'Transition error'


@pytest.mark.smokie
@pytest.mark.positive
def test_menu_start_page(web_driver_desktop):
    """Тест проверяет кликабельность бокового меню и переход на соответствующие страницы меню, закрытие меню"""

    page = Headers(web_driver_desktop, 5)
    page.menu_click()
    page.menu_close_click()
    assert page.get_relative_link() == '/' or \
           page.get_relative_link() == '/uk/', 'Transition error'

    # Перебор в цикле пунктов меню
    menu_points = page.menu_points()
    for index in range(menu_points):
        page.goto_menu_point(index)
        assert page.get_relative_link() == LinsaUa.right_menu_urls[index][0] or \
               page.get_relative_link() == LinsaUa.right_menu_urls[index][1], 'Transition error'
        page.get_url(page.url)
