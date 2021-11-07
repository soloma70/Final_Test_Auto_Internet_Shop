# -*- encoding=utf8 -*-

import time, pytest
from pages.start_page import StartPage
from pages.locators import StartLocators
from pages.url_list import LinsaUa
from selenium.webdriver.common.action_chains import ActionChains
from settings import registr_name, registr_phone, registr_passw
from pages.aux_metods import AuxMetods


# Тестирование десктопной версии сайта
def test_start_page(web_driver_desktop):
    """Тест проверяет кликабельность лого сайта и перезагрузку его стартовой страницы"""

    page_start = StartPage(web_driver_desktop)
    page_start.start_img_click()
    assert page_start.get_relative_link() == '/' or \
           page_start.get_relative_link() == '/uk/', 'Transition error'


@pytest.mark.parametrize("test_search_p", ['линзы', 'lens', 123], ids=['search ru', 'search en', 'search digit'])
def test_search_start_page_positive(web_driver_desktop, test_search_p):
    """Тест проверяет работу поиска с различными позитивными данными"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.search_field_click(test_search_p)
    amount = int(web_driver_desktop.find_element(*StartLocators.search_result).text)
    assert amount > 0, 'Field "Search" working unsucсess'


@pytest.mark.parametrize("test_search",
                        ['123456', AuxMetods.generate_string(255), AuxMetods.generate_string(1001)
                        , AuxMetods.russian_chars(), AuxMetods.russian_chars().upper(), AuxMetods.chinese_chars()
                        , AuxMetods.special_chars()]
                        , ids=['any', '255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'chinese', 'specials'])
def test_search_start_page_negative(web_driver_desktop, test_search):
    """Тест проверяет поле поиска с различными негативными данными и корректность обработки запроса"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.search_field_click(test_search)
    amount = int(web_driver_desktop.find_element(*StartLocators.search_result).text)
    assert amount == 0, 'Field "Search" working unsucсess'


def test_callback_btn_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Перезвоните мне" и загрузку формы обратного звонка, после чего закрывает ее"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.callback_btn_click()
    time.sleep(2)
    assert web_driver_desktop.find_element(*StartLocators.callback_form_submit).is_enabled()\
        , 'Transition error'
    web_driver_desktop.find_element(*StartLocators.callback_form_close).click()
    time.sleep(2)


def test_login_btn_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Вход" """

    page_start = StartPage(web_driver_desktop, 5)
    page_start.login_btn_click()
    assert web_driver_desktop.find_element(*StartLocators.login_submit).is_enabled()\
        , 'Transition error'
    web_driver_desktop.find_element(*StartLocators.login_close).click()


def test_wishlist_btn_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Список желаний" без авторизации"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.wishlist_btn_click()
    assert web_driver_desktop.find_element(*StartLocators.login_submit).is_enabled()\
        , 'Transition error'
    web_driver_desktop.find_element(*StartLocators.login_close).click()


def test_cart_start_page(web_driver_desktop):
    """Тест проверяет кликабельность "Корзина" без авторизации"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.cart_btn_click()
    assert page_start.get_relative_link() == '/ru/cart/' \
           or page_start.get_relative_link() == '/uk/cart/', 'Transition error'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()


def test_lang_start_page(web_driver_desktop):
    """Тест проверяет переключение языков сайта Рус и Укр"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.lang_btn_click()
    page_start.lang_uk_btn_click()
    assert page_start.get_relative_link() == '/uk/', 'Transition error'
    web_driver_desktop.find_element(*StartLocators.lang_btn_active).click()
    web_driver_desktop.find_element(*StartLocators.lang_btn_ru).click()
    assert page_start.get_relative_link() == '/', 'Transition error'


def test_menu_start_page(web_driver_desktop):
    """Тест проверяет кликабельность меню и переход на соответствующие страницы меню, закрытие меню"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.menu_btn_click()
    page_start.menu_close_btn_click()
    assert page_start.get_relative_link() == '/' or \
           page_start.get_relative_link() == '/uk/', 'Transition error'

    # Перебор в цикле пунктов меню
    menu_points = page_start.menu_points
    for index in range(len(menu_points)):
        web_driver_desktop.find_element(*StartLocators.menu_button).click()
        web_driver_desktop.find_elements(*StartLocators.menu_points)[index].click()
        time.sleep(2)
        assert page_start.get_relative_link() == LinsaUa.right_menu_urls[index][0] or \
               page_start.get_relative_link() == LinsaUa.right_menu_urls[index][1], 'Transition error'
        web_driver_desktop.find_element(*StartLocators.logo_img).click()


def test_main_menu_start_page(web_driver_desktop):
    """Тест проверяет кликабельность главного меню и переход на соответствующие страницы меню"""

    page_start = StartPage(web_driver_desktop, 5)

    # Перебор в цикле пунктов главного меню
    for index in range(6):
        web_driver_desktop.find_elements(*StartLocators.main_menu_points)[index].click()
        time.sleep(2)
        assert page_start.get_relative_link() == LinsaUa.main_menu_urls[index][0] or \
               page_start.get_relative_link() == LinsaUa.main_menu_urls[index][1], 'Transition error'
        web_driver_desktop.find_element(*StartLocators.logo_img).click()
        time.sleep(2)

def test_banners_start_page(web_driver_desktop):
    """Тест проверяет кликабельность баннеров и переход на соответствующие страницы"""

    page_start = StartPage(web_driver_desktop, 5)

    # Перебор в цикле баннеры
    for index in range(3):
        amount_banner_text = web_driver_desktop.find_elements(*StartLocators.banner_points)[index].text.split()
        amount_banner = int(amount_banner_text[0].strip())
        web_driver_desktop.find_elements(*StartLocators.banner_points)[index].click()
        time.sleep(2)
        amount_page = int(web_driver_desktop.find_element(*StartLocators.amount_product).text.strip())
        assert page_start.get_relative_link() == LinsaUa.banners_urls[index][0] or \
               page_start.get_relative_link() == LinsaUa.banners_urls[index][1], 'Transition error'
        assert amount_banner == amount_page, f'Different quantity: declared {amount_banner}, in fact {amount_page}'
        web_driver_desktop.find_element(*StartLocators.logo_img).click()
        time.sleep(2)

def test_action_banners_start_page(web_driver_desktop):
    """Тест проверяет кликабельность акционного баннера и переход на соответствующую страницу,
    добавление 1-й акционной позиции в корзину"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.all_sales_prods_click()
    assert page_start.get_relative_link() == LinsaUa.main_menu_urls[0][0] or \
           page_start.get_relative_link() == LinsaUa.main_menu_urls[1][0], 'Transition error'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    # Добавление в корзину солнечных очков
    amount_cart_before = int(web_driver_desktop.find_element(*StartLocators.amount_cart).text)
    element_to_hover_over = web_driver_desktop.find_element(*StartLocators.sales_sunglass)
    hover = ActionChains(web_driver_desktop).move_to_element(element_to_hover_over)
    hover.perform()
    web_driver_desktop.find_element(*StartLocators.sales_add_cart_sunglass).click()
    web_driver_desktop.find_element(*StartLocators.close_cart_popup).click()
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    amount_cart_after = int(web_driver_desktop.find_element(*StartLocators.amount_cart).text)
    assert amount_cart_before+1 == amount_cart_after, "ERROR! Product don't add to cart"


def test_love_brands_start_page(web_driver_desktop):
    """Тест проверяет кликабельность баннеров "Любимые бренды"
    и отображение соответствующих им элементов в ленте"""

    page_start = StartPage(web_driver_desktop, 5)
    page_start.love_brands_sunglasses.click()
    time.sleep(2)
    assert page_start.vogue.is_displayed() and page_start.rayban.is_displayed()
    page_start.love_brands_lenses.click()
    time.sleep(2)
    assert page_start.avisor.is_displayed() and page_start.menicon.is_displayed()
    page_start.love_brands_accessories.click()
    time.sleep(2)
    assert page_start.okvision[2].is_displayed() or page_start.okvision[1].is_displayed()
    web_driver_desktop.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)
    assert web_driver_desktop.find_element(*StartLocators.logo_img).is_displayed(), \
        'ERROR! Start Image is not displayed'

def test_registration_start_page(web_driver_desktop):
    """Тест проверяет кликабельность и заполнение полей формы регистрации на стартовой странице """

    page_start = StartPage(web_driver_desktop, 10)
    page_start.reg_btn.click()
    assert web_driver_desktop.find_element(*StartLocators.registr_popup_windows).is_displayed(), \
        'ERROR! PopUp Registration is not displayed'
    name = web_driver_desktop.find_element(*StartLocators.registr_popup_name)
    name.clear()
    name.send_keys(registr_name)
    phone = web_driver_desktop.find_element(*StartLocators.registr_popup_phone)
    phone.clear()
    phone.send_keys(registr_phone)
    passw = web_driver_desktop.find_element(*StartLocators.registr_popup_passw)
    passw.clear()
    passw.send_keys(registr_passw)
    web_driver_desktop.find_element(*StartLocators.registr_popup_chec).click()
    time.sleep(3)
    page_start.close.click()
    web_driver_desktop.execute_script("window.scrollTo(0, 0)")
    assert web_driver_desktop.find_element(*StartLocators.logo_img).is_displayed(), \
        'ERROR! Start Image is not displayed'


def test_blogs_start_page(web_driver_desktop):
    """Тест проверяет кликабельность блоков в разделе "Оптический блог"
    и корректность перехода по ссылкам """

    page_start = StartPage(web_driver_desktop, 10)
    # page_start.win_scroll_bl
    blog_card_11 = page_start.blog_card_1
    blog_card_1 = page_start.blog_card_1.text
    blog_card_2 = page_start.blog_card_2.text
    blog_card_3 = page_start.blog_card_3.text
    # Click for card 1
    blog_card_11.click()
    blog_title_1 = web_driver_desktop.find_element(*StartLocators.blog_title).text
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    # Click for card 2
    web_driver_desktop.find_element(*StartLocators.blog_card_2).click()
    blog_title_2 = web_driver_desktop.find_element(*StartLocators.blog_title).text
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    # Click for card 3
    web_driver_desktop.find_element(*StartLocators.blog_card_3).click()
    blog_title_3 = web_driver_desktop.find_element(*StartLocators.blog_title).text
    web_driver_desktop.find_element(*StartLocators.logo_img).click()
    # Click for btn 'Больше новостей'
    web_driver_desktop.find_element(*StartLocators.blog_btn).click()
    blog_url = page_start.get_relative_link()
    web_driver_desktop.find_element(*StartLocators.logo_img).click()

    assert blog_card_1 == blog_title_1, f'ERROR! Bad transaction: {blog_card_1} != {blog_title_1}'
    assert blog_card_2 == blog_title_2, f'ERROR! Bad transaction: {blog_card_2} != {blog_title_2}'
    assert blog_card_3 == blog_title_3, f'ERROR! Bad transaction: {blog_card_3} != {blog_title_3}'
    assert blog_url == LinsaUa.main_menu_urls[5][0] or blog_url == LinsaUa.main_menu_urls[5][1]\
        , f'ERROR! Bad transaction for {blog_url}'


def test_about_start_page(web_driver_desktop):
    """Тест проверяет кликабельность блоков в разделе "О нас"
    и корректность перехода по ссылкам """

    page_start = StartPage(web_driver_desktop, 10)
    # page_start.win_scroll_bl
    # Click for card left
    web_driver_desktop.find_element(*StartLocators.about_left_btn).click()
    time.sleep(2)
    assert page_start.get_relative_link() == LinsaUa.right_menu_urls[1][0] or \
           page_start.get_relative_link() == LinsaUa.right_menu_urls[1][1] \
        , f'ERROR! Bad transaction for {page_start.get_relative_link()}'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()

    # Click for card right
    web_driver_desktop.find_element(*StartLocators.about_right_btn).click()
    time.sleep(2)
    assert page_start.get_relative_link() == LinsaUa.main_menu_urls[3][0] or \
           page_start.get_relative_link() == LinsaUa.main_menu_urls[3][1] \
        , f'ERROR! Bad transaction for {page_start.get_relative_link()}'
    web_driver_desktop.find_element(*StartLocators.logo_img).click()


def test_footer_start_page(web_driver_desktop):
    """Тест проверяет кликабельность блоков в footers
    и корректность перехода по ссылкам """

    page_start = StartPage(web_driver_desktop, 10)
    pages_footers = []
    footers_left = page_start.footers_left_btns
    footers_right = page_start.footers_right_btns

    for index, locator in enumerate(footers_left):
        web_driver_desktop.find_elements(*StartLocators.footers_left_btns)[index].click()
        pages_footers.append(page_start.get_relative_link())
        web_driver_desktop.find_element(*StartLocators.logo_img).click()

    for index, locator in enumerate(footers_right):
        web_driver_desktop.find_elements(*StartLocators.footers_right_btns)[index].click()
        pages_footers.append(page_start.get_relative_link())
        web_driver_desktop.find_element(*StartLocators.logo_img).click()

    web_driver_desktop.find_element(*StartLocators.footer_bottom_left_btn).click()
    pages_footers.append(page_start.get_relative_link())
    web_driver_desktop.find_element(*StartLocators.logo_img).click()

    web_driver_desktop.find_element(*StartLocators.footer_bottom_right_btn).click()
    pages_footers.append(page_start.get_relative_link())
    web_driver_desktop.find_element(*StartLocators.logo_img).click()

    for index in range(2):
        web_driver_desktop.find_elements(*StartLocators.footer_middle_btns)[index].click()
        windows = web_driver_desktop.window_handles
        web_driver_desktop.switch_to.window(windows[1])
        pages_footers.append(web_driver_desktop.current_url)
        web_driver_desktop.close()
        time.sleep(2)
        web_driver_desktop.switch_to.window(windows[0])
        web_driver_desktop.find_element(*StartLocators.logo_img).click()

    # Переход на страницу инстаграм не проверяется, требует логин инстаграм
    for index in range(11):
        assert pages_footers[index] == LinsaUa.footers_menu_urls[index][0] or \
                pages_footers[index] == LinsaUa.footers_menu_urls[index][1] \
             , f'ERROR! Bad transaction for {pages_footers[index]}'


