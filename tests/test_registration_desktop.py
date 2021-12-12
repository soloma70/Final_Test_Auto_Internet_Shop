# -*- encoding=utf8 -*-

import pytest
from pages.headers import Headers
from pages.test_sets import RegSets, AuthSets
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
    page.wait_download_reg_win()

    # Ввод данных регистрации, скриншот и переход в кабинет
    page.input_reg_data(RegSets.reg_name, RegSets.reg_phone, RegSets.reg_passw)
    page.save_screen_browser('reg_site')
    page.reg_submit()

    # Блок для неправильного кода смс
    page.wait_reg_sms()
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


@pytest.mark.negative
def test_registration_already_registered_user(web_driver_desktop):
    """Тест проверяет регистрацию уже существующего пользователя"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации и переход в окно регистрации
    page.registr_click()
    page.wait_download_reg_win()

    # Ввод данных авторизации, получение ответа и сравление с ожиданием
    page.input_reg_data(AuthSets.auth_name, AuthSets.auth_phone, AuthSets.auth_passw)
    page.reg_submit()
    answer = page.answer_nonvalid_registr()
    assert answer == '* Этот телефон уже занят'


@pytest.mark.negative
@pytest.mark.parametrize("phone",
                         ['123456', AuxMetods.random_phone(10), AuxMetods.random_phone(255)]
    , ids=['6 num', '10 num', '255 num'])
def test_registration_nonvalid_phone_number(web_driver_desktop, phone):
    """Тест проверяет регистрацию с валидными именем и паролем, неверным форматом номера телефона"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации и переход в окно регистрации
    page.registr_click()
    page.wait_download_reg_win()

    # Ввод данных авторизации, получение ответа и сравнение с ожиданием
    page.input_reg_data(RegSets.reg_name, phone, RegSets.reg_passw)
    page.reg_submit()
    if len(phone) < 9:
        answer = page.answer_nonvalid_registr()
        assert answer == '* Неверный формат номера телефона'
    else:
        page.wait_reg_sms()
        answer = page.enter_sms_code('123456')
        page.reg_sms_close()
        assert answer == 'Неверный код подтверждения'


@pytest.mark.negative
@pytest.mark.parametrize("passw",
                         [AuxMetods.random_num(5), AuxMetods.random_num(6), AuxMetods.random_num(255),
                          AuxMetods.random_num(1001), AuxMetods.random_chars(5), AuxMetods.random_chars(6),
                          AuxMetods.generate_string(255), AuxMetods.russian_chars(), AuxMetods.chinese_chars(),
                          AuxMetods.special_chars()]
    , ids=['5 int', '6 int', '255 int', '>1000 int', '5 chars', '6 chars', '255 chars', 'russian', 'chinese',
           'specials'])
def test_registration_nonvalid_password(web_driver_desktop, passw):
    """Тест проверяет регистрацию с валидными именем и телефоном, некорректным паролем
    Пароль должен быть не менее 6 символов, содержать цифры и заглавные буквы латинского алфавита.
    Опытным путем установлено, что пароль должен содержать заглавную и маленькую латинские буквы"""

    page = Headers(web_driver_desktop, 10)
    # Открытие всплывающего окна авторизации и переход в окно регистрации
    page.registr_click()
    page.wait_download_reg_win()

    # Ввод данных авторизации, получение ответа и сравление с ожиданием
    page.input_reg_data(RegSets.reg_name, RegSets.reg_phone_neg_test, passw)
    page.reg_submit()
    answer = page.answer_nonvalid_registr()
    if len(str(passw)) < 6:
        assert answer == '* Слишком короткий пароль'
    else:
        assert answer == '* Используйте цифры и заглавные буквы (латинские)'
