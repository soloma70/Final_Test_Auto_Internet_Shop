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
