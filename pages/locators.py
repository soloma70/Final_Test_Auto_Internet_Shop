from selenium.webdriver.common.by import By


class StartLocators:
    # DESKTOP LOCATORS

    # HEADERS LOCATORS
    # Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a.top-logo > img')
    # Search locators
    search_field = (By.CSS_SELECTOR, 'div.input-wrapper > input')
    search_result = (By.CSS_SELECTOR, 'div.h-holder > div.amount')

    # Callback locators
    callback_btn = (By.CSS_SELECTOR, 'a[href="#"]')
    callback_form_name = (By.CSS_SELECTOR, 'input[name="name"]')
    callback_form_phone = (By.CSS_SELECTOR, 'input[name="phone"]')
    callback_form_submit = (By.CSS_SELECTOR, 'form > div.b24-form-btn-container > div > button')
    callback_form_close = (By.CSS_SELECTOR, 'div.b24-window-panel.b24-window-panel-pos-right > button')

    # Wishlist locator
    wishlist_btns = (By.CSS_SELECTOR, 'div.header-right > div.info-panel > div.icons-panel > a.favourites > svg')

    # Cart locator
    cart_btn = (By.CSS_SELECTOR, 'a.cart > svg')

    # Lang locators
    lang_btn_active = (By.CSS_SELECTOR, 'div.active-lang')
    lang_btn_uk = (By.CSS_SELECTOR, 'a[href="https://linza.com.ua/uk/"]')
    lang_btn_ru = (By.CSS_SELECTOR, 'a[href="https://linza.com.ua/"]')

    # RightSide Menu locators
    menu_button = (By.CSS_SELECTOR, 'div.menu-button.js-open-side-menu')
    menu_button_close = (By.CSS_SELECTOR, 'div.side-close-menu.js-side-close-menu > svg')
    menu_points = (By.CSS_SELECTOR, 'ul.wrapper-ul > li > a')

    # MAIN PAGE LOCATORS
    # Main Menu locator
    main_menu_points = (By.CSS_SELECTOR, 'div.main-menu > ul > li > a')

    # Banners locators
    banner_points = (By.CSS_SELECTOR, 'div.blocks-holder > div > div.button-holder > a')
    amount_product = (By.CSS_SELECTOR, 'div.h-holder > div.amount')
    sales_banners = (By.CSS_SELECTOR, 'div.main-content')
    sales_sunglass = (By.CSS_SELECTOR, 'div.product-item.sunglasses > div.main-content > a.img')
    sales_add_cart_sunglass = (By.CSS_SELECTOR, 'button.buy-button.js-to-basket')
    all_sales_prods = (By.CSS_SELECTOR, 'a.fat-button.orange')

    # PopUp cart locators
    move_to_cart_popup = (
        By.CSS_SELECTOR, '#product-added-to-cart-popup > div > div > div > div > div.popup-infop > a')
    close_cart_popup = (
        By.CSS_SELECTOR, '#product-added-to-cart-popup > div > div > div > div > div.close-popup.js-close-popup > svg')
    amount_cart = (By.CSS_SELECTOR, 'div.icons-panel > a.cart > span.total-in-cart')

    # Love brand locators
    love_brands_sunglasses = (By.XPATH, '//*[@id="content-wrapper"]/section[2]/div[1]/div/div[1]')
    love_brands_lenses = (By.XPATH, '//*[@id="content-wrapper"]/section[2]/div[1]/div/div[2]')
    love_brands_accessories = (By.XPATH, '//*[@id="content-wrapper"]/section[2]/div[1]/div/div[3]')
    img_vogue = (By.CSS_SELECTOR, 'img[title="VOGUE"]')
    img_rayban = (By.CSS_SELECTOR, 'img[title="RAY-BAN"]')
    img_avizor = (By.CSS_SELECTOR, 'img[title="AVIZOR ENZYME"]')
    img_menicon = (By.CSS_SELECTOR, 'img[title="Menicon Progent"]')
    img_okvision = (By.CSS_SELECTOR, 'img[title="okvision I CARE"]')

    # Blogs locators
    blog_cards = [
        (By.CSS_SELECTOR,
         '#content-wrapper > section.main-blog > div.blogs-items-holder > a.blog-item.blue > div.titles > div.title'),
        (By.CSS_SELECTOR,
         '#content-wrapper > section.main-blog > div.blogs-items-holder > a.blog-item.orange > div.titles > div.title'),
        (By.CSS_SELECTOR,
         '#content-wrapper > section.main-blog > div.blogs-items-holder > a.blog-item.yellow > div.titles > div.title')
    ]
    blog_btn = (By.CSS_SELECTOR, 'section.main-blog > div.button-holder > a')
    blog_title = (By.CSS_SELECTOR, 'div.article-top > h1')

    # More Info locators
    more_info_btn = (By.CSS_SELECTOR, 'i.more')

    # FOOTERS LOCATORS
    footers_left_btns = (By.CSS_SELECTOR, 'div.footer-top > div.left > ul.footer-menu > li > a')
    footers_right_btns = (By.CSS_SELECTOR, 'div.footer-top > div.right > ul.footer-menu > li > a')
    footer_middle_btns = (By.CSS_SELECTOR, 'div.footer-middle > div.item > a')
    footer_bottom_left_btn = (By.CSS_SELECTOR, 'div.footer-bottom > div.left > a.desk')
    footer_bottom_right_btn = (By.CSS_SELECTOR, 'div.footer-bottom > div.right > a')
    # Footer More info
    more_inf = (By.CSS_SELECTOR, 'div.footer_seotext > i')


class RegLocators:
    # Login locators
    login_btn = (By.CSS_SELECTOR, '#content-wrapper > header > div.header-right > div.info-panel > div.cab-panel > a')
    #
    win_popup_enter = (By.CSS_SELECTOR, '#auth-component > div > div > div.socials-enter > a')
    auth_facebook = (By.CSS_SELECTOR, '#auth-component > div > div > div.socials-enter > a')
    login_name = (By.CSS_SELECTOR, 'input[name="login"]')
    login_pass = (By.CSS_SELECTOR, 'input[name="password"]')
    login_submit = (By.ID, 'auth-submit')
    login_answer = (By.CSS_SELECTOR, 'div.auth-inputs > div.input-block.error > div.error-block')
    login_close = (By.CSS_SELECTOR, 'div.close-popup.js-close-popup > svg')
    forgot_passw = (By.CSS_SELECTOR, '#auth-component > div > div > form > div.forgot-holder > a')
    #
    reg_link = (By.CSS_SELECTOR, '#auth-component > div > div > div.links-panel > a')
    reg_title = (By.CSS_SELECTOR, '#auth-component > div > div > div.links-panel > span')
    reg_name = (By.CSS_SELECTOR, 'div.auth-inputs > div > div > input[name="name"]')
    reg_phone = (By.CSS_SELECTOR, 'div.auth-inputs > div > div > input[name="phone"]')
    reg_passw = (By.CSS_SELECTOR, 'div.auth-inputs > div > div > input[name="password"]')
    reg_pers_data = (By.CSS_SELECTOR, 'form > div > div.checkbox-block > label > input[type=checkbox]')
    reg_submit = (By.CSS_SELECTOR, '#auth-component > div > div > form > label > input[type=submit]')
    reg_sms_title = (By.CSS_SELECTOR, '#auth-component > div > div > div.popup-title')
    reg_sms = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[type=text]')
    reg_sms_submit = (By.ID, 'auth-submit')
    reg_non_sms = (By.CSS_SELECTOR, '#auth-component > div > div > div.help-panel > a')
    reg_answer_sms = (By.CSS_SELECTOR, '#auth-component > div > div > form > div > div > div.error-block')
    reg_sms_close = (By.CSS_SELECTOR, '#auth-popup > div > div > div > div.top > div > svg')
    start_shop_btn = (By.CSS_SELECTOR, '#auth-component > div > div > a')

    #
    # PopUp Registration locators
    registr_btn = (By.CSS_SELECTOR, 'a.fat-button.black.js-open-auth-popup')
    registr_popup_windows = (By.CSS_SELECTOR, '#auth-popup > div > div > div.popup-window')
    registr_popup_name = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="name"]')
    registr_popup_phone = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="phone"]')
    registr_popup_passw = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="password"]')
    registr_popup_chec = (By.CSS_SELECTOR, 'label.check-label > input[type="checkbox"]')
    registr_popup_add = (By.CSS_SELECTOR, 'label.submit-popup > input[type="submit"]')
    registr_popup_close = (By.CSS_SELECTOR, '#auth-popup > div > div > div > div.top > div > svg')
    reg_nonvalid_answer = (By.CSS_SELECTOR, 'div.auth-inputs > div.input-block.error > div.error-block')


class StartLocatorsMobile:
    # MOBILE LOCATORS

    # HEADERS LOCATORS
    # Start Image locator
    logo_img_mobile = (By.CSS_SELECTOR, 'div.left-mobile-header > a > img')

    # Search locators
    search_field_img = (By.CSS_SELECTOR, 'div.right-mobile-header > div > img')
    search_field = (By.CSS_SELECTOR, 'div.search-panel-mobile.active > form > input')
    search_field_close = (By.CSS_SELECTOR, 'div.search-panel-mobile.active > form > input')
    search_result = (By.CSS_SELECTOR, 'div.h-holder > div.amount')

    # Wishlist locator
    wishlist_btns = (By.CSS_SELECTOR, 'div.right-mobile-header > a > span')

    # Login locators
    login_name = (By.CSS_SELECTOR, 'input[name="login"]')
    login_pass = (By.CSS_SELECTOR, 'input[name="password"]')
    login_title = (By.CSS_SELECTOR, 'div.links-panel > span')
    login_submit = (By.ID, 'auth-submit')
    login_close = (By.CSS_SELECTOR, '#auth-popup > div > div > div > div.top > div > svg')

    # Cart locator
    cart_btn = (By.CSS_SELECTOR, 'div.right-mobile-header > a.cart > span')

    # RightSide Menu locators
    menu_button = (By.CSS_SELECTOR, 'div.left-mobile-header > div.menu-button.js-open-menu')
    menu_enter = (By.CSS_SELECTOR, 'div.main-menu > div.controls > a')
    menu_button_close = (By.CSS_SELECTOR, 'div.mobile-close-menu.js-mobile-close-menu > svg')
    lang_btn_active = (By.CSS_SELECTOR, 'div.controls > div > div')
    lang_btn = (By.CSS_SELECTOR, 'div.controls > div > ul > li > a')
    menu_points_main = (By.CSS_SELECTOR, '#content-wrapper > div.main-menu > ul > li > a')
    menu_points_hidden = (By.CSS_SELECTOR, '#content-wrapper > div.main-menu > ul.desktop-hidden > li > a')

    # Cabinet, element in DOM exit_cabinet don't working
    user_name = (By.CSS_SELECTOR, 'div.cards-wrapper > div > div.card-name')
    user_data = (By.CSS_SELECTOR, 'div.cards-wrapper > div > div.info-holder > div > div.value')
    exit_cabinet = (By.CSS_SELECTOR, '#cabinet-panel > ul > li > a.logout.js-logout')
    cabinet_menu_mobile = (By.CSS_SELECTOR, 'section.cabinet-section > aside > ul > li > a')

    # MAIN PAGE LOCATORS
    # Banners locators
    banner_points = (By.CSS_SELECTOR, 'div.blocks-holder > div > a')
    amount_product = (By.CSS_SELECTOR, 'div.h-holder > div.amount')
    sales_banners = (By.CSS_SELECTOR, 'div.main-content')
    all_sales_prods = (By.CSS_SELECTOR, 'a.fat-button.orange')

    # Add cart locators
    select_sunglass = (By.CSS_SELECTOR, 'div.product-item.sunglasses > div.main-content > a.img > img')
    add_cart_product = (By.ID, 'md-to-basket')
    close_cart_popup = (By.CSS_SELECTOR, '#product-added-to-cart-popup > div > div > div > div.top > div > svg')
    amount_cart = (By.CSS_SELECTOR, 'div.right-mobile-header > a.cart > span.total-in-cart')

    # Love brand locators
    love_brands_section = (By.CSS_SELECTOR, '#content-wrapper > section.favourite-brands')
    love_brands_sunglasses = (By.CSS_SELECTOR, 'div[data-id="sunglasses-brand"]')
    love_brands_lenses = (By.CSS_SELECTOR, 'div[data-id="lenses-brand"]')
    love_brands_accessories = (By.CSS_SELECTOR, 'div[data-id="accessories-brand"]')

    # PopUp Registration locators
    registr_btn = (By.CSS_SELECTOR, 'a.fat-button.black.js-open-auth-popup')
    registr_popup_windows = (By.CSS_SELECTOR, '#auth-popup > div > div > div.popup-window')
    registr_popup_name = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="name"]')
    registr_popup_phone = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="phone"]')
    registr_popup_passw = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="password"]')
    registr_popup_chec = (By.CSS_SELECTOR, 'label.check-label > input[type="checkbox"]')
    registr_popup_submit = (By.CSS_SELECTOR, 'label.submit-popup > input[type="submit"]')
    registr_popup_close = (By.CSS_SELECTOR, '#auth-popup > div > div > div > div.top > div > svg')

    # Blogs locators
    blog_section = (By.CSS_SELECTOR, '#content-wrapper > section.main-blog')
    blog_click_1 = (By.CSS_SELECTOR, 'div.blogs-items-holder > a.blog-item.blue')
    blog_click_2 = (By.CSS_SELECTOR, 'div.blogs-items-holder > a.blog-item.orange')
    blog_click_3 = (By.CSS_SELECTOR, 'div.blogs-items-holder > a.blog-item.yellow')
    blog_titles_1 = (By.CSS_SELECTOR, 'a.blog-item.blue > div.titles > div.title')
    blog_titles_2 = (By.CSS_SELECTOR, 'a.blog-item.orange > div.titles > div.title')
    blog_titles_3 = (By.CSS_SELECTOR, 'a.blog-item.yellow > div.titles > div.title')

    blog_btn = (By.CSS_SELECTOR, 'section.main-blog > div.button-holder > a')
    blog_title = (By.CSS_SELECTOR, 'div.article-top > h1')

    # FOOTERS LOCATORS
    footers_left_btns = (
        By.CSS_SELECTOR, 'div[class="footer-top"] > div[class="left"] > ul[class="footer-menu"] > li > a')
    footers_right_btns = (
        By.CSS_SELECTOR, 'div[class="footer-top"] > div[class="right"] > ul[class="footer-menu"] > li > a')
    footer_middle_btns = (
        By.CSS_SELECTOR, 'div[class="footer-middle"] > div[class="mobile-icons-footer"] > a')
    footer_bottom_left_btn = (
        By.CSS_SELECTOR, 'div[class="footer-bottom"] > div[class="left"] > a[class="mob"]')
    footer_bottom_right_btn = (
        By.CSS_SELECTOR, 'div[class="footer-bottom"] > div[class="right"] > a')


class CartLocators:
    amount_cart_header = (By.CSS_SELECTOR, 'div.icons-panel > a.cart > span.total-in-cart')
    goto_cart_popup = (By.CSS_SELECTOR, '#product-added-to-cart-popup > div > div > div > a')
    popup_cart_title = (By.CSS_SELECTOR, '#product-added-to-cart-popup > div > div > div > div.popup-title')
    close_popup_cart = (By.CSS_SELECTOR, '#product-added-to-cart-popup > div > div > div > div.top > div > svg')
    #
    amount_cart = (By.ID, 'cart-total-goods')
    sum_cart_top = (By.CSS_SELECTOR, 'div.left > div > div.amount.js-total-cart-price')
    sum_cart_bottom = (By.CSS_SELECTOR, 'div.summary > div.amount.js-total-cart-price')
    clear_cart = (By.CSS_SELECTOR, 'div.double-holder > div.right > a')
    cart_empty = (By.CSS_SELECTOR, 'div.js-empty-cart.not-found')
    #
    in_cart_prod_name = (By.CSS_SELECTOR, 'div.cart-item > div.info > a.ttl')
    in_cart_prod_content = (By.CSS_SELECTOR, 'div.cart-item > div.info > div.dscr')
    in_cart_lens_sph = (By.CSS_SELECTOR, 'div.cart-item > div.info > div.dscr > text:nth-child(2)')
    in_cart_lens_bc = (By.CSS_SELECTOR, 'div.cart-item > div.info > div.dscr > text:nth-child(3)')
    # # 0 - brand, 1 - sex, 2 - temple length, 3 - bridge width, 4 - eyepiece width
    #
    in_cart_volume = (By.CSS_SELECTOR, 'div.cart-block > div > div.info > div.dscr > br:nth-child(1)')
    in_cart_type = (By.CSS_SELECTOR, 'div.cart-block > div > div.info > div.dscr > br:nth-child(3)')
    in_cart_line = (By.CSS_SELECTOR, 'div.cart-block > div > div.info > div.dscr > br:nth-child(5)')
    #
    in_cart_prod_sum = (By.CSS_SELECTOR, 'div.cart-item > div.price.js-cart-item-price')
    in_cart_prod_del = (By.CSS_SELECTOR, 'div.cart-item > div.remove.js-remove-from-cart > svg')
    #
    checkout = (By.CSS_SELECTOR, '#content-wrapper > section > div > div.button-holder > a')
    # Recipient's data
    input_name = (By.CSS_SELECTOR,
                  'div.step.step_1 > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > input[type=text]')
    input_surname = (By.CSS_SELECTOR,
                     'div.step.step_1 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > input[type=text]')
    input_email = (By.CSS_SELECTOR, 'div.step.step_1 > div:nth-child(3) > div.input-wrapper > input[type=email]')
    input_phone = (By.CSS_SELECTOR, 'div.step.step_1 > div:nth-child(4) > div.input-wrapper > input[type=text]')
    next_step_delivery = (By.CSS_SELECTOR, 'div.left > div.button-holder > a')
    # Delivery
    input_city = (
        By.CSS_SELECTOR, 'div.selectize-control.single > div.selectize-input.items.has-options.full.has-items')
    city_list = (By.CSS_SELECTOR, 'div.selectize-dropdown.single > div.selectize-dropdown-content > div.option')
    fast_change_city = (By.CSS_SELECTOR, 'div.step.step_2 > div:nth-child(3) > div > label > input[type=radio]')
    #
    dilivery_cour = (
        By.CSS_SELECTOR, 'div.delivery-radio-wrapper > table > tr:nth-child(2) > td:nth-child(1) > label > span.round')
    input_street = (By.CSS_SELECTOR,
                    'div.input-block.street > div.select-wrapper.department > div > '
                    'div.selectize-input.items.not-full > input')
    street_list = (By.CSS_SELECTOR,
                   'div.input-block.street > div.select-wrapper.department > div > div.selectize-dropdown.single > '
                   'div > div')
    input_house = (By.CSS_SELECTOR, 'div.input-block.house > div.input-wrapper > input')
    input_flat = (By.CSS_SELECTOR, 'div.input-block.flat > div.input-wrapper > input')
    #
    dilivery_np = (
        By.CSS_SELECTOR, 'div.delivery-radio-wrapper > table > tr:nth-child(3) > td:nth-child(1) > label > span.round')

    np_branch = (By.CSS_SELECTOR,
                 'div.select-wrapper.department > div > div.selectize-input.items.has-options.not-full > input['
                 'type=text]')
    branch_list = (By.CSS_SELECTOR, 'div.select-wrapper.department > div > div.selectize-dropdown.single > div > div')
    #
    next_step_pay = (By.CSS_SELECTOR, 'form.ecom_steps > div > div.left > div.button-holder > a')
    # Pay
    pay_rec_order = (
        By.CSS_SELECTOR, 'div.delivery-radio-wrapper > table:nth-child(1) > tr:nth-child(1) > td > label > span.round')
    pay_on_site = (
        By.CSS_SELECTOR, 'div.delivery-radio-wrapper > table:nth-child(1) > tr:nth-child(2) > td > label > span.round')
    comment_order = (By.ID, 'cabinet-message')
    dont_call = (By.CSS_SELECTOR, 'div.delivery-radio-wrapper > table:nth-child(3) > tr > td > label > span.round')
    next_step_benefit = (By.CSS_SELECTOR, 'form.ecom_steps > div > div.left > div.button-holder > a')
    # Benefits
    input_promo = (By.CSS_SELECTOR,
                   'div.double-checkout-block > div.left > div.step.step_4 > div.input-block > div > input[type=text]')
    confirm_promo = (
        By.CSS_SELECTOR, 'div.double-checkout-block > div.left > div.step.step_4 > div.input-block > button')
    wrong_promo = (
        By.CSS_SELECTOR, 'div.double-checkout-block > div.left > div.step.step_4 > div.input-block > div > div > span')
    checkout_btn = (By.CSS_SELECTOR, 'div.double-checkout-block > div.left > div.button-holder > button')


class ProductLocators:
    # Page name & amount
    name = (By.CSS_SELECTOR, 'h1.standard-title')
    amount_prod = (By.CSS_SELECTOR, 'div.h-holder > div.amount')
    # Filter locators
    filters = (By.CSS_SELECTOR, 'div.product-filters-titles.js-filter-toggle-items > div > span')
    # Sort locators
    sort_by = (By.CSS_SELECTOR, 'section.sort_panel > a')  # 4 items
    #
    products = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > a.img')
    products_buy = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.additional > button')
    products_lens_buy = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.additional.lens > a')
    #
    # Prod Card locator
    card_prod_full = (By.CSS_SELECTOR, 'div.main-content')
    card_prod_wishlist = (
        By.CSS_SELECTOR, 'div.products-wrapper > div > div.add-to-favorites.js-add-to-wishlist > svg')
    cards_prod_brand = (
        By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > a.top > span.product-type')
    cards_prod_name = (
        By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > a.top > span.title')
    cards_prod_url = (
        By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > a.top')  # 16 items
    card_prod_vol = (
        By.CSS_SELECTOR,
        'div.products-wrapper > div > div.main-content > div > div > div:nth-child(1) > div > div.amount')  # 16 items
    card_prod_price = (
        By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > div.bottom > div.prices > div.actual')
    card_prod_price_old = (
        By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > div.bottom > div.prices > div.old')
    #
    block_1 = '#content-wrapper > section.products-section > div:nth-child(1)'
    block_2 = '#content-wrapper > section.products-section > div:nth-child(2)'
    price_act = 'div.main-content > div.bottom > div.prices > div.actual'
    price_old = 'div.main-content > div.bottom > div.prices > div.old'
    sale_banner = 'div.main-content > div.bottom > div.prices > div.percent_banner'
    #
    clear_all_filters = (By.CSS_SELECTOR, 'div.clear-all.js-remove-all-filters > div.delete-cross')
    # 0 - brand, 1 - sex, 2 - temple length, 3 - bridge width, 4 - eyepiece width
    card_prod_filters = [
        (By.CSS_SELECTOR,
         'div.products-wrapper > div > div.main-content > a.top > span.product-type'),
        (By.CSS_SELECTOR,
         'div.products-wrapper > div > div.main-content > div > div.glasses-size > div:nth-child(1)'),
        (By.CSS_SELECTOR,
         'div.products-wrapper > div > div.main-content > div > div.glasses-size > div:nth-child(2)'),
        (By.CSS_SELECTOR,
         'div.products-wrapper > div > div.main-content > div > div.glasses-size > div:nth-child(3)'),
        (By.CSS_SELECTOR,
         'div.products-wrapper > div > div.main-content > div > div.glasses-size > div:nth-child(4)')
    ]
    card_prod_not_found = (By.CSS_SELECTOR, 'div.not-found')


class ProductLensLocators:
    # Product card
    name = (By.CSS_SELECTOR, 'div.card-section > div.title-card-holder > h1')

    rating = (By.CSS_SELECTOR, '#content-wrapper > div.card-section > div.card-rating > div > div.rev-amount')
    add_review = (By.CSS_SELECTOR, '#content-wrapper > div.card-section > div.card-rating > div > a')

    main = (By.CSS_SELECTOR, '#tabs-anchors-wrapper > a[data-tab="main"]')
    char = (By.CSS_SELECTOR, '#tabs-anchors-wrapper > a[data-tab="characteristics"]')
    photo = (By.CSS_SELECTOR, '#tabs-anchors-wrapper > a[data-tab="photo"]')
    desc = (By.CSS_SELECTOR, '#tabs-anchors-wrapper > a[data-tab="description"]')
    reviews = (By.CSS_SELECTOR, '#tabs-anchors-wrapper > a[data-tab="reviews"]')

    price = (By.CSS_SELECTOR, '#js-goods-price-value')

    # Same eyes
    same_eyes = (By.CSS_SELECTOR, '#js-different-eyes > div > div.titles-row > div.label > div > a:nth-child(1) > svg')
    dioptr_same = (By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(3) > div > div.selectric > span')
    dioptr_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(3) > div > div.selectric-items > div > ul > li')
    curv_same = (By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(4) > div > div.selectric > div')
    curv_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(4) > div > div.selectric-items > div > ul > li')
    color_same = (By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(5) > div > div.selectric > div')
    color_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(5) > div > div.selectric-items > div > ul > li')
    pack_one_same = (
        By.CSS_SELECTOR, '#lenses-quantity-block-same > div.quantity-label > div > label.goods-round > span.round')
    pack_mul_same = (
        By.CSS_SELECTOR,
        '#lenses-quantity-block-same > div.quantity-label > div > label.goods-round.append > span.round')
    amount_same = (By.CSS_SELECTOR, '#product-quantity-same')
    minus_same = (
        By.CSS_SELECTOR,
        '#lenses-quantity-block-same > div.quan-wrapper-cell > div > div.minus.js-sub-product-quantity')
    plus_same = (
        By.CSS_SELECTOR, '#lenses-quantity-block-same > div.quan-wrapper-cell > div > div.plus.js-add-product-quantity')

    # Different eyes
    # diff_eyes = (By.CSS_SELECTOR, '#js-different-eyes > div > div.titles-row > div.label > div > a.active')
    diff_eyes = (By.CSS_SELECTOR, '#js-same-eyes > div > div.titles-row > div.label > div > a:nth-child(2) > span')

    dioptr_left = (By.CSS_SELECTOR, '#lenses-selects-form-left > div:nth-child(3) > div > div.selectric > span')
    dioptr_left_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-left > div:nth-child(3) > div > div.selectric-items > div > ul > li')
    dioptr_right = (By.CSS_SELECTOR, '#lenses-selects-form-right > div:nth-child(3) > div > div.selectric > span')
    dioptr_right_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-right > div:nth-child(3) > div > div.selectric-items > div > ul > li')
    curv_left = (By.CSS_SELECTOR, '#lenses-selects-form-left > div:nth-child(4) > div > div.selectric > span')
    curv_left_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-left > div:nth-child(4) > div > div.selectric-items > div > ul > li')
    curv_right = (By.CSS_SELECTOR, '#lenses-selects-form-right > div:nth-child(4) > div > div.selectric > span')
    curv_right_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-right > div:nth-child(4) > div > div.selectric-items > div > ul > li')
    color_left = (By.CSS_SELECTOR, '#lenses-selects-form-left > div:nth-child(5) > div > div.selectric > div')
    color_left_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-left > div:nth-child(5) > div > div.selectric-items > div > ul > li')
    color_right = (By.CSS_SELECTOR, '#lenses-selects-form-right > div:nth-child(5) > div > div.selectric > div')
    color_right_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-right > div:nth-child(5) > div > div.selectric-items > div > ul > li')
    pack_one_left = (
        By.CSS_SELECTOR, '#lenses-quantity-block-left > div.quantity-label > div > label.goods-round > span.round')
    pack_one_right = (
        By.CSS_SELECTOR, '#lenses-quantity-block-right > div.quantity-label > div > label.goods-round > span.round')
    pack_mul_left = (
        By.CSS_SELECTOR,
        '#lenses-quantity-block-left > div.quantity-label > div > label.goods-round.append > span.round')
    pack_mul_right = (
        By.CSS_SELECTOR,
        '#lenses-quantity-block-right > div.quantity-label > div > label.goods-round.append > span.round')

    amount_left = (By.CSS_SELECTOR, '#product-quantity-left')
    minus_left = (By.CSS_SELECTOR,
                  '#lenses-quantity-block-left > div.quan-wrapper-cell > div > div.minus.js-sub-product-quantity > span')
    plus_left = (By.CSS_SELECTOR,
                 '#lenses-quantity-block-left > div.quan-wrapper-cell > div > div.plus.js-add-product-quantity > span')

    amount_right = (By.CSS_SELECTOR, '#product-quantity-right')
    minus_right = (By.CSS_SELECTOR,
                   '#lenses-quantity-block-right > div.quan-wrapper-cell > div > div.minus.js-sub-product-quantity > '
                   'span')
    plus_right = (By.CSS_SELECTOR,
                  '#lenses-quantity-block-right > div.quan-wrapper-cell > div > div.plus.js-add-product-quantity > span')

    buy_btn = (By.ID, 'md-to-basket')
    buy_one_click = (By.CSS_SELECTOR, 'a.one-click-buy.js-lenses-quick-order')
    buy_repeat_order = (By.CSS_SELECTOR, 'a.one-click-buy.js-open-auth-popup')

    add_favorite = (By.CSS_SELECTOR, 'div.add-to-favorites.js-add-to-wishlist > svg')  # 5 items

    alternative_name = (By.CSS_SELECTOR, 'div.md-title-goods > span')
    alternative_prods = (
        By.CSS_SELECTOR, 'section.products-section.promos-compact.lenses-alt > div.products-wrapper > div')  # 4 items
    alternative_more = (By.CSS_SELECTOR, 'a.fat-button blue')

    viewed_name = (By.CSS_SELECTOR, 'div.standard-title')
    viewed_prods = (
        By.CSS_SELECTOR, 'section.products-section.promos-compact > div.products-wrapper > div')  # 3 items
    viewed_more = (By.CSS_SELECTOR, 'a.fat-button blue')

    reviews_amount = (By.CSS_SELECTOR, 'div.reviews-title')
    review_add = (By.CSS_SELECTOR, 'a.fat-button.glow-button.blue min_245 js-add-review')
    reviews_block = (By.CSS_SELECTOR, 'div.reviews-block > div.review-item')  # 4 items
    reviews_yet = (By.CSS_SELECTOR, 'div.reviews-block > div.button-holder > a')

    add_cart_sum = (By.ID, 'js-goods-price-value')


class PaginLocators:
    # Pagination locators
    pagination = (By.CSS_SELECTOR, '#content-wrapper > div.pagination > a.page-number ')
    arrow_right = (By.CSS_SELECTOR, 'a.arrow-right-pagination > div')
    arrow_left = (By.CSS_SELECTOR, 'a.arrow-left-pagination > div')


class SalesLocators:
    # DESKTOP LOCATORS

    # HEADERS LOCATORS
    # Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a.top-logo > img')

    # Sales Banners locator
    banner_imgs = (By.CSS_SELECTOR, 'div.sales-banner > div.top > div.img-banner > div')
    banner_btns = (By.CSS_SELECTOR, 'div.sales-banner > div.bottom > div.right > a.typical-button.juicy-green')


class BlogLocators:
    # DESKTOP LOCATORS

    # HEADERS LOCATORS
    # Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a.top-logo > img')
    # Sales Banners locator
    news_tags = (By.CSS_SELECTOR, 'div.news-tags-wrapper > a')  # 8 tegs (href)
    news = (By.CSS_SELECTOR, 'div.news-wrapper > a')  # 9 blocks (href)
    news_name = (By.CSS_SELECTOR, 'h1.article-h1')
    #
    add_favorites = (By.CSS_SELECTOR, 'a.js-add-to-saved.share-links-save > img')
    add_favorite_text = (By.CSS_SELECTOR, 'div.share-links > a > span.add')
    del_favorites = (By.CSS_SELECTOR, 'a.share-links-save.js-delete-from-saved > img')
    del_favorite_text = (By.CSS_SELECTOR, 'div.share-links > a > span.delete')

    # Pagination locators
    pagination = (By.CSS_SELECTOR, '#content-wrapper > div.pagination > a')  # 5 pages + arrow (all 11 pages)
    arrow_right = (By.CSS_SELECTOR, 'a.arrow-right-pagination > div')
    arrow_left = (By.CSS_SELECTOR, 'a.arrow-left-pagination > div')


class LensLocators:
    # DESKTOP LOCATORS
    # brands 7, lines 7, type_lens 5, repl_mode 5, base_curv 7, diameter 6, dioptr 7
    filter_list = [
        (By.CSS_SELECTOR, '#filter-tab-0 > div.filter-slider.slider.js-slide-0.slick-initialized.slick-slider > div > '
                          'div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-1 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
                          'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-2 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div > '
                          'div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-3 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div > '
                          'div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-4 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
                          'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-5 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div > '
                          'div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-6 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
                          'div.slick-slide.slick-current.slick-active > div > div > label > a')
    ]
    # Lens Card locator
    name = (By.CSS_SELECTOR, 'h1.standard-title')
    amount_lens = (By.CSS_SELECTOR, 'div.h-holder > div.amount')
    card_lens_full = (By.CSS_SELECTOR, 'div.main-content')
    card_lens_wishlist = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.add-to-favorites.js-add-to-wishlist > svg')
    cards_lens_brand = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.main-content > a.top > span.product-type')
    cards_lens_name = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.main-content > a.top > span.title')
    cards_lens_url = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.main-content > a.top')  # 16 items
    card_lens_amount = (By.CSS_SELECTOR,
                        'div.products-wrapper > div.product-item.lens > div.main-content > div.bottom > '
                        'div.lenses_sizes > div:nth-child(1) > div > div.amount')
    card_lens_price = (By.CSS_SELECTOR,
                       'div.products-wrapper > div.product-item.lens > div.main-content > div.bottom > '
                       'div.lenses_sizes > div:nth-child(1) > div > div.add-price')

    cards_lens_add_btn = (
        By.CSS_SELECTOR,
        'div.products-wrapper > div.product-item.lens > div.additional.lens > a.buy-button ')  # 16 items

    # 0 - brand, 1 - name (contains product line)
    card_lens_filters = [
        (By.CSS_SELECTOR,
         'div.products-wrapper > div.product-item.lens > div.main-content > a.top > span.product-type'),
        (By.CSS_SELECTOR,
         'div.products-wrapper > div.product-item.lens > div.main-content > a.top > span.title'),
    ]


class FramesLocators:
    # DESKTOP LOCATORS
    # brands 7/6, sex 4, temple_length 7/7/3, bridge_width 7/6, eyepiece_width 7/7/7,
    # frame_shape 7/3, frame_type 2, dioptr 4, collection_year 7/6, polarization 1
    filter_list = [
        (By.CSS_SELECTOR,
         '#filter-tab-1 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-2 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-3 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-4 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-5 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-6 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-7 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-8 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-9 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-10 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > d'
         'iv.slick-slide.slick-current.slick-active > div > div > label > a')
    ]


class SunglassLocators:
    # DESKTOP LOCATORS
    # brands 7/7/7/7/2, sex 4, temple_length 7/7/7/7/2, bridge_width 7/7/7/7/7/3, eyepiece_width 7/7/7/7/7/7/2,
    # frame_shape 7/4, collection_year 7/7/5, frame_color
    filter_list = [
        (By.CSS_SELECTOR,
         '#filter-tab-1 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-2 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-3 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-4 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-5 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a')
    ]


class CareLocators:
    # DESKTOP LOCATORS
    # brands 7/6, volume 7/7/5, type 6
    filter_list = [
        (By.CSS_SELECTOR,
         '#filter-tab-0 > div.filter-slider.slider.js-slide-0.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-1 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > '
         'div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR,
         '#filter-tab-2 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div > div > '
         'div > label > a'),
    ]
    card_prod_filters_care = [
        (By.CSS_SELECTOR,
         'div.products-wrapper > div > div.main-content > a.top > span.product-type'),
        (By.CSS_SELECTOR,
         'div.products-wrapper > div > div.main-content > div > div > div:nth-child(1) > div > div.amount'),
    ]

    card_care_amount = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item > div.main-content > div.bottom')
    loc_price1 = 'div.main-content > div > div > div > div > div.add-price'
    loc_price2 = 'div.main-content > div > div > div.actual'
    loc_begin = '#content-wrapper > section.products-section'

    choice_volume = (By.CSS_SELECTOR,
                     'div.char-card-block.glasses > div > div.select-cell.size > div > div.selectric > span')
    list_volume = (By.CSS_SELECTOR,
                   'div.char-card-block.glasses > div > div.select-cell.size > div > div.selectric-items > div > ul > '
                   'li')

    buy_btn = (By.ID, 'md-to-basket')
    add_cart_sum = (By.CSS_SELECTOR, '#product-prices > div > div.price > span')


class CabinetLocators:
    # /ru/cabinet/ 0 Кабинет 1 Личные данные 2 Список желаний 3 Мои заказы 4 Адреса доставки 5 Сохраненные статьи Выйти
    cabinet = (By.CSS_SELECTOR, '#content-wrapper > section > aside > ul > li > a')
    exit_cabinet = (By.CSS_SELECTOR, '#content-wrapper > section > aside > div > a')
    # Cabinet menu Header
    cabinet_name = (By.CSS_SELECTOR, 'div.toggler.js-open-cabinet-panel')
    cabinet_menu_header = (By.CSS_SELECTOR, '#cabinet-panel > ul > li > a')

    # Кабинет ФИО Тел. Почта Адрес доставки Текущая скидка Редактировать данные Изменить пароль
    fio = (By.CSS_SELECTOR, '#content-wrapper > section > main > div.cards-wrapper > div:nth-child(1) > div.card-name')
    phone = (By.CSS_SELECTOR,
             '#content-wrapper > section > main > div.cards-wrapper > div:nth-child(1) > div.info-holder > '
             'div:nth-child(1) > div.value')
    email = (By.CSS_SELECTOR,
             '#content-wrapper > section > main > div.cards-wrapper > div:nth-child(1) > div.info-holder > '
             'div:nth-child(2) > div.value')
    delivery_adr = (By.CSS_SELECTOR,
                    '#content-wrapper > section > main > div.cards-wrapper > div:nth-child(1) > div.info-holder > '
                    'div.item.w100 > div.value')
    discont = (By.CSS_SELECTOR,
               '#content-wrapper > section > main > div.cards-wrapper > div:nth-child(2) > '
               'div.info-holder.bonuses-holder > div > div.percent')
    edit_data = (By.CSS_SELECTOR,
                 '#content-wrapper > section > main > div.cards-wrapper > div:nth-child(1) > div.card-controls > '
                 'a:nth-child(1) > span')
    change_passw = (By.CSS_SELECTOR,
                    '#content-wrapper > section > main > div.cards-wrapper > div:nth-child(1) > div.card-controls > '
                    'a:nth-child(2) > span')

    # Личные данные
    # Фамилия Имя Телефон емейл День рождения Язык по умолч.укр/рус Сохранить Отмена Изменить пароль Редактировать данные
    my_data = (By.CSS_SELECTOR, 'div.left-column > div > div > div > input')
    last_name = (By.CSS_SELECTOR, 'div.left-column > div:nth-child(1) > div > div > input')
    first_name = (By.CSS_SELECTOR, 'div.left-column > div:nth-child(2) > div > div > input')
    my_phone = (By.CSS_SELECTOR, 'div.left-column > div:nth-child(3) > div > div > input')
    my_email = (By.CSS_SELECTOR, 'div.left-column > div:nth-child(4) > div > div > input')
    my_birthday = (By.CSS_SELECTOR, 'div.left-column > div:nth-child(5) > div > div > input')
    my_lang_uk = (By.ID, 'lang_uk')
    my_lang_ru = (By.ID, 'lang_ru')
    my_saved = (By.CSS_SELECTOR, '#content-wrapper > section > main > div.cabinet-control-buttons > label')
    my_cancel = (By.CSS_SELECTOR, '#content-wrapper > section > main > div.cabinet-control-buttons > a')
    my_change_passw = (
        By.CSS_SELECTOR, '#content-wrapper > section > main > div.edit-top-panel > div.ctrl-panel > a:nth-child(1)')
    my_edit_data = (
        By.CSS_SELECTOR, '#content-wrapper > section > main > div.edit-top-panel > div.ctrl-panel > a:nth-child(2)')

    # Список желаний
    # Список Добавить список Название Добавить Закрыть Удалить список Вернуться на главную
    my_wishlist = (By.CSS_SELECTOR, '#wishlist-wrapper > div.products-control-panel > div.info > a.item.active')
    my_add_wishlist = (
        By.CSS_SELECTOR, '#wishlist-wrapper > div.products-control-panel > div.info > a.item.js-create-wishlist')
    my_name_wishlist = (
        By.CSS_SELECTOR, '#add-wishlist-popup > div > div > div > form > div > div > div > input[type=text]')
    my_add_name_wishlist = (By.CSS_SELECTOR, '#add-wishlist-popup > div > div > div > form > button')
    my_close_name_wishlist = (
        By.CSS_SELECTOR, '#add-wishlist-popup > div > div > div > div > div.close-popup.js-close-popup > svg')
    my_delete_wishlist = (
        By.CSS_SELECTOR, '#wishlist-wrapper > div.products-information > div.delete-all-wishlist.js-delete-wishlist')
    my_goto_start_page = (By.CSS_SELECTOR, '#content-wrapper > section > main > div.double-no-goods > div.left > a')

    # Адреса доставки
    # Добавить новый адрес Город Список городов Киев Днепр Харьков Улица Список улиц Дом Квартира Добавить Закрыть
    # Успешно добавлен Закрыть "Успешно" По умолчанию
    my_add_new_delivery = (By.CSS_SELECTOR, 'div.add-address.js-add-address-btn > svg:nth-child(1)')
    my_city = (By.CSS_SELECTOR,
               '#add-address-popup > div > div > div > form > div:nth-child(2) > div:nth-child(1) > div > div > '
               'div.selectize-input.items.full.has-options.has-items > div')
    city_list = (By.CSS_SELECTOR,
                 '#add-address-popup > div > div > div > form > div:nth-child(2) > div:nth-child(1) > div > div > '
                 'div.selectize-dropdown.single.addresses-city > div > div')
    city_kiev = (By.CSS_SELECTOR,
                 '#add-address-popup > div > div > div > form > div:nth-child(2) > div:nth-child(2) > div > '
                 'label:nth-child(1) > input')
    city_dnepr = (By.CSS_SELECTOR,
                  '#add-address-popup > div > div > div > form > div:nth-child(2) > div:nth-child(2) > div > '
                  'label:nth-child(2) > input')
    city_kharkiv = (By.CSS_SELECTOR,
                    '#add-address-popup > div > div > div > form > div:nth-child(2) > div:nth-child(2) > div > '
                    'label:nth-child(3) > input')
    my_street = (By.CSS_SELECTOR,
                 '#add-address-popup > div > div > div > form > div:nth-child(3) > div.input-block > div > div > '
                 'div.selectize-input.items.not-full > input[type=text]')
    street_list = (By.CSS_SELECTOR,
                   '#add-address-popup > div > div > div > form > div:nth-child(3) > div.input-block > div > div > '
                   'div.selectize-dropdown.single.addresses-street > div > div')
    my_house = (By.CSS_SELECTOR,
                '#add-address-popup > div > div > div > form > div:nth-child(3) > div.double-inputs-address > '
                'div:nth-child(1) > input[type=text]')
    my_flat = (By.CSS_SELECTOR,
               '#add-address-popup > div > div > div > form > div:nth-child(3) > div.double-inputs-address > '
               'div:nth-child(2) > input[type=text]')
    my_add_addr = (By.CSS_SELECTOR, '#add-address-popup > div > div > div > form > button')
    my_close_addr = (
        By.CSS_SELECTOR, '#add-address-popup > div > div > div > div > div.close-popup.js-close-popup > svg')
    # Успешно
    title_success = (By.CSS_SELECTOR, '#success-notification-popup > div > div > div > div.popup-title')
    close_success = (By.CSS_SELECTOR, '#success-notification-popup > div > div > div > div.top > div > svg')
    #
    my_def_addr = (By.CSS_SELECTOR, 'label.address-round > span.round')
    address_cities = (
        By.CSS_SELECTOR, 'div.addresses-section > div > div > div.main-info > div.address-details > div.city')
    address_streets = (
        By.CSS_SELECTOR, 'div.addresses-section > div > div > div.main-info > div.address-details > div.street')

    edit_my_adress = (By.CSS_SELECTOR, 'div.edit.js-edit-address-btn > svg')
    delete_my_address = (By.CSS_SELECTOR, 'div.delete.js-delete-address-btn > svg')

    # Список желаний
    # Добавить список желаний
    add_wishlist = (
        By.CSS_SELECTOR, '#wishlist-wrapper > div.products-control-panel > div.info > a.item.js-create-wishlist')
    list_wishlist = (By.CSS_SELECTOR, '#wishlist-wrapper > div.products-control-panel > div.info > a')
    # Название
    input_name_wishlist = (
        By.CSS_SELECTOR, '#add-wishlist-popup > div > div > div > form > div > div > div > input[type=text]')
    # Добавить
    input_confirm = (By.CSS_SELECTOR, '#add-wishlist-popup > div > div > div > form > button')
    #
    wishlist_frames = (By.CSS_SELECTOR, 'div.product-item.frames > div.main-content > a.img > img')
    wishlist_frames_price = (
        By.CSS_SELECTOR, 'div.product-item.frames > div.main-content > div > div.prices > div.actual')
    wishlist_buy_frames = (By.CSS_SELECTOR, 'div.product-item.frames > div.additional > button')
    wishlist_sg = (By.CSS_SELECTOR, 'div.product-item.sunglasses > div.main-content > a.img > img')
    wishlist_sg_price = (
        By.CSS_SELECTOR, 'div.product-item.sunglasses > div.main-content > div > div.prices > div.actual')
    wishlist_buy_sg = (By.CSS_SELECTOR, 'div.product-item.sunglasses > div.additional > button')
    wishlist_buy_lens = (By.CSS_SELECTOR, 'div.product-item.lens > div.additional.lens > a')
    wishlist_buy_care = (By.CSS_SELECTOR, 'div.product-item  > div.additional.lens > a')
    header_cart = (By.CSS_SELECTOR, 'div.icons-panel > a.cart > svg')

    # Пункты меню (0-5)
    points_main_menu = (By.CSS_SELECTOR, '#content-wrapper > div.main-menu > ul > li > a')

    # Вернуться на главную
    goto_start_page = (By.CSS_SELECTOR, '#content-wrapper > section > main > div.double-no-goods > div.left > a')
    # Переход на страницу линз
    goto_lens_page = (By.CSS_SELECTOR, 'div.banner-block.js-banner-block.blue > div.button-holder > a')
    # Переход на страницу очков
    goto_sunglass_page = (By.CSS_SELECTOR, 'div.banner-block.js-banner-block.orange > div.button-holder > a')
    # Переход на страницу оправ
    goto_frames_page = (By.CSS_SELECTOR, 'div.banner-block.js-banner-block.grape > div.button-holder > a')

    # Название списка
    choise_name_wishlist = (By.CSS_SELECTOR, 'div.selectize-input.items.full.has-options.has-items > input')
    # Выбор - Список списков
    wishlists = (By.CSS_SELECTOR, 'div.selectize-dropdown.single.addresses-city > div > div')
    # Добавить
    add_in_wishlist = (By.CSS_SELECTOR, 'form > label.submit-popup > input[type=submit]')

    # Перейти в список желаний
    goto_wishlist = (By.CSS_SELECTOR, 'div.icons-panel > a.favourites > svg')

    # Работа со списками - купить
    lists_wishlist = (By.CSS_SELECTOR, '#wishlist-wrapper > div.products-control-panel > div.info > a')
    prods_wishlist = (By.CSS_SELECTOR, 'div.wishlist-products-section > div > div > div.main-content > a.img')
    lens_care_wishlist_buy = (By.CSS_SELECTOR, 'div.wishlist-products-section > div > div > div.additional.lens > a')
    frame_sunglass_wishlist_buy = (
        By.CSS_SELECTOR, 'div.wishlist-products-section > div > div > div.additional > button')

    # Удалить из списка (список эл-тов в списке)
    del_from_withlist = (
        By.CSS_SELECTOR, 'div.wishlist-products-wrapper > div > div.delete.js-delete-product-from-wishlist > svg')
    # Да
    del_yes = (By.CSS_SELECTOR, 'div.swal2-actions > button.swal2-confirm.swal2-styled')
    # Нет
    del_no = (By.CSS_SELECTOR, 'div.swal2-actions > button.swal2-cancel.swal2-styled')

    # Удалить список покупок
    del_withlist = (By.CSS_SELECTOR, 'div.delete-all-wishlist.js-delete-wishlist > div > svg')

    # Сохраненные статьи
    list_saved_articles = (By.CSS_SELECTOR, 'div.cabinet-saved > ul > li > a[target="_blank"]')
    del_article = (By.CSS_SELECTOR, 'div.cabinet-saved > ul > li > a.js-delete-from-saved')
