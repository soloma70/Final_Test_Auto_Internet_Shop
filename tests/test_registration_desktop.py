# -*- encoding=utf8 -*-

import pytest
from pages.cabinet import CabinetPage
from pages.headers import Headers
from pages.test_sets import RegSets
from pages.url_list import LinsaUa
from pages.aux_metods import AuxMetods


@pytest.mark.skip
@pytest.mark.positive
def test_authorization_valid(web_driver_desktop):
    """Тест проверяет регистрацию пользователя с валидными параметрами и после успешной регистрации переходит в кабинет,
    выходит из кабинета.
    Тест помечен, как пропускаемый, так как для регистрации система запрашивает код подтверждения по SMS - 6 цифр
    и для успешной регистрации телефон д.б. реальным"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации и переход в окно регистрации
    page.registr_click()

    # Ввод данных регистрации, скриншот и переход в кабинет
    page.input_reg_data(RegSets.reg_name, RegSets.reg_phone, RegSets.reg_passw )
    page.save_screen_browser('reg_site')
    page.reg_submit()
    page.wait_download_cabinet()
    assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][
        1], 'ERROR! Bad transactoin!'

    page = CabinetPage(web_driver_desktop)
    page.save_screen_browser('reg_cabinet')
    assert page.cabinet_name.text.strip() == RegSets.reg_name.upper(), 'ERROR! Start Image is not displayed'

    page.exit_cabinet()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@pytest.mark.negative
@pytest.mark.parametrize("login",
                         ['123456', AuxMetods.generate_number(50), AuxMetods.generate_string(255),
                          AuxMetods.russian_chars(), AuxMetods.chinese_chars(), AuxMetods.special_chars()]
    , ids=['6 int', 'random int', '255 sym', 'russian', 'chinese', 'specials'])
@pytest.mark.parametrize("passw",
                         ['123456', AuxMetods.generate_number(50), AuxMetods.generate_string(255),
                          AuxMetods.russian_chars(), AuxMetods.chinese_chars(), AuxMetods.special_chars()]
    , ids=['6 int', 'random int', '255 sym', 'russian', 'chinese', 'specials'])
def test_authorization_non_valid(web_driver_desktop, login, passw):
    """Тест проверяет авторизацию с не валидными параметрами"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, получение ответа и сравление с ожиданием
    answer = page.input_auth_nonvalid_data(login, passw)
    assert answer == 'Проверьте правильность данных для входа'
