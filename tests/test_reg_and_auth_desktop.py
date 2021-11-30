# -*- encoding=utf8 -*-

import pytest
from pages.headers import Headers
from pages.locators import StartLocators, RegLocators
from pages.start_page import StartPage
from pages.test_sets import RegSets
from pages.url_list import LinsaUa
from pages.aux_metods import AuxMetods


def test_registration_header_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Вход" """

    page = Headers(web_driver_desktop, 5)
    page.login_btn_click()
    assert web_driver_desktop.find_element(*RegLocators.login_submit).is_enabled(), 'Transition error'
    web_driver_desktop.find_element(*RegLocators.login_close).click()


def test_registration_body_start_page(web_driver_desktop):
    """Тест проверяет регистрацию нового пользователя, заполнение полей формы регистрации на стартовой странице,
    делает скриншот и переходит в кабинет"""

    page = StartPage(web_driver_desktop, 10)
    # Клик и проверка всплывающего окна регистрации
    popup_win = page.reg_btn_click()
    assert popup_win.is_displayed(), 'ERROR! PopUp Registration is not displayed'
    # Ввод данных регистрации, скриншот и выход закрытием всплывающего окна
    page.input_reg_data(RegSets.reg_name, RegSets.reg_phone, RegSets.reg_passw)
    # Скрол вверх и проверка видимости лого
    page.win_scroll_begin()
    assert page.logo_img().is_displayed(), 'ERROR! Start Image is not displayed'