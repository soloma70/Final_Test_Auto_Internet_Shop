# -*- encoding=utf8 -*-
import time

import pytest
from pages.cabinet import CabinetPage
from pages.headers import Headers
from pages.test_sets import RegSets, AuthSets
from pages.url_list import LinsaUa
from pages.aux_metods import AuxMetods


@pytest.mark.smoke
@pytest.mark.positive
def test_registration_valid(web_driver_desktop):
    """Тест проверяет регистрацию пользователя с валидными параметрами и после успешной регистрации переходит в кабинет,
    выходит из кабинета.
    Для регистрации система запрашивает код подтверждения по SMS - 6 цифр и для успешной регистрации телефон
    д.б. реальным. Поэтому проверка выполняется только до момента введения кода и проверяется, что код не подходит
    В случае получения правильного кода нужно раскоментировать блок для правильного кода смс"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации и переход в окно регистрации
    page.registr_click()

    # Ввод данных регистрации, скриншот и переход в кабинет
    page.input_reg_data(RegSets.reg_name, RegSets.reg_phone, RegSets.reg_passw )
    page.save_screen_browser('reg_site')
    page.reg_submit()

    # Блок для неправильного кода смс
    answer = page.enter_sms_code('123456')
    page.reg_sms_close()
    assert answer == 'Неверный код подтверждения'

    # Блок для правильного кода смс
    # page.wait_download_cabinet()
    # assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][
    #    1], 'ERROR! Bad transaction!'

    # page = CabinetPage(web_driver_desktop)
    # page.save_screen_browser('reg_cabinet')
    # assert page.cabinet_name.text.strip() == RegSets.reg_name.upper(), 'ERROR! Start Image is not displayed'
    #
    # page.exit_cabinet()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# @pytest.mark.negative
# @pytest.mark.parametrize("login",
#                          ['123456', AuxMetods.generate_number(50), AuxMetods.generate_string(255),
#                           AuxMetods.russian_chars(), AuxMetods.chinese_chars(), AuxMetods.special_chars()]
#     , ids=['6 int', 'random int', '255 sym', 'russian', 'chinese', 'specials'])
# @pytest.mark.parametrize("passw",
#                          ['123456', AuxMetods.generate_number(50), AuxMetods.generate_string(255),
#                           AuxMetods.russian_chars(), AuxMetods.chinese_chars(), AuxMetods.special_chars()]
#     , ids=['6 int', 'random int', '255 sym', 'russian', 'chinese', 'specials'])

@pytest.mark.negative
def test_registration_already_registered_user(web_driver_desktop):
    """Тест проверяет регистрацию уже существующего пользователя"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации и переход в окно регистрации
    page.registr_click()

    # Ввод данных авторизации, получение ответа и сравление с ожиданием
    page.input_reg_data(AuthSets.auth_name, AuthSets.auth_phone, AuthSets.auth_passw)
    page.reg_submit()
    answer = page.answer_nonvalid_registr()
    assert answer == '* Этот телефон уже занят'
