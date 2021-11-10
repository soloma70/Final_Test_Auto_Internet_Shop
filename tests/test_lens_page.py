# -*- encoding=utf8 -*-
from time import sleep
from pages.lens_page import LensPage
from pages.locators import LensLocators, ProductLensLocators
from pages.url_list import LinsaUa
from selenium.webdriver.common.action_chains import ActionChains


def test_sales_banners_sales_page(web_driver_desktop):
    """Тест проверяет видимость акционных баннеров и переход на соответствующие страницы акций"""

    page = LensPage(web_driver_desktop, 5)
    filters = page.filters
    filter_list = []
    for i in range(len(filters)):
        filters[i].click()
        sleep(1)
        filter_list.append(web_driver_desktop.find_elements(*LensLocators.filter_list[i]))

    print()
    print(len(filters))
    for k in range(len(filter_list)):
        print(len(filter_list[k]))
