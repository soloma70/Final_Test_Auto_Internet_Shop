from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import StartLocators, StartLocatorsMobile, RegLocators


class StartPage(BasePage):
    """Класс определяет параметры стартовой страницы сайта (десктопная версия), свойства и функции поиска элеменов
    на странице """

    def __init__(self, driver, timeout=3):
        super().__init__(driver, timeout)
        self.url = LinsaUa.start_url
        driver.get(self.url)

        # Banners elements
        self.sales_banners = driver.find_elements(*StartLocators.sales_banners)
        self.all_sales_prods = driver.find_element(*StartLocators.all_sales_prods)


    def logo_img(self) -> WebElement:
        return self.driver.find_element(*StartLocators.logo_img)

    def logo_img_mob(self) -> WebElement:
        return self.driver.find_element(*StartLocatorsMobile.logo_img_mobile)

    def main_menu_click(self, index: int):
        self.driver.find_elements(*StartLocators.main_menu_points)[index].click()
        sleep(1)

    def amount_banner(self) -> int:
        return len(self.driver.find_elements(*StartLocators.banner_points))

    def banner_click(self, index: int) -> [int, int]:
        amount_banner = int((self.driver.find_elements(*StartLocators.banner_points)[index].text.split())[0].strip())
        self.driver.find_elements(*StartLocators.banner_points)[index].click()
        sleep(1)
        amount_page = int(self.driver.find_element(*StartLocators.amount_product).text.strip())
        return amount_banner, amount_page

    def all_sales_prods_click(self):
        self.all_sales_prods.click()

    def love_brands_sunglasses(self) -> [WebElement, WebElement]:
        self.driver.find_element(*StartLocators.love_brands_sunglasses).click()
        sleep(2)
        vogue = self.driver.find_element(*StartLocators.img_vogue)
        rayban = self.driver.find_element(*StartLocators.img_rayban)
        return vogue, rayban

    def love_brands_lenses(self) -> [WebElement, WebElement]:
        self.driver.find_element(*StartLocators.love_brands_lenses).click()
        sleep(2)
        avisor = self.driver.find_element(*StartLocators.img_avizor)
        menicon = self.driver.find_element(*StartLocators.img_menicon)
        return avisor, menicon

    def love_brands_accessories(self) -> [WebElement, WebElement]:
        self.driver.find_element(*StartLocators.love_brands_accessories).click()
        sleep(2)
        okvision = self.driver.find_elements(*StartLocators.img_okvision)
        return okvision[2], okvision[4]

    def reg_btn_click(self) -> WebElement:
        self.driver.find_element(*RegLocators.registr_btn).click()
        return self.driver.find_element(*RegLocators.registr_popup_windows)

    def input_reg_data(self, r_name: str, r_phone: str, r_passw: str):
        name = self.driver.find_element(*RegLocators.registr_popup_name)
        name.clear()
        name.send_keys(r_name)
        phone = self.driver.find_element(*RegLocators.registr_popup_phone)
        phone.clear()
        phone.send_keys(r_phone)
        passw = self.driver.find_element(*RegLocators.registr_popup_passw)
        passw.clear()
        passw.send_keys(r_passw)
        self.driver.find_element(*RegLocators.registr_popup_chec).click()
        super().save_screen_browser('test_registration_start_page')
        self.driver.find_element(*RegLocators.registr_popup_close)

    # Blog elements
    def blog_card_name(self) ->[str, str, str]:
        blog_card = [card for card in StartLocators.blog_cards]
        card_1 = self.driver.find_element(blog_card[0][0], blog_card[0][1]).text
        card_2 = self.driver.find_element(blog_card[1][0], blog_card[1][1]).text
        card_3 = self.driver.find_element(blog_card[2][0], blog_card[2][1]).text
        return card_1, card_2, card_3

    def blog_card_goto(self, index: int) -> str:
        self.driver.find_element(*StartLocators.blog_cards[index]).click()
        blog_title_2 = self.driver.find_element(*StartLocators.blog_title).text
        super().get_url(self.url)
        return blog_title_2

    def more_news_btn(self) -> str:
        self.driver.find_element(*StartLocators.blog_btn).click()
        blog_url = super().get_relative_link()
        super().get_url(self.url)
        return blog_url

    def more_info_click(self):
        self.driver.find_element(*StartLocators.more_info_btn).click()
        sleep(2)
