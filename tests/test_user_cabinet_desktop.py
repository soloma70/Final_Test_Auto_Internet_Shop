# -*- encoding=utf8 -*-
from urllib.parse import urlparse

import pytest
from pages.cabinet import CabinetPage
from pages.headers import Headers
from pages.test_sets import AuthSets
from pages.url_list import LinsaUa
from pages.aux_metods import AuxMetods
from time import sleep


@pytest.mark.positive
def test_authorization_valid(web_driver_auth_desktop):
    """Тест проверяет авторизацию пользователя с валидными параметрами и переходит в кабинет"""

    page = Headers(web_driver_auth_desktop, 10)
    # Открытие всплывающего окна авторизации
    page.login_btn_click()
    print()
    # Ввод данных авторизации, скриншот и переход в кабинет
    page.input_auth_data(AuthSets.auth_phone, AuthSets.auth_passw)
    page.save_screen_browser('auth_cabinet')
    assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][
        1], 'ERROR! Bad transactoin!'

    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() == AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'
    sleep(1)
    for i in range(1, len(page.cabinet)):
        page.goto_menu(i)
        sleep(2)

    page.exit_cabinet()


@pytest.mark.positive
def test_add_new_address(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, добавляет новый адрес доставки, делает скриншот и
    удаляет адрес, делает скришщот, выходит из кабинета"""

    page = Headers(web_driver_auth_desktop, 10)

    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, скриншот и переход в кабинет и проверка URL кабинета
    page.input_auth_data(AuthSets.auth_phone, AuthSets.auth_passw)
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
    page.save_screen_browser('add_my_adress')

    # Проверка соответствия последнего введеного адреса тестовому набору
    last_add_adress = page.list_last_add_adress()
    assert last_add_adress == AuthSets.adress[0], 'ERROR! Bad last add adress'

    # Удаление последнего добавленного адреса
    page.delete_adress(-1)
    page.save_screen_browser('delete_my_adress')

    # Выход из кабинета
    page.exit_cabinet()


@pytest.mark.positive
def test_edit_user_data(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, переходит на страницу редактирования данных,добавляе емейл,
    дату рождения, меняет язык по умолчанию на украинский, сохраняет данные, делает скриншот и выходит из кабинета"""

    page = Headers(web_driver_auth_desktop, 10)

    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, скриншот и переход в кабинет и проверка URL кабинета
    page.input_auth_data(AuthSets.auth_phone, AuthSets.auth_passw)
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
    page.save_screen_browser('change_my_personal_data')

    # Проверка соответствия введеных данных тестовому набору
    list_data = page.list_personal_data()
    assert list_data[3] == AuthSets.auth_email, 'ERROR! Bad last add email'
    assert list_data[4] == AuthSets.birthday, 'ERROR! Bad last add email'

    # Очистка введеных полей и выход из кабинета
    page.clear_email_birthday_lang()
    page.exit_cabinet()


@pytest.mark.positive
def test_wishlist_user(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, переходит на страницу списка желаний, находит продукты
    соответственно тестовым наборам, проверяет получившийся список, удаляет его и выходит из кабинета"""

    page = Headers(web_driver_auth_desktop, 10)

    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, скриншот и переход в кабинет и проверка URL кабинета
    page.input_auth_data(AuthSets.auth_phone, AuthSets.auth_passw)
    assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][
        1], 'ERROR! Bad transactoin!'

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() == AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Переход на страницу Список желаний и добавление нового списка
    page.goto_menu(2)
    status_add = page.add_new_wishlist(AuthSets.my_wish_list)
    page.save_screen_browser('add_new_wishlist')
    assert status_add == 'Успешно', "ERROR! Wishlist don't add"

    # Добавление нового продукта (линз) в wishlist
    page.goto_start_page()
    page.goto_lens_page()
    status_add_prod = page.add_random_prod_wishlist(AuthSets.my_wish_list)
    assert status_add_prod == 'Успешно', "ERROR! Wishlist don't add"

    # Переход в wishlist через кнопку в хедере, переход в тестовый список
    page.goto_wishlist_header()
    page.goto_wishlist(AuthSets.my_wish_list)
    page.save_screen_browser('add_new_product_wishlist')

    # Удаление тестового списка
    status_del = page.delete_open_wishlist()
    page.save_screen_browser('del_new_wishlist')
    assert status_del == 'Успешно', "ERROR! Wishlist don't add"
    page.exit_cabinet()
