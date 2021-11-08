# -*- encoding=utf8 -*-
from time import sleep
from pages.sales_page import SalesPage
from pages.locators import SalesLocators, ProductLensLocators
from pages.url_list import LinsaUa
from selenium.webdriver.common.action_chains import ActionChains


def test_sales_banners_sales_page(web_driver_desktop):
    """Тест проверяет видимость акционных баннеров и переход на соответствующие страницы акций"""

    page = SalesPage(web_driver_desktop, 5)
    banners = page.sales_banner_imgs
    btns = page.sales_banner_btns

    # Проверка видимости баннеров
    for index in range(len(banners)):
        banner = web_driver_desktop.find_elements(*SalesLocators.banner_imgs)[index]
        assert banner.is_displayed(), 'ERROR! Banner not displayed'

    # Проверка перехода на страницу акции
    for index in range(len(btns)):
        url_banner = web_driver_desktop.find_elements(*SalesLocators.banner_btns)[index].get_attribute('href')
        web_driver_desktop.find_elements(*SalesLocators.banner_btns)[index].click()
        url_page = web_driver_desktop.current_url
        assert url_banner == url_page, "ERROR! Banner's URL Banner not displayed"
        web_driver_desktop.get(LinsaUa.sales_url())


def test_sales_products_sales_page(web_driver_desktop):
    """Тест проверяет переход на страницу 1-го акционного товара и добавление его в корзину"""

    page = SalesPage(web_driver_desktop, 5)

    # Переход на страницу акции
    amount_cart_before = int(page.amount_cart.text)
    page.sales_banner_btns[0].click()

    # Добавление в корзину акционного продукта с параметрами заказа по умолчанию
    element = web_driver_desktop.find_element(*SalesLocators.product_banner)
    ActionChains(web_driver_desktop).move_to_element(element).perform()
    web_driver_desktop.find_element(*SalesLocators.products_banner_buy).click()
    web_driver_desktop.find_element(*ProductLensLocators.buy_btn).click()
    web_driver_desktop.find_element(*ProductLensLocators.close_cart_popup).click()
    amount_cart_after1 = int(web_driver_desktop.find_element(*SalesLocators.amount_cart).text)
    assert amount_cart_before + 1 == amount_cart_after1, "ERROR! Product don't add to cart"

    # Изменение параметров линзы - одинаковые линзы
    price_before = int(web_driver_desktop.find_element(*ProductLensLocators.price).text)
    web_driver_desktop.find_element(*ProductLensLocators.dioptr_same).click()
    dioptr_list = web_driver_desktop.find_elements(*ProductLensLocators.dioptr_list)
    ActionChains(web_driver_desktop).move_to_element(dioptr_list[21]).click().perform()
    web_driver_desktop.find_element(*ProductLensLocators.curv_same).click()
    curv_list = web_driver_desktop.find_elements(*ProductLensLocators.curv_list)
    ActionChains(web_driver_desktop).move_to_element(curv_list[1]).click().perform()

    # Тестирование изменений количества упаковок
    plus = web_driver_desktop.find_element(*ProductLensLocators.amount_plus_same)
    plus.click()
    plus.click()
    price_after = int(web_driver_desktop.find_element(*ProductLensLocators.price).text)
    assert price_after == price_before * 3, "ERROR! Sum's not eqw"
    #
    minus = web_driver_desktop.find_element(*ProductLensLocators.amount_minus_same)
    minus.click()
    minus.click()
    web_driver_desktop.find_element(*ProductLensLocators.buy_btn).click()
    web_driver_desktop.find_element(*ProductLensLocators.close_cart_popup).click()
    amount_cart_after2 = int(web_driver_desktop.find_element(*SalesLocators.amount_cart).text)
    assert amount_cart_after1 + 1 == amount_cart_after2, "ERROR! Product don't add to cart"


def test_sales_prod_sales_page(web_driver_desktop):
    """Тест проверяет переход на соответствующие страницы акционных линз"""

    page = SalesPage(web_driver_desktop, 5)
    product_banners = page.sales_product

    # Проверка перехода на страницы акции
    for index in range(len(product_banners)):
        url_banner = web_driver_desktop.find_elements(*SalesLocators.products)[index].get_attribute('href')
        web_driver_desktop.find_elements(*SalesLocators.products)[index].click()
        sleep(1)
        url_page = web_driver_desktop.current_url
        assert url_banner == url_page, "ERROR! Banner's URL Banner not displayed"
        web_driver_desktop.get(LinsaUa.sales_url())