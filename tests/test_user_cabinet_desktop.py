# -*- encoding=utf8 -*-
from urllib.parse import urlparse

import pytest
from pages.cabinet import CabinetPage
from pages.headers import Headers
from pages.test_sets import AuthSets
from pages.url_list import LinsaUa
from pages.aux_metods import AuxMetods
from time import sleep


# def test_registration_header_start_page(web_driver_desktop):
#     """Тест проверяет кликабельность "Вход" """
#
#     page = Headers(web_driver_desktop, 5)
#     page.login_btn_click()
#     assert web_driver_desktop.find_element(*RegLocators.login_submit).is_enabled(), 'Transition error'
#     web_driver_desktop.find_element(*RegLocators.login_close).click()


def test_authorization_valid_positive(web_driver_auth_desktop):
    """Тест проверяет авторизацию пользователя с валидными параметрами и переходит в кабинет"""

    page = Headers(web_driver_auth_desktop, 10)
    # Открытие всплывающего окна авторизации
    page.login_btn_click()
    print()
    # Ввод данных авторизации, скриншот и переход в кабинет
    page.input_auth_data(AuthSets.auth_phone, AuthSets.auth_passw)
    page.save_screen_browser(f'auth_cabinet')
    assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][1], 'ERROR! Bad transactoin!'

    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() == AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'
    sleep(1)
    for i in range(1, len(page.cabinet)):
        page.goto_menu(i)
        sleep(2)

    page.exit_cabinet()

def test_add_new_address_positive(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, добавляет новый адрес доставки, делает скриншот и
    удаляет адрес, делает скришщот, выходит из кабинета"""

    page = Headers(web_driver_auth_desktop, 10)

    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, скриншот и переход в кабинет и проверка URL кабинета
    page.input_auth_data(AuthSets.auth_phone, AuthSets.auth_passw)
    page.save_screen_browser(f'auth_cabinet')
    assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][
        1], 'ERROR! Bad transactoin!'

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() == AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'
    sleep(1)

    # Переход на страницу Адреса доставки и добавление адреса из тестового набора
    page.goto_menu(4)
    page.add_new_adress(AuthSets.adress[0][0], AuthSets.adress[0][1], AuthSets.adress[0][2], AuthSets.adress[0][3])
    page.inst_default_address()
    page.save_screen_browser(f'add_my_adress')

    # Проверка соответствия последнего введеного адреса тестовому набору
    last_add_adress = page.list_last_add_adress()
    assert last_add_adress == AuthSets.adress[0], 'ERROR! Bad last add adress'

    # Удаление последнего добавленного адреса
    page.delete_adress(-1)
    page.save_screen_browser(f'delete_my_adress')

    # Выход из кабинета
    page.exit_cabinet()


def test_edit_user_data_positive(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, переходит на страницу редактирования данных,добавляе емейл,
    дату рождения, меняет язык по умолчанию на украинский, сохраняет данные, делает скриншот и выходит из кабинета"""

    page = Headers(web_driver_auth_desktop, 10)

    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, скриншот и переход в кабинет и проверка URL кабинета
    page.input_auth_data(AuthSets.auth_phone, AuthSets.auth_passw)
    page.save_screen_browser(f'auth_cabinet')
    assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][
        1], 'ERROR! Bad transactoin!'

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() == AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Переход на страницу Личные данные и добавление емейл и дня рождения
    page.goto_menu(1)
    page.add_email(AuthSets.auth_email)
    page.add_birthday(AuthSets.birthday)
    page.change_default_lang('uk')
    page.save_personal_data()
    page.save_screen_browser(f'change_my_personal_data')

    # Проверка соответствия введеных данных тестовому набору
    list_data = page.list_personal_data()
    assert list_data[3] == AuthSets.auth_email, 'ERROR! Bad last add email'
    assert list_data[4] == AuthSets.birthday, 'ERROR! Bad last add email'

    # Очистка введеных полей и выход из кабинета
    page.clear_email_birthday_lang()
    page.exit_cabinet()

