from selenium.webdriver.common.by import By


class StartLocators:

    # DESKTOP LOCATORS
    # HEADERS LOCATORS
    # Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a[class="top-logo"]>img')
    # Search locators
    search_field = (By.CSS_SELECTOR, 'div[class="input-wrapper"]>input')
    search_result = (By.CSS_SELECTOR, 'div[class="h-holder"]>div[class="amount"]')
    # Callback locators
    callback_btn = (By.CSS_SELECTOR, 'a[href="#"]')
    callback_form_name = (By.CSS_SELECTOR, 'input[name="name"]')
    callback_form_phone = (By.CSS_SELECTOR, 'input[name="phone"]')
    callback_form_submit = (By.CSS_SELECTOR, 'button[class="b24-form-btn"]')
    callback_form_close = (By.CSS_SELECTOR, 'div[class="b24-window-panel b24-window-panel-pos-right"]>button')
    # Login locators
    login_btn = (By.CSS_SELECTOR, 'a[class="enter md-cab-link js-open-auth-popup"]')
    login_name = (By.CSS_SELECTOR, 'input[name="login"]')
    login_pass = (By.CSS_SELECTOR, 'input[name="password"]')
    login_submit = (By.CSS_SELECTOR, 'input[id="auth-submit"]')
    login_close = (By.CSS_SELECTOR, 'div[class="close-popup js-close-popup"]>svg')
    # Wishlist locator
    wishlist_btns = (By.CSS_SELECTOR, 'div[class="icons-panel"]>a>svg')
    # Cart locator
    cart_btn = (By.CSS_SELECTOR, 'a[class="cart"]>svg')
    # Lang locators
    lang_btn_active = (By.CSS_SELECTOR, 'div[class="active-lang"]')
    lang_btn_uk = (By.CSS_SELECTOR, 'a[href="https://linza.com.ua/uk/"]')
    lang_btn_ru = (By.CSS_SELECTOR, 'a[href="https://linza.com.ua/"]')
    # RightSide Menu locators
    menu_button = (By.CSS_SELECTOR, 'div[class="menu-button js-open-side-menu"]')
    menu_button_close = (By.CSS_SELECTOR, 'div[class="side-close-menu js-side-close-menu"]>svg')
    menu_points = (By.CSS_SELECTOR, 'ul[class="wrapper-ul"]>li>a')

    # MAIN PAGE LOCATORS
    # Main Menu locator
    main_menu_points = (By.CSS_SELECTOR, 'div[class="main-menu"]>ul>li>a')
    # Banners locators
    banner_points = (By.CSS_SELECTOR, 'div[class="blocks-holder"]>div>div[class="button-holder"]>a')
    amount_product = (By.CSS_SELECTOR, 'div[class="h-holder"]>div[class="amount"]')
    sales_banners = (By.CSS_SELECTOR, 'div[class="main-content"]')
    sales_sunglass = (By.CSS_SELECTOR, 'div[class="product-item sunglasses"]>div[class="main-content"]>a[class="img"]')
    sales_add_cart_sunglass = (By.CSS_SELECTOR, 'button[class="buy-button js-to-basket"]')
    all_sales_prods = (By.CSS_SELECTOR, 'a[class="fat-button orange"]')
    # PopUp cart locators
    move_to_cart_popup = (By.CSS_SELECTOR, 'div[id="product-added-to-cart-popup"]>div>div>div>div>div[class="popup-infop"]>a')
    close_cart_popup = (By.CSS_SELECTOR, 'div[id="product-added-to-cart-popup"]>div>div>div>div>div[class="close-popup js-close-popup"]>svg')
    amount_cart = (By.CSS_SELECTOR, 'div[class="icons-panel"]>a[class="cart"]>span[class="total-in-cart"]')
    # Love brand locators
    love_brands_sunglasses = (By.XPATH, '//*[@id="content-wrapper"]/section[2]/div[1]/div/div[1]')
    love_brands_lenses = (By.XPATH, '//*[@id="content-wrapper"]/section[2]/div[1]/div/div[2]')
    love_brands_accessories = (By.XPATH, '//*[@id="content-wrapper"]/section[2]/div[1]/div/div[3]')
    img_vogue = (By.CSS_SELECTOR, 'img[title="VOGUE"]')
    img_rayban = (By.CSS_SELECTOR, 'img[title="RAY-BAN"]')
    img_avizor = (By.CSS_SELECTOR, 'img[title="AVIZOR ENZYME"]')
    img_menicon = (By.CSS_SELECTOR, 'img[title="Menicon Progent"]')
    img_okvision = (By.CSS_SELECTOR, 'img[title="okvision I CARE"]')
    # PopUp Registration locators
    registr_btn = (By.CSS_SELECTOR, 'a[class="fat-button black js-open-auth-popup"]')
    registr_popup_windows = (By.CSS_SELECTOR, 'div[id="auth-popup"] > div > div > div[class="popup-window"]')
    registr_popup_name = (By.CSS_SELECTOR, 'div[class="input-wrapper green"] > input[name="name"]')
    registr_popup_phone = (By.CSS_SELECTOR, 'div[class="input-wrapper green"] > input[name="phone"]')
    registr_popup_passw = (By.CSS_SELECTOR, 'div[class="input-wrapper green"] > input[name="password"]')
    registr_popup_chec = (By.CSS_SELECTOR, 'label[class="check-label"] > input[type="checkbox"]')
    registr_popup_add = (By.CSS_SELECTOR, 'label[class="submit-popup"] > input[type="submit"]')
    registr_popup_close = (By.CSS_SELECTOR, '#auth-popup > div > div > div > div.top > div > svg')
    # Blogs locators
    blog_card_1 = (By.XPATH, '//*[@id="content-wrapper"]/section[4]/div[2]/a[1]/div[2]/div[1]')
    blog_card_2 = (By.XPATH, '//*[@id="content-wrapper"]/section[4]/div[2]/a[2]/div[2]/div[1]')
    blog_card_3 = (By.XPATH, '//*[@id="content-wrapper"]/section[4]/div[2]/a[3]/div[2]/div[1]')
    blog_btn = (By.CSS_SELECTOR, 'section[class="main-blog"] > div[class="button-holder"] > a')
    blog_title = (By.CSS_SELECTOR, 'div[class="article-top"] > h1')
    # About Us locators
    about_left_btn = (By.CSS_SELECTOR, 'section[class="about-us-main"] > div[class="left"] > div[class="details"] > a')
    about_right_btn = (By.CSS_SELECTOR, 'section[class="about-us-main"] > div[class="right"] > a')

    # FOOTERS LOCATORS
    footers_left_btns = (
                By.CSS_SELECTOR, 'div[class="footer-top"] > div[class="left"] > ul[class="footer-menu"] > li > a')
    footers_right_btns = (
                By.CSS_SELECTOR, 'div[class="footer-top"] > div[class="right"] > ul[class="footer-menu"] > li > a')
    footer_middle_btns = (
        By.CSS_SELECTOR, 'div[class="footer-middle"] > div[class="item"] > a')
    footer_bottom_left_btn = (
        By.CSS_SELECTOR, 'div[class="footer-bottom"] > div[class="left"] > a[class="desk"]')
    footer_bottom_right_btn = (
        By.CSS_SELECTOR, 'div[class="footer-bottom"] > div[class="right"] > a')


    # Mobile version locators
    logo_img_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/a/img')
    search_field_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[3]/div/img')
    wishlist_btn_mobile = (By.XPATH, '//*[@id="total-in-wishlist"]')
    cart_btn_mobile = (By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[3]/a[2]/svg')
    menu_button_mobile = (By.CSS_SELECTOR, '//*div[class="menu-button js-open-menu"]')



