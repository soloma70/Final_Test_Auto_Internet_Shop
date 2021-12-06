# -*- encoding=utf8 -*-

import pytest
from pages.sales_page import SalesPage


@pytest.mark.smoke
@pytest.mark.positive
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


@pytest.mark.smoke
@pytest.mark.positive
def test_sales_products_sales_page(web_driver_desktop):
    """Тест проверяет переход на страницу 1-го акционного товара и добавление его в корзину
    с параметрами по умолчанию (сложная проверка с изменениями диоптрий, кривизны, типа упаковки
    и количества в тестах user stories), делает скриншот"""

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


@pytest.mark.smoke
@pytest.mark.positive
def test_sales_prod_sales_page(web_driver_desktop):
    """Тест проверяет переход на соответствующие страницы акционных линз"""

    page = SalesPage(web_driver_desktop, 5)
    product_banners = page.sales_product

    # Проверка перехода на страницы акции
    for index in range(len(product_banners)):
        url_banner, url_page = page.goto_product_page(index)
        assert url_banner == url_page, "ERROR! Banner's URL Banner not displayed"
        page.get_url(page.url)
