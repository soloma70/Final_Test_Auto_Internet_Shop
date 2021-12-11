# -*- encoding=utf8 -*-

from time import sleep
import pytest
from pages.start_page import StartPage
from pages.url_list import LinsaUa
from pages.test_sets import MainMenuSets, RegSets


@pytest.mark.smoke
@pytest.mark.positive
def test_main_menu_start_page(web_driver_desktop):
    """Тест проверяет кликабельность главного меню и переход на соответствующие страницы меню"""

    page = StartPage(web_driver_desktop, 5)

    # Перебор в цикле пунктов главного меню
    for index in range(MainMenuSets.amount_menu_points):
        page.main_menu_click(index)
        assert page.get_relative_link() in (
        LinsaUa.main_menu_urls[index][0], LinsaUa.main_menu_urls[index][1]), f'Transition {index} error'
        page.get_url(page.url)


@pytest.mark.positive
def test_banners_start_page(web_driver_desktop):
    """Тест проверяет кликабельность баннеров и переход на соответствующие страницы"""

    page = StartPage(web_driver_desktop, 5)
    amount_banners = page.amount_banner()

    # Перебор в цикле баннеры
    for index in range(amount_banners):
        amount_banner, amount_page = page.banner_click(index)
        assert page.get_relative_link() in (
            LinsaUa.banners_urls[index][0], LinsaUa.banners_urls[index][1]), 'Transition error'
        assert amount_banner == amount_page, f'Different quantity: declared {amount_banner}, in fact {amount_page}'
        page.get_url(page.url)


@pytest.mark.positive
def test_action_banners_start_page(web_driver_desktop):
    """Тест проверяет кликабельность акционного баннера и переход на соответствующую страницу,
    добавление 1-й акционной позиции в корзину, делает скриншот"""

    page = StartPage(web_driver_desktop, 5)
    page.all_sales_prods_click()
    assert page.get_relative_link() in (LinsaUa.main_menu_urls[0][0], LinsaUa.main_menu_urls[1][0]), 'Transition error'
    page.get_url(page.url)
    # Добавление в корзину солнечных очков - 1-я позиция
    amount_cart_before = page.amount_cart()
    page.add_cart_lens_def_par(0)
    amount_cart_after = page.amount_cart()
    assert amount_cart_before + 1 == amount_cart_after, "ERROR! Product don't add to cart"

    page.win_scroll_begin()
    page.save_screen_browser('test_add_cart_1_sunglasses')


@pytest.mark.positive
def test_love_brands_start_page(web_driver_desktop):
    """Тест проверяет кликабельность баннеров "Любимые бренды"
    и отображение соответствующих им элементов в ленте"""

    page = StartPage(web_driver_desktop, 5)
    # Клик на "Солнцезащитные очки" и проверка всплывающей линейки
    vogue, rayban = page.love_brands_sunglasses()
    assert vogue.is_displayed() and rayban.is_displayed()
    # Клик на "Контактные линзы" и проверка всплывающей линейки
    avisor, menicon = page.love_brands_lenses()
    assert avisor.is_displayed() and menicon.is_displayed()
    # Клик на "Аксессуары" и проверка всплывающей линейки
    okvision2, okvision4 = page.love_brands_accessories()
    assert okvision2.is_displayed() or okvision4.is_displayed()
    # Скрол вверх и проверка видимости лого
    page.win_scroll_begin()
    assert page.logo_img().is_displayed(), 'ERROR! Start Image is not displayed'


@pytest.mark.positive
def test_registration_start_page(web_driver_desktop):
    """Тест проверяет кликабельность и заполнение полей формы регистрации на стартовой странице
    и делает скриншот"""

    page = StartPage(web_driver_desktop, 10)
    # Клик и проверка всплывающего окна регистрации
    popup_win = page.reg_btn_click()
    assert popup_win.is_displayed(), 'ERROR! PopUp Registration is not displayed'
    # Ввод данных регистрации, скриншот и выход закрытием всплывающего окна
    page.input_reg_data(RegSets.reg_name, RegSets.reg_phone, RegSets.reg_passw)
    # Скрол вверх и проверка видимости лого
    page.win_scroll_begin()
    assert page.logo_img().is_displayed(), 'ERROR! Start Image is not displayed'


@pytest.mark.positive
def test_blogs_start_page(web_driver_desktop):
    """Тест проверяет кликабельность блоков в разделе "Оптический блог"
    и корректность перехода по ссылкам """

    page = StartPage(web_driver_desktop, 10)
    # Получение наименований карточек новостей блога
    card_1, card_2, card_3 = page.blog_card_name()
    # Переход по карточкам
    blog_titles = []
    for i in range(3):
        title = page.blog_card_goto(i)
        blog_titles.append(title)
    # Клик на кнопку 'Больше новостей'
    blog_url = page.more_news_btn()
    # Сравнение наименований новостей и URL блога
    assert card_1 == blog_titles[0], f'ERROR! Bad transaction: {card_1} != {blog_titles[0]}'
    assert card_2 == blog_titles[1], f'ERROR! Bad transaction: {card_2} != {blog_titles[1]}'
    assert card_3 == blog_titles[2], f'ERROR! Bad transaction: {card_3} != {blog_titles[2]}'
    assert blog_url in (
        LinsaUa.main_menu_urls[5][0], LinsaUa.main_menu_urls[5][1]), f'ERROR! Bad transaction for {blog_url}'


@pytest.mark.positive
def test_more_info_start_page(web_driver_desktop):
    """Тест проверяет раскрытие блока "Больше информации" и делает скрин"""

    page = StartPage(web_driver_desktop, 10)
    # Click for card left
    page.more_info_click()
    page.win_scroll()
    sleep(3)
    page.save_screen_browser('test_more_info_start_page')
