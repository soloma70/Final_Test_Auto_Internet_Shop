# -*- encoding=utf8 -*-
from pages.sales_page import SalesPage


def test_sales_banners_sales_page(web_driver_desktop):
    """Тест проверяет видимость акционных баннеров и переход на соответствующие страницы акций"""

    page = SalesPage(web_driver_desktop, 5)
    banners = page.sales_banner_imgs
    btns = page.sales_banner_btns

    # Проверка видимости баннеров
    for index in range(len(banners)):
        banner = page.find_banner(index)
        assert banner.is_displayed(), 'ERROR! Banner not displayed'

    # Проверка перехода на страницу акции
    for index in range(len(btns)):
        url_banner, url_page = page.goto_page_banner(index)
        assert url_banner == url_page, "ERROR! Banner's URL Banner not displayed"
        page.get_url(page.url)


def test_sales_products_sales_page(web_driver_desktop):
    """Тест проверяет переход на страницу 1-го акционного товара и добавление его в корзину
    с параметрами по умолчанию (сложная проверка с изменениями диоптрий, кривизны, типа упаковки
    и количества в отдельных тестах), делает скриншот"""

    page = SalesPage(web_driver_desktop, 5)
    amount_cart_before = page.amount_cart()

    # Переход на страницу акции
    page.goto_page_banner(0)

    # Добавление в корзину акционного продукта с параметрами заказа по умолчанию
    page.add_cart_lens_def_par(0)
    amount_cart_after = page.amount_cart()
    assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"

    page.win_scroll_begin()
    page.save_screen_browser('add_cart_1_sales_prod')

    # Изменение параметров линзы - одинаковые линзы
    # price_before = int(web_driver_desktop.find_element(*ProductLensLocators.price).text)
    # web_driver_desktop.find_element(*ProductLensLocators.dioptr_same).click()
    # dioptr_list = web_driver_desktop.find_elements(*ProductLensLocators.dioptr_list)
    # ActionChains(web_driver_desktop).move_to_element(dioptr_list[21]).click().perform()
    # web_driver_desktop.find_element(*ProductLensLocators.curv_same).click()
    # curv_list = web_driver_desktop.find_elements(*ProductLensLocators.curv_list)
    # ActionChains(web_driver_desktop).move_to_element(curv_list[1]).click().perform()

    # Тестирование изменений количества упаковок
    # plus = web_driver_desktop.find_element(*ProductLensLocators.amount_plus_same)
    # plus.click()
    # plus.click()
    # price_after = int(web_driver_desktop.find_element(*ProductLensLocators.price).text)
    # assert price_after == price_before * 3, "ERROR! Sum's not eqw"
    # #
    # minus = web_driver_desktop.find_element(*ProductLensLocators.amount_minus_same)
    # minus.click()
    # minus.click()
    # web_driver_desktop.find_element(*ProductLensLocators.buy_btn).click()
    # web_driver_desktop.find_element(*ProductLensLocators.close_cart_popup).click()
    # amount_cart_after2 = int(web_driver_desktop.find_element(*SalesLocators.amount_cart).text)
    # assert amount_cart_after1 + 1 == amount_cart_after2, "ERROR! Product don't add to cart"


def test_sales_prod_sales_page(web_driver_desktop):
    """Тест проверяет переход на соответствующие страницы акционных линз"""

    page = SalesPage(web_driver_desktop, 5)
    product_banners = page.sales_product

    # Проверка перехода на страницы акции
    for index in range(len(product_banners)):
        url_banner, url_page = page.goto_product_page(index)
        assert url_banner == url_page, "ERROR! Banner's URL Banner not displayed"
        page.get_url(page.url)
