
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocatorsMobile
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class StartPage(BasePage):
    """Класс определяет параметры стартовой страницы сайте, свойства и функции поиска элеменов на странице
    в десктопной и мобильной версиях сайта, а так же некоторые вспомагательные функции """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.start_url
        driver.get(self.url)

        # RightSide Menu elements
        self.menu_points = driver.find_elements(*StartLocatorsMobile.menu_points_main)  # 13
        self.menu_points_hidden = driver.find_elements(*StartLocatorsMobile.menu_points_hidden)  # 7

        # Banners elements
        self.sales_banners = driver.find_elements(*StartLocatorsMobile.sales_banners)

        # Footers elements
        self.footers_left_btns = driver.find_elements(*StartLocatorsMobile.footers_left_btns)
        self.footers_right_btns = driver.find_elements(*StartLocatorsMobile.footers_right_btns)

    def start_img_click(self):
        self.driver.find_element(*StartLocatorsMobile.logo_img_mobile).click()

    def search_field_click_close(self):
        self.driver.find_element(*StartLocatorsMobile.search_field_img).click()
        self.driver.find_element(*StartLocatorsMobile.search_field_close).click()

    def search_field_click_search(self, search_value):
        self.driver.find_element(*StartLocatorsMobile.search_field_img).click()
        search_field = self.driver.find_element(*StartLocatorsMobile.search_field)
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.send_keys(Keys.ENTER)

    def amount_found_result(self) -> int:
        amount = int(self.driver.find_element(*StartLocatorsMobile.search_result).text)
        return amount

    def wishlist_btn_click(self):
        self.driver.find_element(*StartLocatorsMobile.wishlist_btns).click()

    def wait_login_title(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(StartLocatorsMobile.login_title))

    def login_close(self):
        self.driver.find_element(*StartLocatorsMobile.login_close).click()

    def cart_btn_click(self):
        self.driver.find_element(*StartLocatorsMobile.cart_btn).click()

    def lang_btn_active_click(self):
        self.driver.find_element(*StartLocatorsMobile.lang_btn_active).click()

    def lang_btn_click(self):
        self.driver.find_element(*StartLocatorsMobile.lang_btn).click()

    def menu_btn_click(self):
        self.driver.find_element(*StartLocatorsMobile.menu_button).click()

    def menu_autor_click(self):
        self.driver.find_element(*StartLocatorsMobile.menu_enter).click()

    def input_autor_data(self, a_phone: str, a_passw: str):
        phone = self.driver.find_element(*StartLocatorsMobile.login_name)
        phone.clear()
        phone.send_keys(a_phone)
        passw = self.driver.find_element(*StartLocatorsMobile.registr_popup_passw)
        passw.clear()
        passw.send_keys(a_passw)

    def menu_autor_submit(self):
        self.driver.find_element(*StartLocatorsMobile.login_submit).click()

    def wait_download_cabinet(self) -> str:
        name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(StartLocatorsMobile.user_name))
        return f'{name.text.split()[1]} {name.text.split()[0]}'

    def exit_cabinet(self):
        element = self.driver.find_element(*StartLocatorsMobile.exit_cabinet)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    def amount_tab_cabinet_menu(self) -> int:
        return len(self.driver.find_elements(*StartLocatorsMobile.cabinet_menu_mobile))

    def goto_cabinet_menu(self, index: int) -> str:
        element_menu = self.driver.find_elements(*StartLocatorsMobile.cabinet_menu_mobile)[index]
        ActionChains(self.driver).move_to_element(element_menu).perform()
        element_menu.click()
        part_url = self.get_relative_link().split('/')
        menu_url = f'/{part_url[1]}/{part_url[2]}/'
        return menu_url

    def menu_close_click(self):
        self.driver.find_element(*StartLocatorsMobile.menu_button_close).click()

    def menu_points_main_click(self, index: int):
        self.driver.find_elements(*StartLocatorsMobile.menu_points_main)[index].click()

    def menu_points_hidden_click(self, index: int):
        self.driver.find_elements(*StartLocatorsMobile.menu_points_hidden)[index].click()

    def banner_points_click(self, index: int):
        self.driver.find_elements(*StartLocatorsMobile.banner_points)[index].click()

    def amount_products(self) -> int:
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(StartLocatorsMobile.amount_product))
        amount = int(element.text.strip())
        return amount

    def all_sales_prods_click(self):
        self.driver.find_element(*StartLocatorsMobile.all_sales_prods).click()

    def amount_cart_mobile(self) -> int:
        return int(self.driver.find_element(*StartLocatorsMobile.amount_cart).text)

    def sales_banner_first_position(self):
        self.driver.find_elements(*StartLocatorsMobile.sales_banners)[0].click()

    def add_cart_product_def_par(self):
        self.driver.find_element(*StartLocatorsMobile.add_cart_product).click()

    def close_cart_popup(self):
        self.driver.find_element(*StartLocatorsMobile.close_cart_popup).click()

    def goto_love_brands_lenses(self):
        self.driver.find_element(*StartLocatorsMobile.love_brands_lenses).click()
        sleep(1)

    def goto_love_brands_accessories(self):
        self.driver.find_element(*StartLocatorsMobile.love_brands_accessories).click()
        sleep(1)

    def goto_love_brands_sunglasses(self):
        self.driver.find_element(*StartLocatorsMobile.love_brands_sunglasses).click()
        sleep(1)

    def move_to_element_love_blands(self):
        element = self.driver.find_element(*StartLocatorsMobile.love_brands_section)
        ActionChains(self.driver).move_to_element(element).perform()

    def registration_btn(self):
        self.driver.find_element(*StartLocatorsMobile.registr_btn).click()

    def registration_popup_win(self) -> WebElement:
        return self.driver.find_element(*StartLocatorsMobile.registr_popup_windows)

    def input_reg_data_mobile(self, r_name: str, r_phone: str, r_passw: str):
        name = self.driver.find_element(*StartLocatorsMobile.registr_popup_name)
        name.clear()
        name.send_keys(r_name)
        phone = self.driver.find_element(*StartLocatorsMobile.registr_popup_phone)
        phone.clear()
        phone.send_keys(r_phone)
        passw = self.driver.find_element(*StartLocatorsMobile.registr_popup_passw)
        passw.clear()
        passw.send_keys(r_passw)
        self.driver.find_element(*StartLocatorsMobile.registr_popup_chec).click()

    def registration_submit(self):
        self.driver.find_element(*StartLocatorsMobile.registr_popup_submit).click()

    def registration_close(self):
        self.driver.find_element(*StartLocatorsMobile.registr_popup_close).click()

    def blog_card_titles(self) -> list:
        title1 = self.driver.find_element(*StartLocatorsMobile.blog_titles_1).text
        title2 = self.driver.find_element(*StartLocatorsMobile.blog_titles_2).text
        element = self.driver.find_element(*StartLocatorsMobile.blog_titles_3)
        ActionChains(self.driver).move_to_element(element).perform()
        title3 = self.driver.find_element(*StartLocatorsMobile.blog_titles_3).text
        return [title1, title2, title3]

    def goto_blog(self, index: int):
        if index == 1:
            element = self.driver.find_element(*StartLocatorsMobile.blog_titles_1)
            ActionChains(self.driver).move_to_element(element).perform()
            self.driver.find_element(*StartLocatorsMobile.blog_titles_1).click()
        elif index == 2:
            self.driver.find_element(*StartLocatorsMobile.blog_titles_2).click()
        elif index == 3:
            element = self.driver.find_element(*StartLocatorsMobile.blog_titles_3)
            ActionChains(self.driver).move_to_element(element).perform()
            self.driver.find_element(*StartLocatorsMobile.blog_titles_3).click()

    def blog_title(self) -> str:
        return self.driver.find_element(*StartLocatorsMobile.blog_title).text

    def goto_more_news(self):
        self.driver.find_element(*StartLocatorsMobile.blog_btn).click()

    def goto_footer_left(self, index: int):
        self.driver.find_elements(*StartLocatorsMobile.footers_left_btns)[index].click()

    def goto_footer_right(self, index: int):
        self.driver.find_elements(*StartLocatorsMobile.footers_right_btns)[index].click()

    def goto_footer_bottom_left(self):
        self.driver.find_element(*StartLocatorsMobile.footer_bottom_left_btn).click()

    def goto_footer_bottom_right(self):
        self.driver.find_element(*StartLocatorsMobile.footer_bottom_right_btn).click()

    def goto_footer_middle(self, index: int):
        self.driver.find_elements(*StartLocatorsMobile.footer_middle_btns)[index].click()
