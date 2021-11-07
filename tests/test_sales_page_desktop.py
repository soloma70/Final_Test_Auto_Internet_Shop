# -*- encoding=utf8 -*-

import time, pytest
from pages.sales_page import SalesPage
from pages.locators import SalesLocators, ProductCartLocators
from pages.url_list import LinsaUa
from selenium.webdriver.common.action_chains import ActionChains
from settings import registr_name, registr_phone, registr_passw
from pages.aux_metods import AuxMetods


def test_sales_banners_sales_page(web_driver_desktop):
    """Тест проверяет видимость акционных баннеров и переход на соответствующие страницы акций"""

    page = SalesPage(web_driver_desktop, 5)
    banners = page.sales_banner_imgs
    btns = page.sales_banner_btns

    # Проверка видимости баннеров
    for index in range(len(banners)):
        banner = web_driver_desktop.find_elements(*SalesLocators.sales_banner_imgs)[index]
        assert banner.is_displayed(), 'ERROR! Banner not displayed'

    # Проверка перехода на страницу акции
    for index in range(len(btns)):
        url_banner = web_driver_desktop.find_elements(*SalesLocators.sales_banner_btns)[index].get_attribute('href')
        web_driver_desktop.find_elements(*SalesLocators.sales_banner_btns)[index].click()
        url_page = web_driver_desktop.current_url
        assert url_banner == url_page, "ERROR! Banner's URL Banner not displayed"
        web_driver_desktop.get(LinsaUa.sales_url())


def test_sales_products_sales_page(web_driver_desktop):
    """Тест проверяет добавление в корзину акционных товаров и переход на страницу акционных товаров"""

    page = SalesPage(web_driver_desktop, 5)

    # Добавление в корзину акционных продуктов

    amount_cart_before = int(web_driver_desktop.find_element(*SalesLocators.amount_cart).text)
    url_product = web_driver_desktop.find_elements(*SalesLocators.sales_products)[0].get_attribute('href')
    element_to_hover_over = web_driver_desktop.find_element(*SalesLocators.sales_products)[0]
    hover = ActionChains(web_driver_desktop).move_to_element(element_to_hover_over)
    hover.perform()
    web_driver_desktop.find_element(*SalesLocators.sales_products_buy).click()


    web_driver_desktop.find_element(*SalesLocators.close_cart_popup).click()

    web_driver_desktop.find_element(*SalesLocators.logo_img).click()
    amount_cart_after = int(web_driver_desktop.find_element(*StartLocators.amount_cart).text)
    assert amount_cart_before+1 == amount_cart_after, "ERROR! Product don't add to cart"
