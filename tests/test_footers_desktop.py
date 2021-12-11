# -*- encoding=utf8 -*-

import pytest
from pages.footers import Footers
from pages.url_list import LinsaUa


@pytest.mark.smoke
@pytest.mark.positive
def test_footer_start_page(web_driver_desktop):
    """Тест проверяет кликабельность блоков в footers
    и корректность перехода по ссылкам """

    page = Footers(web_driver_desktop, 10)
    footers = []
    foot_left = page.footers_left
    foot_right = page.footers_right

    # Проверка левых и правых футеров меню
    for index in range(len(foot_left)):
        page.footers_left_click(index)
        footers.append(page.get_relative_link())
        page.get_url(page.url)

    for index in range(len(foot_right)):
        page.footers_right_click(index)
        footers.append(page.get_relative_link())
        page.get_url(page.url)

    # Проверка нижних левых и правых футеров меню
    page.footers_bottom_left_click()
    footers.append(page.get_relative_link())
    page.get_url(page.url)

    page.footers_bottom_right_click()
    footers.append(page.get_relative_link())
    page.get_url(page.url)

    # Проверка кнопок Фейсбук и Инстаграм
    for index in range(2):
        footer = page.footers_middle_click_and_goto(index)
        footers.append(footer)
        page.get_url(page.url)

    # Переход на страницу фейсбук и инстаграм не проверяется
    for index in range(10):
        assert footers[index] == LinsaUa.footers_menu_urls[index][0] or \
                footers[index] == LinsaUa.footers_menu_urls[index][1] \
             , f'ERROR! Bad transaction for {index}: {footers[index]}'
