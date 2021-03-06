# -*- encoding=utf8 -*-

from time import sleep
import pytest
from pages.start_page import StartPage


@pytest.mark.smoke
@pytest.mark.parametrize("width", [480, 1280, 1440]
    , ids=['win size 480x960', 'win size 1200x960', 'win size 1440x960'])
def test_start_page_firefox(web_driver_gecko, width):
    """Тест проверяет загрузку стартовой страницы магазина и переход к ее отдельным блокам в браузере Firefox
    на различных размерах экрана, что соответствует разным мобильным и десктопным устройствам"""

    page = StartPage(web_driver_gecko)
    if width in (480, 960):
        assert page.logo_img_mob().is_displayed() is True, "ERROR screen"
    else:
        assert page.logo_img().is_displayed() is True, "ERROR screen"

    element_sales_banners = page.goto_sales_banners()
    sleep(0.5)
    assert element_sales_banners.is_displayed() is True, "ERROR screen"
    element_love_brands = page.goto_love_brands()
    sleep(0.5)
    assert element_love_brands.is_displayed() is True, "ERROR screen"
    element_benefit = page.goto_benefit()
    sleep(0.5)
    assert element_benefit.is_displayed() is True, "ERROR screen"
    element_blog = page.goto_blog()
    sleep(0.5)
    assert element_blog.is_displayed() is True, "ERROR screen"
    element_footers_img = page.goto_footers_img()
    sleep(0.5)
    assert element_footers_img.is_displayed() is True, "ERROR screen"


@pytest.mark.smoke
@pytest.mark.parametrize("width", [480, 1280, 1440]
    , ids=['win size 480x960', 'win size 1200x960', 'win size 1440x960'])
def test_start_page_edge(web_driver_edge, width):
    """Тест проверяет загрузку стартовой страницы магазина и переход к ее отдельным блокам в браузере Edge
    на различных размерах экрана, что соответствует разным мобильным и десктопным устройствам"""

    page = StartPage(web_driver_edge)
    if width in (480, 960):
        assert page.logo_img_mob().is_displayed() is True, "ERROR screen"
    else:
        assert page.logo_img().is_displayed() is True, "ERROR screen"

    element_sales_banners = page.goto_sales_banners()
    sleep(0.5)
    assert element_sales_banners.is_displayed() is True, "ERROR screen"
    element_love_brands = page.goto_love_brands()
    sleep(0.5)
    assert element_love_brands.is_displayed() is True, "ERROR screen"
    element_benefit = page.goto_benefit()
    sleep(0.5)
    assert element_benefit.is_displayed() is True, "ERROR screen"
    element_blog = page.goto_blog()
    sleep(0.5)
    assert element_blog.is_displayed() is True, "ERROR screen"
    element_footers_img = page.goto_footers_img()
    sleep(0.5)
    assert element_footers_img.is_displayed() is True, "ERROR screen"


@pytest.mark.smoke
@pytest.mark.parametrize("width", [480, 1280, 1440]
    , ids=['win size 480x960', 'win size 1200x960', 'win size 1440x960'])
def test_start_page_opera(web_driver_opera, width):
    """Тест проверяет загрузку стартовой страницы магазина в браузере Opera на различных размерах экрана,
    что соответствует разным мобильным и десктопным устройствам"""

    StartPage(web_driver_opera)
    sleep(1)
