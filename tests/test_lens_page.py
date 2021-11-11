# -*- encoding=utf8 -*-
from time import sleep
from pages.lens_page import LensPage
from pages.locators import LensLocators, ProductLensLocators
from pages.url_list import LinsaUa
from selenium.webdriver.common.action_chains import ActionChains


def test_amount_lens_page(web_driver_desktop):
    """Тест проверяет количество позиций на странице, суммирует по всем страницам и сравнивает
    с количеством линз в наименовании страницы"""

    page = LensPage(web_driver_desktop, 5)
    amount_lens = int(page.amount_total.text)
    amount_page = int(page.pagination[-1].text)
    amount_total = 0
    for i in range(amount_page):
        web_driver_desktop.get(web_driver_desktop.find_elements(*LensLocators.pagination)[i].get_attribute('href'))
        sleep(1)
        amount_on_page = len(web_driver_desktop.find_elements(*LensLocators.cards_lens_url))
        amount_total += amount_on_page
    page = LensPage(web_driver_desktop, 5)

    assert amount_lens == amount_total, 'ERROR! Incorrect amount lens'


def test_pagination_lens_page(web_driver_desktop):
    """Тест проверяет прямой переход по страницам раздела, а так же преход с помощью стрелок и сравнивает
    фактический URL с ожидаемым"""

    page = LensPage(web_driver_desktop, 5)
    amount_page_url = page.pagination

    for i in range(len(amount_page_url)):
        goto_url = web_driver_desktop.find_elements(*LensLocators.pagination)[i].get_attribute('href')
        web_driver_desktop.get(goto_url)
        sleep(1)
        current_url = web_driver_desktop.current_url
        assert goto_url == current_url and web_driver_desktop.find_element(*LensLocators.name).is_displayed()\
            , 'ERROR! Incorrect transaction'

    page = LensPage(web_driver_desktop, 5)
    amount_page_url = page.pagination

    for i in range(len(amount_page_url)-1):
        web_driver_desktop.find_element(*LensLocators.arrow_right).click()
        sleep(1)
        page_number = int(web_driver_desktop.current_url.split('=')[1])
        assert i+2 == page_number and web_driver_desktop.find_element(*LensLocators.name).is_displayed()\
             , 'ERROR! Incorrect transaction'

    for i in range(len(amount_page_url)-2):
        web_driver_desktop.find_element(*LensLocators.arrow_left).click()
        sleep(1)
        page_number = int(web_driver_desktop.current_url.split('=')[1])
        assert (len(amount_page_url)-1)-i == page_number and web_driver_desktop.find_element(*LensLocators.name).is_displayed()\
             , 'ERROR! Incorrect transaction'



    # filters = page.filters
    #
    # filter_list = []
    # for i in range(len(filters)):
    #     filters[i].click()
    #     sleep(1)
    #     filter_list.append(web_driver_desktop.find_elements(*LensLocators.filter_list[i]))
    #
    print()
    # print(len(filters))
    # for k in range(len(filter_list)):
    #     print()
    #     for j in range(len(filter_list[k])):
    #         print(filter_list[k][j].get_attribute('href'))
    #
    # for l in range(len(sort_by)):
    #     print(sort_by[l].get_attribute('href'))

    # cards_lens_url = page.cards_lens_url
    # card_lens_amount = page.card_lens_amount
    # card_lens_price = page.card_lens_price
    # print(len(cards_lens_url))
    # print(len(card_lens_amount))
    # print(len(card_lens_price))
    #
    # # Проверка функции сортировки
    # # Сортировка по убыванию, сортировка по возрастанию
    #
    # sort_by = page.sort_by
    # url_list_sort_by = []
    # for i in range(len(sort_by)):
    #     web_driver_desktop.find_elements(*LensLocators.sort_by)[i].click()
    #     sleep(2)
    #
    #     url_list = web_driver_desktop.find_elements(*LensLocators.cards_lens_url)
    #     url_list_act = []
    #     for j in range(len(url_list)):
    #         url = web_driver_desktop.find_elements(*LensLocators.cards_lens_url)[j].get_attribute('href')
    #         url_list_act.append(url)
    #
    #     url_list_sort_by.append(url_list_act)
    #
    # print(url_list_sort_by[0])
    # print(url_list_sort_by[1])
    # print(url_list_sort_by[2])
    # print(url_list_sort_by[3])

