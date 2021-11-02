from selenium.webdriver.common.by import By


class StartLocators:

    # Descktop version locators
    logo_img = (By.CSS_SELECTOR, 'a[class="top-logo"]>img')
    search_field = (By.CSS_SELECTOR, 'div[class="input-wrapper"]>input')
    search_result = (By.CSS_SELECTOR, 'div[class="h-holder"]>div[class="amount"]')
    callback_btn = (By.CSS_SELECTOR, 'a[href="#"]')
    callback_form_name = (By.CSS_SELECTOR, 'input[name="name"]')
    callback_form_phone = (By.CSS_SELECTOR, 'input[name="phone"]')
    callback_form_submit = (By.CSS_SELECTOR, 'button[class="b24-form-btn"]')
    callback_form_close = (By.CSS_SELECTOR, 'div[class="b24-window-panel b24-window-panel-pos-right"]>button')
    login_btn = (By.CSS_SELECTOR, 'a[class="enter md-cab-link js-open-auth-popup"]')
    login_name = (By.CSS_SELECTOR, 'input[name="login"]')
    login_pass = (By.CSS_SELECTOR, 'input[name="password"]')
    login_submit = (By.CSS_SELECTOR, 'input[id="auth-submit"]')
    login_close = (By.CSS_SELECTOR, 'div[class="close-popup js-close-popup"]>svg')
    wishlist_btns = (By.CSS_SELECTOR, 'div[class="icons-panel"]>a>svg')
    cart_btn = (By.CSS_SELECTOR, 'a[class="cart"]>svg')
    lang_btn_active = (By.CSS_SELECTOR, 'div[class="active-lang"]')
    lang_btn_uk = (By.CSS_SELECTOR, 'a[href="https://linza.com.ua/uk/"]')
    lang_btn_ru = (By.CSS_SELECTOR, 'a[href="https://linza.com.ua/"]')
    menu_button = (By.CSS_SELECTOR, 'div[class="menu-button js-open-side-menu"]')
    menu_button_close = (By.CSS_SELECTOR, 'div[class="side-close-menu js-side-close-menu"]>svg')
    menu_points = (By.CSS_SELECTOR, 'ul[class="wrapper-ul"]>li>a')
    main_menu_points = (By.CSS_SELECTOR, 'div[class="main-menu"]>ul>li>a')
    banner_points = (By.CSS_SELECTOR, 'div[class="blocks-holder"]>div>div[class="button-holder"]>a')
    amount_product = (By.CSS_SELECTOR, 'div[class="h-holder"]>div[class="amount"]')

    sales_banners = (By.CSS_SELECTOR, 'div[class="main-content"]')
    sales_add_cart_sunglass = (By.CSS_SELECTOR, 'button[class="buy-button js-to-basket"]')
    all_sales_prods = (By.CSS_SELECTOR, 'a[class="fat-button orange"]')

    amount_cart = (By.CSS_SELECTOR, 'div[class="icons-panel"]>a[class="cart"]>span[class="total-in-cart"]')


    # Mobile version locators
    logo_img_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/a/img')
    search_field_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[3]/div/img')
    wishlist_btn_mobile = (By.XPATH, '//*[@id="total-in-wishlist"]')
    cart_btn_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[3]/a[2]/svg')
    menu_button_mobile = (By.CSS_SELECTOR, '//*div[class="menu-button js-open-menu"]')


class NewUserLocators:
    NEW_USER_BTN = (By.CSS_SELECTOR, 'a[href="/login"]')