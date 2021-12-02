from pages.base_page import BasePage
from pages.url_list import LinsaUa
from pages.locators import CartLocators, CabinetLocators, StartLocators, ProductLocators
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class CabinetPage(BasePage):
    """Класс создает экземпляр страницы Кабинет пользователя (десктопная версия), переменные и методы поиска элеменов
    на странице """

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = LinsaUa.cabinet_url()
        driver.get(self.url)

        self.cabinet = self.driver.find_elements(*CabinetLocators.cabinet)
        self.cabinet_name = self.driver.find_element(*CabinetLocators.cabinet_name)

    def goto_menu(self, index: int):
        self.driver.find_elements(*CabinetLocators.cabinet)[index].click()

    def exit_cabinet(self):
        self.driver.find_element(*CabinetLocators.exit_cabinet).click()

    def search_item_in_list(self, test_item: str, item_list: list) -> int:
        i = 0
        while test_item != item_list[i]:
            i += 1
        return i

    def add_new_adress(self, city: str, street: str, house: str, flat: str):
        self.driver.find_element(*CabinetLocators.my_add_new_delivery).click()
        self.driver.find_element(*CabinetLocators.my_city).click()
        #
        city_list = self.driver.find_elements(*CabinetLocators.city_list)
        city_name = [name_city.text.strip() for name_city in city_list]
        index = self.search_item_in_list(city, city_name)
        city_list[index].click()
        part_street = street.split()[1]
        self.driver.find_element(*CabinetLocators.my_street).send_keys(part_street)
        # WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(CartLocators.street_list))
        sleep(1)
        #
        street_list = self.driver.find_elements(*CabinetLocators.street_list)
        srteet_l = [street.text for street in street_list]
        index = self.search_item_in_list(street, srteet_l)
        street_list[index].click()
        self.driver.find_element(*CabinetLocators.my_house).send_keys(house)
        self.driver.find_element(*CabinetLocators.my_flat).send_keys(flat)
        self.driver.find_element(*CabinetLocators.my_add_addr).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(CabinetLocators.my_add_sucsess))
        self.driver.find_element(*CabinetLocators.my_close_sucsess).click()

    def inst_default_address(self):
        self.driver.find_element(*CabinetLocators.my_def_addr).click()

    def list_last_add_adress(self) -> list:
        city = self.driver.find_elements(*CabinetLocators.address_cities)[-1].text.strip()
        full_adress = self.driver.find_elements(*CabinetLocators.address_streets)[-1].text.strip().split()
        street = f'{full_adress[0]} {full_adress[1]}'
        house = full_adress[2]
        flat = full_adress[-1]
        return [city, street, house, flat]

    def delete_adress(self, index: int):
        self.driver.find_elements(*CabinetLocators.delete_my_address)[index].click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(CabinetLocators.my_add_sucsess))
        self.driver.find_element(*CabinetLocators.my_close_sucsess).click()

    def add_email(self, email: str):
        field_email = self.driver.find_elements(*CabinetLocators.my_data)[3]
        field_email.clear()
        field_email.send_keys(email)

    def add_birthday(self, birthday: str):
        field_birthday = self.driver.find_elements(*CabinetLocators.my_data)[4]
        field_birthday.clear()
        field_birthday.send_keys(birthday)

    def change_default_lang(self, lg='uk'):
        if lg == 'uk':
            self.driver.find_element(*CabinetLocators.my_lang_uk).click()
        elif lg == 'ru':
            self.driver.find_element(*CabinetLocators.my_lang_ru).click()

    def save_personal_data(self):
        self.driver.find_element(*CabinetLocators.my_saved).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(CabinetLocators.my_add_sucsess))
        self.driver.find_element(*CabinetLocators.my_close_sucsess).click()

    def list_personal_data(self) -> list:
        list_elements = self.driver.find_elements(*CabinetLocators.my_data)
        list_data = [list_element.get_attribute('value') for list_element in list_elements]
        return list_data

    def clear_email_birthday_lang(self):
        self.driver.find_elements(*CabinetLocators.my_data)[3].clear()
        self.driver.find_elements(*CabinetLocators.my_data)[4].clear()
        self.change_default_lang('ru')
        self.driver.find_element(*CabinetLocators.my_saved).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(CabinetLocators.my_add_sucsess))
        self.driver.find_element(*CabinetLocators.my_close_sucsess).click()

    def cancel_personal_data(self):
        self.driver.find_element(*CabinetLocators.my_cancel).click()

    def add_new_wishlist(self, name_wishlist: str) -> str:
        self.driver.find_element(*CabinetLocators.add_wishlist).click()
        self.driver.find_element(*CabinetLocators.input_name_wishlist).send_keys(name_wishlist)
        self.driver.find_element(*CabinetLocators.input_confirm).click()
        title_success = self.driver.find_element(*CabinetLocators.title_success).text
        self.driver.find_element(*CabinetLocators.close_success).click()
        return title_success

    def choise_point_list(self, name_test: str, elem_list: list) -> int:
        i = 0
        while name_test != elem_list[i]:
            i += 1
        return i

    def goto_wishlist(self, name_wishlist: str):
        elem_wishlist = self.driver.find_elements(*CabinetLocators.lists_wishlist)
        list_wishlist = [elem_wishlist[i].text.rsplit(' ', 1)[0] for i in range(len(elem_wishlist))]
        index = self.choise_point_list(name_wishlist, list_wishlist)
        elem_wishlist[index].click()

    def goto_start_page(self):
        self.driver.find_element(*CabinetLocators.goto_start_page).click()

    def goto_lens_page(self):
        self.driver.find_elements(*StartLocators.main_menu_points)[1].click()

    def add_random_prod_wishlist(self, name_wishlist: str):
        index = self.rand_prod_card(self.amount_on_page())
        self.driver.find_elements(*ProductLocators.card_prod_wishlist)[index].click()
        self.driver.find_element(*CabinetLocators.choise_name_wishlist).click()
        wishlists = self.driver.find_elements(*CabinetLocators.wishlists)
        list_wishlist = [wishlist.text for wishlist in wishlists]
        i = self.choise_point_list(name_wishlist, list_wishlist)
        wishlists[i].click()
        self.driver.find_element(*CabinetLocators.add_in_wishlist).click()
        title_success = self.driver.find_element(*CabinetLocators.title_success).text
        self.driver.find_element(*CabinetLocators.close_success).click()
        return title_success

    def goto_wishlist_header(self):
        self.driver.find_element(*StartLocators.wishlist_btns).click()

    def delete_open_wishlist(self) -> str:
        self.driver.find_element(*CabinetLocators.del_withlist).click()
        self.driver.find_element(*CabinetLocators.del_yes).click()
        title_success = self.driver.find_element(*CabinetLocators.title_success).text
        self.driver.find_element(*CabinetLocators.close_success).click()
        return title_success
