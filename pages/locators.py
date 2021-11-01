from selenium.webdriver.common.by import By


class StartLocators:

    # Descktop version locators
    logo_img = (By.XPATH, '//*[@id="content-wrapper"]/header/div[1]/a')
    search_field = (By.XPATH, '//*[@id="content-wrapper"]/header/div[1]/div[1]/form/div/input')
    search_result = (By.CSS_SELECTOR, 'div[class="h-holder"]>div[class="amount"]')
    callback_btn = (By.XPATH, '//*[@id="content-wrapper"]/header/div[1]/div[2]/div/a[2]')
    login_btn = (By.XPATH, '//*[@id="content-wrapper"]/header/div[2]/div[1]/div[1]/a')
    wishlist_btns = (By.ID, 'total-in-wishlist')
    cart_btn = (By.CLASS_NAME, 'cart')
    lang_btn = (By.XPATH, '//*[@id="content-wrapper"]/header/div[2]/div[1]/div[3]')
    menu_button = (By.XPATH, '//*[@id="content-wrapper"]/header/div[2]/div[2]')

    # Mobile version locators
    logo_img_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/a/img')
    search_field_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[3]/div/img')
    wishlist_btn_mobile = (By.XPATH, '//*[@id="total-in-wishlist"]')
    cart_btn_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[3]/a[2]/svg')
    menu_button_mobile = (By.CSS_SELECTOR, '//*div[class="menu-button js-open-menu"]')


class NewUserLocators:
    NEW_USER_BTN = (By.CSS_SELECTOR, 'a[href="/login"]')