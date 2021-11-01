# -*- encoding=utf8 -*-

import time, pytest
from pages.start_page import StartPage
from pages.locators import StartLocators


def test_start_page(web_driver):
    page_start = StartPage(web_driver)
    time.sleep(2)
    # page_start.start_click()
    # print('\nПроверяем, что мы находимся на стартовой странице и переходим на страницу регистрации нового пользователя')
    # assert page_start.get_relative_link() == '/new_user', 'Transition error'
    # time.sleep(2)


@pytest.mark.parametrize("width",
                         [320, 425, 960, 1101, 1201, 1280, 1440, 2440]
    , ids=[' win size 320x960', ' win size 425x960', ' win size 960x960', ' win size 1100x960'
    , ' win size 1200x960', ' win size 1280x960', ' win size 1440x960', ' win size 2450x960'])
def test_start_page_var_win_width(web_driver_var_size, width):
    page_start = StartPage(web_driver_var_size, 5)
    if width == 320 or width == 425 or width == 960:
        assert page_start.start_img_mobile.is_displayed() == True, "ERROR screen"
    else:
        assert page_start.start_img.is_displayed() == True, "ERROR screen"


@pytest.mark.parametrize("test_search", ['линзы', 'lens', 123], ids=['search ru', 'search en', 'search digit'])
def test_search_start_page_desktop_positive(web_driver_decktop, test_search):
    page_start = StartPage(web_driver_decktop, 5)
    page_start.search_field_click(test_search)
    amount = int(web_driver_decktop.find_element(*StartLocators.search_result).text)
    assert amount > 0, 'Field "Search" working unsucсess'


@pytest.mark.parametrize("test_search",
                        ['123456', StartPage.generate_string(255), StartPage.generate_string(1001)
                        , StartPage.russian_chars(), StartPage.russian_chars().upper(), StartPage.chinese_chars()
                        , StartPage.special_chars()]
                        , ids=['any', '255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'chinese', 'specials'])
def test_search_start_page_desktop_positive(web_driver_decktop, test_search):
    page_start = StartPage(web_driver_decktop, 5)
    page_start.search_field_click(test_search)
    amount = int(web_driver_decktop.find_element(*StartLocators.search_result).text)
    assert amount == 0, 'Field "Search" working unsucсess'


def test_header_start_page_mobile(web_driver_mobile):
    page_start = StartPage(web_driver_mobile)
    time.sleep(2)
    page_start.start_img_click_mobile()
    time.sleep(2)
