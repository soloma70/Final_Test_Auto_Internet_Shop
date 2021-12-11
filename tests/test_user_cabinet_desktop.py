# -*- encoding=utf8 -*-

import pytest
from pages.cabinet import CabinetPage
from pages.headers import Headers
from pages.test_sets import AuthSets
from pages.aux_metods import AuxMetods


@pytest.mark.negative
@pytest.mark.parametrize("login",
                         ['123456', AuxMetods.random_num(20), AuxMetods.generate_string(255),
                          AuxMetods.russian_chars(), AuxMetods.chinese_chars(), AuxMetods.special_chars()]
    , ids=['6 int', 'random int', '255 sym', 'russian', 'chinese', 'specials'])
@pytest.mark.parametrize("passw",
                         ['123456', AuxMetods.random_num(20), AuxMetods.generate_string(255),
                          AuxMetods.russian_chars(), AuxMetods.chinese_chars(), AuxMetods.special_chars()]
    , ids=['6 int', 'random int', '255 sym', 'russian', 'chinese', 'specials'])
def test_authorization_non_valid(web_driver_desktop, login, passw):
    """Тест проверяет авторизацию с не валидными параметрами"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, получение ответа и сравление с ожиданием
    page.input_login_passw(login, passw)
    page.auth_submit()
    answer = page.answer_nonvalid_data()
    page.auth_cancel()
    assert answer == 'Проверьте правильность данных для входа'


@pytest.mark.smokie
@pytest.mark.positive
def test_authorization_valid(web_driver_auth_desktop):
    """Тест открывает кабинет пользователя, переходит на страницы бокового меню и меню в хедере"""

    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() in AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Переход по страницам бокового меню
    for i in range(1, len(page.cabinet)):
        page.goto_cabinet_menu(i)

    # Переход по страницам меню в хедере
    for i in range(1, len(page.cabinet)):
        page.goto_cabinet_menu_header(i)


@pytest.mark.positive
def test_add_new_address(web_driver_auth_desktop):
    """Тест загружает кабинет, добавляет новый адрес доставки, делает скриншот и удаляет адрес, делает скриншоот"""

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() in AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Переход на страницу Адреса доставки и добавление адреса из тестового набора
    page.goto_cabinet_menu(4)
    page.add_new_adress(AuthSets.adress[0][0], AuthSets.adress[0][1], AuthSets.adress[0][2], AuthSets.adress[0][3])
    page.inst_default_address()
    page.save_screen_browser('add_my_adress')

    # Проверка соответствия последнего введеного адреса тестовому набору
    last_add_adress = page.list_last_add_adress()
    assert last_add_adress == AuthSets.adress[0], 'ERROR! Bad last add adress'

    # Удаление последнего добавленного адреса
    page.delete_adress(-1)
    page.save_screen_browser('delete_my_adress')


@pytest.mark.positive
def test_edit_user_data(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, переходит на страницу редактирования данных,добавляе емейл,
    дату рождения, меняет язык по умолчанию на украинский, сохраняет данные, делает скриншот и выходит из кабинета"""

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() in AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Переход на страницу Личные данные и добавление емейл и дня рождения
    page.goto_cabinet_menu(1)
    page.add_email(AuthSets.auth_email)
    page.add_birthday(AuthSets.birthday)
    page.change_default_lang('uk')
    page.save_personal_data()
    page.save_screen_browser('change_my_personal_data')

    # Проверка соответствия введеных данных тестовому набору
    list_data = page.list_personal_data()
    assert list_data[3] == AuthSets.auth_email, 'ERROR! Bad last add email'
    assert list_data[4] == AuthSets.birthday, 'ERROR! Bad last add email'

    # Очистка введеных полей
    page.clear_email_birthday_lang()


@pytest.mark.integration
@pytest.mark.positive
def test_wishlist_user(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, переходит на страницу списка желаний, находит продукты
    соответственно тестовым наборам, проверяет получившийся список, удаляет его и выходит из кабинета"""

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() in AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Переход на страницу Список желаний и добавление нового списка
    page.goto_cabinet_menu(2)
    status_add = page.add_new_wishlist(AuthSets.my_wish_list)
    page.save_screen_browser('add_new_wishlist')
    assert status_add == 'Успешно', "ERROR! Wishlist don't add"

    # Добавление нового продукта (линз) в wishlist
    page.goto_start_page()
    page.goto_menu_page(1)
    status_add_prod = page.add_random_prod_wishlist(AuthSets.my_wish_list)
    assert status_add_prod == 'Успешно', "ERROR! Wishlist don't add"

    # Переход в wishlist через кнопку в хедере, переход в тестовый список
    page.goto_wishlist_header()
    page.goto_wishlist(AuthSets.my_wish_list)
    page.save_screen_browser('add_new_product_wishlist')

    # Удаление тестового списка
    status_del = page.delete_wishlist(AuthSets.my_wish_list)
    page.save_screen_browser('del_new_wishlist')
    assert status_del == 'Успешно', "ERROR! Wishlist don't add"


@pytest.mark.integration
@pytest.mark.positive
def test_add_article_in_favorite_user(web_driver_auth_desktop):
    """Тест авторизует пользователя, переходит в кабинет, переходит на страницу блогов, выбирает рандомный блог,
    добавляет в избраннае, переходит на страницу Сохраненные статьи и проверяет название статьи среди сохраненных"""

    # Инициализация экземпляра авторизованой страницы кабинета и проверка имени пользователя
    page = CabinetPage(web_driver_auth_desktop)
    assert page.cabinet_name.text.strip() in AuthSets.auth_name.upper(), 'ERROR! Start Image is not displayed'

    # Добавление новой рандомной статьи в избранное
    page.goto_menu_page(5)
    name_article = page.add_article_in_favorites()
    page.goto_cabinet_menu_header(5)
    list_articles_add = page.list_article_in_favorite()
    page.save_screen_browser('add_new_article_favorites')
    assert name_article in list_articles_add, "ERROR! New article don't add"

    # Удаление добавленной статьи
    page.delete_add_article(name_article)
    list_articles_del = page.list_article_in_favorite()
    page.save_screen_browser('del_add_article_favorites')
    assert name_article not in list_articles_del, "ERROR! New article don't del"
