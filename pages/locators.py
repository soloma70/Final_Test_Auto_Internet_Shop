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
    move_to_cart_popup = (
        By.CSS_SELECTOR, 'div[id="product-added-to-cart-popup"]>div>div>div>div>div[class="popup-infop"]>a')
    close_cart_popup = (By.CSS_SELECTOR,
                        'div[id="product-added-to-cart-popup"]>div>div>div>div>div[class="close-popup js-close-popup"]>svg')
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


class StartLocatorsMobile:
    # MOBILE LOCATORS

    # HEADERS LOCATORS
    # Start Image locator
    logo_img_mobile = (By.CSS_SELECTOR, 'div[class="left-mobile-header"] > a > img')

    # Search locators
    search_field_img = (By.CSS_SELECTOR, 'div[class="right-mobile-header"] > div > img')
    search_field = (By.CSS_SELECTOR, 'div[class="search-panel-mobile active"] > form > input')
    search_field_close = (By.CSS_SELECTOR, 'div[class="search-panel-mobile active"] > form > input')
    search_result = (By.CSS_SELECTOR, 'div[class="h-holder"] > div[class="amount"]')

    # Wishlist locator
    wishlist_btns = (By.CSS_SELECTOR, 'div[class="right-mobile-header"] > a > span')

    # Login locators
    login_name = (By.CSS_SELECTOR, 'input[name="login"]')
    login_pass = (By.CSS_SELECTOR, 'input[name="password"]')
    login_submit = (By.CSS_SELECTOR, 'input[id="auth-submit"]')
    login_close = (By.CSS_SELECTOR, 'div[class="close-popup js-close-popup"] > svg')

    # Cart locator
    cart_btn = (By.CSS_SELECTOR, 'div[class="right-mobile-header"] > a[class="cart"] > span')

    # RightSide Menu locators
    menu_button = (By.CSS_SELECTOR, 'div[class="left-mobile-header"] > div[class="menu-button js-open-menu"]')
    menu_button_close = (By.CSS_SELECTOR, 'div[class="mobile-close-menu js-mobile-close-menu"] > svg')
    lang_btn_active = (By.CSS_SELECTOR, 'div[class="controls"] > div > div')
    lang_btn = (By.CSS_SELECTOR, 'div[class="controls"] > div > ul > li > a')
    menu_points_main = (By.CSS_SELECTOR, 'div[id="content-wrapper"] > div[class="main-menu"] > ul > li > a')
    menu_points_hidden = (
        By.CSS_SELECTOR, 'div[id="content-wrapper"] > div[class="main-menu"] > ul[class="desktop-hidden"] > li > a')

    # MAIN PAGE LOCATORS
    # Banners locators
    banner_points = (By.CSS_SELECTOR, 'div[class="blocks-holder"] > div > a')
    amount_product = (By.CSS_SELECTOR, 'div[class="h-holder"]>div[class="amount"]')
    sales_banners = (By.CSS_SELECTOR, 'div[class="main-content"]')
    sales_sunglass = (
        By.CSS_SELECTOR, 'div[class="product-item sunglasses"] > div[class="main-content"] > a[class="img"] > img')
    add_cart_sunglass = (By.CSS_SELECTOR, 'button[id="md-to-basket"]')
    all_sales_prods = (By.CSS_SELECTOR, 'a[class="fat-button orange"]')

    # Add cart locators
    select_sunglass = (
        By.CSS_SELECTOR, 'div[data-id="33882"] > div[class="main-content"] > a[class="img"] > img')
    close_cart_popup = (
        By.CSS_SELECTOR,
        'div[id="product-added-to-cart-popup"]>div>div>div>div>div[class="close-popup js-close-popup"]>svg')
    amount_cart = (By.CSS_SELECTOR, 'div[class="right-mobile-header"]>a[class="cart"]>span[class="total-in-cart"]')

    # Love brand locators
    love_brands_sunglasses = (By.CSS_SELECTOR, 'div[class="brands-buttons-holder"] > div[data-id="sunglasses-brand"]')
    love_brands_lenses = (By.CSS_SELECTOR, 'div[class="brands-buttons-holder"] > div[data-id="lenses-brand"]')
    love_brands_accessories = (By.CSS_SELECTOR, 'div[class="brands-buttons-holder"] > div[data-id="accessories-brand"]')
    img_avizor = (By.CSS_SELECTOR, 'img[title="AVIZOR ENZYME"]')
    img_menicon = (By.CSS_SELECTOR, 'img[title="Menicon Progent"]')
    img_okvision = (By.CSS_SELECTOR, 'img[title="okvision I CARE"]')
    img_vogue = (By.CSS_SELECTOR, 'img[title="VOGUE"]')
    img_rayban = (By.CSS_SELECTOR, 'img[title="RAY-BAN"]')
    img_carrera = (By.CSS_SELECTOR, 'img[title="CARRERA"]')

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
    blog_card_1 = (By.XPATH, '//*[@id="content-wrapper"]/section[4]/div[2]/div/div/div[1]/div/a/div[2]/div[1]')
    blog_card_2 = (By.XPATH, '//*[@id="content-wrapper"]/section[4]/div[2]/div/div/div[2]/div/a/div[2]/div[1]')
    blog_card_3 = (By.XPATH, '//*[@id="content-wrapper"]/section[4]/div[2]/div/div/div[3]/div/a/div[2]/div[1]')
    blog_btn = (By.CSS_SELECTOR, 'section[class="main-blog"] > div[class="button-holder"] > a')
    blog_title = (By.CSS_SELECTOR, 'div[class="article-top"] > h1')

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


class SalesLocators:
    # DESKTOP LOCATORS

    # HEADERS LOCATORS
    # Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a.top-logo > img')

    # Sales Banners locator
    banner_imgs = (By.CSS_SELECTOR, 'div.sales-banner > div.top > div.img-banner > div')
    banner_btns = (By.CSS_SELECTOR, 'div.sales-banner > div.bottom > div.right > a.typical-button.juicy-green')
    products = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > a.img')
    products_buy = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.additional.lens > a')
    product_banner = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > a.img')
    products_banner_buy = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.additional.lens > a')
    amount_cart = (By.CSS_SELECTOR, 'div.icons-panel > a.cart > span.total-in-cart')

class ProductLensLocators:
    # Product card
    name = (By.CSS_SELECTOR, 'div.card-section > div.title-card-holder > h1')

    rating = (By.CSS_SELECTOR, 'div[class="card-section"] > div[class="card-rating"] > div > div[class="rev-amount"]')
    add_review = (By.CSS_SELECTOR, 'div[class="card-section"] > div[class="card-rating"] > div > a[class="add-review js-add-review"]')

    main = (By.CSS_SELECTOR, 'div[class="card-section"] > div[class="card-menu"] > nav > a[data-tab="main"]')
    char = (By.CSS_SELECTOR, 'div[class="card-section"] > div[class="card-menu"] > nav > a[data-tab="characteristics"]')
    photo = (By.CSS_SELECTOR, 'div[class="card-section"] > div[class="card-menu"] > nav > a[data-tab="photo"]')
    desc = (By.CSS_SELECTOR, 'div[class="card-section"] > div[class="card-menu"] > nav > a[data-tab="description"]')
    reviews = (By.CSS_SELECTOR, 'div[class="card-section"] > div[class="card-menu"] > nav > a[data-tab="reviews"]')

    price = (By.CSS_SELECTOR, '#js-goods-price-value')
    # Same eyes
    same_eyes = (By.CSS_SELECTOR, 'div[id="js-same-eyes"] > div > div > div > div > a[1] > svg')
    dioptr_same = (By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(3) > div > div.selectric > span')
    dioptr_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(3) > div > div.selectric-items > div > ul > li')
    curv_same = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(4) > div > div.selectric > div')
    curv_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(4) > div > div.selectric-items > div > ul > li')
    pack_one_same = (
        By.CSS_SELECTOR, 'div[id="lenses-quantity-block-same"] > div[class="quantity-label"] > div > label[class="goods-round"] > span[class="round"]')
    pack_mul_same = (
        By.CSS_SELECTOR, 'div[id="lenses-quantity-block-same"] > div[class="quantity-label"] > div > label[class="goods-round append"] > span[class="round"]')
    amount_same = (
        By.CSS_SELECTOR, '#product-quantity-same')
    amount_minus_same = (
        By.CSS_SELECTOR,
        '#lenses-quantity-block-same > div.quan-wrapper-cell > div > div.minus.js-sub-product-quantity')
    amount_plus_same = (
        By.CSS_SELECTOR,
        '#lenses-quantity-block-same > div.quan-wrapper-cell > div > div.plus.js-add-product-quantity')
    # Different eyes
    diff_eyes = (
        By.CSS_SELECTOR, 'form[id="js-different-eyes"] > div > div > div > div > a[2] > svg')
    dioptr_left = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-left"] > div[1] > div > div[class="selectric"] > span')
    dioptr_right = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-right"] > div[1] > div > div[class="selectric"] > span')
    curv_left = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-left"] > div[2] > div > div[class="selectric"] > span')
    curv_right = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-right"] > div[2] > div > div[class="selectric"] > span')
    pack_one_left = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-left"] > div[class="quantity-label"] > div > label[class="goods-round"] > span[class="round"]')
    pack_one_right = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-right"] > div[class="quantity-label"] > div > label[class="goods-round"] > span[class="round"]')
    pack_mul_left = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-left"] > div[class="quantity-label"] > div > label[class="goods-round append"] > span[class="round"]')
    pack_mul_right = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-right"] > div[class="quantity-label"] > div > label[class="goods-round append"] > span[class="round"]')
    amount_left = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-left"] > div[class="quan-wrapper-cell"] > div > div[class="inp-holder"] > input')
    amount_right = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-right"] > div[class="quan-wrapper-cell"] > div > div[class="inp-holder"] > input')
    amount_minus_left = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-left"] > div[class="quan-wrapper-cell"] > div > div[class="minus js-sub-product-quantity"] > span')
    amount_minus_right = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-right"] > div[class="quan-wrapper-cell"] > div > div[class="minus js-sub-product-quantity"] > span')
    amount_plus_left = (
        By.CSS_SELECTOR,
        'div[id="lenses-quantity-block-left"] > div[class="quan-wrapper-cell"] > div > div[class="plus js-add-product-quantity"] > span')
    amount_plus_right = (
            By.CSS_SELECTOR,
            'div[id="lenses-quantity-block-right"] > div[class="quan-wrapper-cell"] > div > div[class="plus js-add-product-quantity"] > span')

    buy_btn = (By.CSS_SELECTOR, 'button[id="md-to-basket"]')
    buy_one_click = (By.CSS_SELECTOR, 'a[id="one-click-buy js-lenses-quick-order"]')
    buy_repeat_order = (By.CSS_SELECTOR, 'a[id="one-click-buy js-open-auth-popup "]')
    close_cart_popup = (By.CSS_SELECTOR,
                        'div[id="product-added-to-cart-popup"]>div>div>div>div>div[class="close-popup js-close-popup"]>svg')

    add_favorite = (By.CSS_SELECTOR, 'div[class="add-to-favorites js-add-to-wishlist"] > svg')  # 5 items

    alternative_name = (By.CSS_SELECTOR, 'div[class="md-title-goods"] > span')
    alternative_prods = (
        By.CSS_SELECTOR, 'section[class="products-section promos-compact lenses-alt"] > div[class="products-wrapper"] > div')  # 4 items
    alternative_more = (By.CSS_SELECTOR, 'a[class="fat-button blue"]')

    viewed_name = (By.CSS_SELECTOR, 'div[class="standard-title"]')
    viewed_prods = (
        By.CSS_SELECTOR,
        'section[class="products-section promos-compact "] > div[class="products-wrapper"] > div')  # 3 items
    viewed_more = (By.CSS_SELECTOR, 'a[class="fat-button blue"]')

    reviews_amount = (By.CSS_SELECTOR, 'div[class="reviews-title"]')
    review_add = (By.CSS_SELECTOR, 'a[class="fat-button glow-button blue min_245 js-add-review"]')
    reviews_block = (By.CSS_SELECTOR, 'div[class="reviews-block"] > div[class="review-item"]')  # 4 items
    reviews_yet = (By.CSS_SELECTOR, 'div[class="reviews-block"] > div[class="button-holder"] > a')

class BlogLocators:
    # DESKTOP LOCATORS

    # HEADERS LOCATORS
    # Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a.top-logo > img')

    # Sales Banners locator
    news_tags = (By.CSS_SELECTOR, 'div.news-tags-wrapper > a')  # 8 tegs (href)
    news = (By.CSS_SELECTOR, 'div.news-wrapper > a')  # 9 blocks (href)
    news_name = (By.CSS_SELECTOR, 'h1.article-h1')
    pagination = (By.CSS_SELECTOR, '#content-wrapper > div.pagination > a')  # 5 pages + arrow (all 11 pages)
    arrow_right = (By.CSS_SELECTOR, 'a.arrow-right-pagination > div')
    arrow_left = (By.CSS_SELECTOR, 'a.arrow-left-pagination > div')