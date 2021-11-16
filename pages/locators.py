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
    callback_form_submit = (By.CSS_SELECTOR, 'button.b24-form-btn')
    callback_form_close = (By.CSS_SELECTOR, 'div.b24-window-panel.b24-window-panel-pos-right > button')

    # Login locators
    login_btn = (By.CSS_SELECTOR, 'a.enter.md-cab-link.js-open-auth-popup')
    login_name = (By.CSS_SELECTOR, 'input[name="login"]')
    login_pass = (By.CSS_SELECTOR, 'input[name="password"]')
    login_submit = (By.CSS_SELECTOR, 'input[id="auth-submit"]')
    login_close = (By.CSS_SELECTOR, 'div.close-popup.js-close-popup > svg')

    # Wishlist locator
    wishlist_btns = (By.CSS_SELECTOR, 'div. icons-panel > a > svg')

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

    # PopUp Registration locators
    registr_btn = (By.CSS_SELECTOR, 'a.fat-button.black.js-open-auth-popup')
    registr_popup_windows = (By.CSS_SELECTOR, '#auth-popup > div > div > div.popup-window')
    registr_popup_name = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="name"]')
    registr_popup_phone = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="phone"]')
    registr_popup_passw = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="password"]')
    registr_popup_chec = (By.CSS_SELECTOR, 'label.check-label > input[type="checkbox"]')
    registr_popup_add = (By.CSS_SELECTOR, 'label.submit-popup > input[type="submit"]')
    registr_popup_close = (By.CSS_SELECTOR, '#auth-popup > div > div > div > div.top > div > svg')

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
    love_brands_sunglasses = (By.CSS_SELECTOR, 'div.brands-buttons-holder > div.sunglasses-brand')
    love_brands_lenses = (By.CSS_SELECTOR, 'div.brands-buttons-holder > div.lenses-brand')
    love_brands_accessories = (By.CSS_SELECTOR, 'div.brands-buttons-holder > div.accessories-brand')
    img_avizor = (By.CSS_SELECTOR, 'img[title="AVIZOR ENZYME"]')
    img_menicon = (By.CSS_SELECTOR, 'img[title="Menicon Progent"]')
    img_okvision = (By.CSS_SELECTOR, 'img[title="okvision I CARE"]')
    img_vogue = (By.CSS_SELECTOR, 'img[title="VOGUE"]')
    img_rayban = (By.CSS_SELECTOR, 'img[title="RAY-BAN"]')
    img_carrera = (By.CSS_SELECTOR, 'img[title="CARRERA"]')

    # PopUp Registration locators
    registr_btn = (By.CSS_SELECTOR, 'a.fat-button.black.js-open-auth-popup')
    registr_popup_windows = (By.CSS_SELECTOR, '#auth-popup > div > div > div.popup-window')
    registr_popup_name = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="name"]')
    registr_popup_phone = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="phone"]')
    registr_popup_passw = (By.CSS_SELECTOR, 'div.input-wrapper.green > input[name="password"]')
    registr_popup_chec = (By.CSS_SELECTOR, 'label.check-label > input[type="checkbox"]')
    registr_popup_add = (By.CSS_SELECTOR, 'label.submit-popup > input[type="submit"]')
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

class CartLocators:
    amount_cart_header = (By.CSS_SELECTOR, 'div.icons-panel > a.cart > span.total-in-cart')
    close_popup_cart = (By.CSS_SELECTOR,
                        '#product-added-to-cart-popup > div > div > div > div > div.close-popup.js-close-popup > svg')

class ProductLocators:
    products = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.main-content > a.img')
    products_buy = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.additional > button')
    products_lens_buy = (By.CSS_SELECTOR, 'div.products-wrapper > div > div.additional.lens > a')

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
    same_eyes = (
        By.CSS_SELECTOR, '#js-different-eyes > div > div.titles-row > div.label > div > > a[href="#js-same-eyes"] > svg')
    dioptr_same = (By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(3) > div > div.selectric > span')
    dioptr_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(3) > div > div.selectric-items > div > ul > li')
    curv_same = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(4) > div > div.selectric > div')
    curv_list = (
        By.CSS_SELECTOR, '#lenses-selects-form-same > div:nth-child(4) > div > div.selectric-items > div > ul > li')
    pack_one_same = (
        By.CSS_SELECTOR, '#lenses-quantity-block-same > div.quantity-label > div > label.goods-round > span.round')
    pack_mul_same = (
        By.CSS_SELECTOR, '#lenses-quantity-block-same > div.quantity-label > div > label.goods-round append > span.round')
    amount_same = (
        By.CSS_SELECTOR, '#product-quantity-same')
    amount_minus_same = (
        By.CSS_SELECTOR, '#lenses-quantity-block-same > div.quan-wrapper-cell > div > div.minus.js-sub-product-quantity')
    amount_plus_same = (
        By.CSS_SELECTOR, '#lenses-quantity-block-same > div.quan-wrapper-cell > div > div.plus.js-add-product-quantity')

    # Different eyes
    diff_eyes = (
        By.CSS_SELECTOR, '#js-same-eyes > div > div.titles-row > div > div > a[href="#js-different-eyes"] > svg')
    dioptr_left = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-left"] > div[1] > div > div[class="selectric"] > span')
    dioptr_right = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-right"] > div[1] > div > div[class="selectric"] > span')
    curv_left = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-left"] > div[2] > div > div[class="selectric"] > span')
    curv_right = (
        By.CSS_SELECTOR, 'form[id="lenses-selects-form-right"] > div[2] > div > div[class="selectric"] > span')
    pack_one_left = (
        By.CSS_SELECTOR, '#lenses-quantity-block-left > div.quantity-label > div > label.goods-round > span.round')
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

    buy_btn = (By.CSS_SELECTOR, '#md-to-basket')
    buy_one_click = (By.CSS_SELECTOR, 'a[id="one-click-buy js-lenses-quick-order"]')
    buy_repeat_order = (By.CSS_SELECTOR, 'a[id="one-click-buy js-open-auth-popup "]')

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
    # Pagination locators
    pagination = (By.CSS_SELECTOR, '#content-wrapper > div.pagination > a')  # 5 pages + arrow (all 11 pages)
    arrow_right = (By.CSS_SELECTOR, 'a.arrow-right-pagination > div')
    arrow_left = (By.CSS_SELECTOR, 'a.arrow-left-pagination > div')

class LensLocators:
    # DESKTOP LOCATORS

    # HEADERS LOCATORS: Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a.top-logo > img')

    # Filter locators
    filters = (By.CSS_SELECTOR, 'div.product-filters-titles.js-filter-toggle-items > div > span')  # 7 items
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
    clear_all_filters = (By.CSS_SELECTOR, 'div.clear-all.js-remove-all-filters > div.delete-cross')


    # Sort locators
    sort_by = (By.CSS_SELECTOR, 'section.sort_panel > a') # 4 items

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
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.main-content > a.top') # 16 items
    card_lens_amount = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.main-content > div.bottom > div.lenses_sizes > div:nth-child(1) > div > div.amount')
    card_lens_price = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.main-content > div.bottom > div.lenses_sizes > div:nth-child(1) > div > div.add-price')

    cards_lens_add_btn = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.lens > div.additional.lens > a.buy-button ')  # 16 items

    # Pagination locators
    pagination = (By.CSS_SELECTOR, '#content-wrapper > div.pagination > a.page-number ')  # 5 pages + arrow (all 6 pages)
    arrow_right = (By.CSS_SELECTOR, 'a.arrow-right-pagination > div')
    arrow_left = (By.CSS_SELECTOR, 'a.arrow-left-pagination > div')

    # Footer More info
    more_inf = (By.CSS_SELECTOR, 'div.footer_seotext > i')


class FramesLocators:
    # DESKTOP LOCATORS

    # HEADERS LOCATORS: Start Image locator
    logo_img = (By.CSS_SELECTOR, 'a.top-logo > img')

    # Filter locators
    filters = (By.CSS_SELECTOR, 'div.product-filters-titles.js-filter-toggle-items > div > span')  # 7 items
    # brands 7/6, sex 4, temple_length 7/7/3, bridge_width 7/6, eyepiece_width 7/7/7,
    # frame_shape 7/3, frame_type 2, dioptr 4, collection_year 7/6, polarization 1
    filter_list = [
        (By.CSS_SELECTOR, '#filter-tab-1 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-2 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-3 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-4 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-5 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-6 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-7 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-8 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-9 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a'),
        (By.CSS_SELECTOR, '#filter-tab-10 > div.filter-slider.slider.slick-initialized.slick-slider > div > div > div.slick-slide.slick-current.slick-active > div > div > label > a')
                ]
    clear_all_filters = (By.CSS_SELECTOR, 'div.clear-all.js-remove-all-filters > div.delete-cross')


    # Sort locators
    sort_by = (By.CSS_SELECTOR, 'section.sort_panel > a') # 5 items

    # Frames Card locator
    name = (By.CSS_SELECTOR, 'h1.standard-title')
    amount_frames = (By.CSS_SELECTOR, 'div.h-holder > div.amount')
    card_frames_full = (By.CSS_SELECTOR, 'div.main-content')
    card_frames_wishlist = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.add-to-favorites.js-add-to-wishlist > svg')
    cards_frames_brand = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > a.top > span.product-type')
    cards_frames_name = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > a.top > span.title')
    cards_frames_url = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > a.top') # 16 items
    card_frames_sex = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > div.bottom > div.glasses-size > div:nth-child(1)')
    card_frames_temple_length = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > div.bottom > div.glasses-size > div:nth-child(2)')
    card_frames_bridge_width = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > div.bottom > div.glasses-size > div:nth-child(3)')
    card_frames_eyepiece_width = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > div.bottom > div.glasses-size > div:nth-child(4)')
    card_frames_price = (By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.main-content > div.bottom > div.prices > div')

    cards_frames_add_btn = (
        By.CSS_SELECTOR, 'div.products-wrapper > div.product-item.frames > div.additional > a.buy-button ')  # 16 items

    # Pagination locators
    pagination = (By.CSS_SELECTOR, '#content-wrapper > div.pagination > a.page-number ')  # 87 pages + arrow (all 6 pages)
    arrow_right = (By.CSS_SELECTOR, 'a.arrow-right-pagination > div')
    arrow_left = (By.CSS_SELECTOR, 'a.arrow-left-pagination > div')

    # Footer More info
    more_inf = (By.CSS_SELECTOR, 'div.footer_seotext > i')


