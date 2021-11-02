# -*- encoding=utf8 -*-

import time, pytest
from pages.start_page import StartPage
from pages.locators import StartLocators


# Тестирование десктопной версии сайта
def test_start_page(web_driver_desktop):
    """Тест проверяет кликабельность лого сайта и перезагрузку его стартовой страницы"""

    page_start = StartPage(web_driver_desktop)
    page_start.start_img_click()
    assert page_start.get_relative_link() == '/' or \
           page_start.get_relative_link() == '/uk/', 'Transition error'


@pytest.mark.parametrize("test_search_p", ['линзы', 'lens', 123], ids=['search ru', 'search en', 'search digit'])
def test_search_start_page_desktop_positive(web_driver_desktop, test_search_p):
    """Тест проверяет работу поиска с различными позитивными данными"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.search_field_click(test_search_p)
    amount = int(web_driver_desktop.find_element(*StartLocators.search_result).text)
    assert amount > 0, 'Field "Search" working unsucсess'


@pytest.mark.parametrize("test_search",
                        ['123456', StartPage.generate_string(255), StartPage.generate_string(1001)
                        , StartPage.russian_chars(), StartPage.russian_chars().upper(), StartPage.chinese_chars()
                        , StartPage.special_chars()]
                        , ids=['any', '255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'chinese', 'specials'])
def test_search_start_page_desktop_negative(web_driver_desktop, test_search):
    """Тест проверяет поле поиска с различными негативными данными и корректность обработки запроса"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.search_field_click(test_search)
    amount = int(web_driver_desktop.find_element(*StartLocators.search_result).text)
    assert amount == 0, 'Field "Search" working unsucсess'


def test_callback_btn_start_page_desktop(web_driver_desktop):
    """Тест проверяет кликабельность "Перезвоните мне" и загрузку формы обратного звонка, после чего закрывает ее"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.callback_btn_click()
    time.sleep(2)
    assert web_driver_desktop.find_element(*StartLocators.callback_form_submit).is_enabled()\
        , 'Transition error'
    web_driver_desktop.find_element(*StartLocators.callback_form_close).click()
    time.sleep(2)


def test_login_btn_start_page_desktop(web_driver_desktop):
    """Тест проверяет кликабельность "Вход" """

    page_start = StartPage(web_driver_desktop, 5)
    page_start.login_btn_click()
    assert web_driver_desktop.find_element(*StartLocators.login_submit).is_enabled()\
        , 'Transition error'
    web_driver_desktop.find_element(*StartLocators.login_close).click()


def test_wishlist_btn_start_page_desktop(web_driver_desktop):
    """Тест проверяет кликабельность "Список желаний" без авторизации"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.wishlist_btn_click()
    assert web_driver_desktop.find_element(*StartLocators.login_submit).is_enabled()\
        , 'Transition error'
    web_driver_desktop.find_element(*StartLocators.login_close).click()


def test_cart_start_page_desktop(web_driver_desktop):
    """Тест проверяет кликабельность "Корзина" без авторизации"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.cart_btn_click()
    assert page_start.get_relative_link() == '/ru/cart/' \
           or page_start.get_relative_link() == '/uk/cart/', 'Transition error'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()


def test_lang_start_page_desktop(web_driver_desktop):
    """Тест проверяет переключение языков сайта Рус и Укр"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.lang_btn_click()
    page_start.lang_uk_btn_click()
    assert page_start.get_relative_link() == '/uk/', 'Transition error'
    web_driver_desktop.find_element(*StartLocators.lang_btn_active).click()
    web_driver_desktop.find_element(*StartLocators.lang_btn_ru).click()
    assert page_start.get_relative_link() == '/', 'Transition error'


def test_menu_start_page_desktop(web_driver_desktop):
    """Тест проверяет кликабельность меню и переход на соответствующие страницы меню, закрытие меню"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.menu_btn_click()
    time.sleep(2)
    page_start.menu_close_btn_click()
    time.sleep(2)
    assert page_start.get_relative_link() == '/' or \
           page_start.get_relative_link() == '/uk/', 'Transition error'

    web_driver_desktop.find_element(*StartLocators.menu_button).click()
    time.sleep(2)
    web_driver_desktop.find_elements(*StartLocators.menu_button_menu)[0].click()
    time.sleep(2)
    assert page_start.get_relative_link() == '/ru/articles/blog/' or \
           page_start.get_relative_link() == '/uk/articles/blog/', 'Transition error'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    time.sleep(2)


    web_driver_desktop.find_element(*StartLocators.menu_button).click()
    time.sleep(2)
    web_driver_desktop.find_elements(*StartLocators.menu_button_menu)[1].click()
    time.sleep(2)
    assert page_start.get_relative_link() == '/ru/page/about/' or \
           page_start.get_relative_link() == '/uk/page/about/', 'Transition error'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    time.sleep(2)


    web_driver_desktop.find_element(*StartLocators.menu_button).click()
    time.sleep(2)
    web_driver_desktop.find_elements(*StartLocators.menu_button_menu)[2].click()
    time.sleep(2)
    assert page_start.get_relative_link() == '/ru/sluzhba-podderzhki/' or \
           page_start.get_relative_link() == '/uk/sluzhba-pidtrimki/', 'Transition error'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    time.sleep(2)



