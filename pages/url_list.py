class LinsaUa:
    start_url = 'https://linza.com.ua'

    right_menu_urls = [
        ['/ru/articles/blog/', '/uk/articles/blog/'],
        ['/ru/page/about/', '/uk/page/about/'],
        ['/ru/sluzhba-podderzhki/', '/uk/sluzhba-pidtrimki/'],
        ['/ru/page/dostavka/', '/uk/page/dostavka/'],
        ['/ru/obmen-vozvrat/', '/uk/obmen-vozvrat/'],
        ['/ru/warranty/', '/uk/warranty/'],
        ['/ru/diskont/', '/ru/diskont/'],
        ['/ru/certificates/', '/uk/certificates/'],
        ['/ru/brands/', '/uk/brands/'],
    ]

    left_menu_urls = [
        ['/ru/sluzhba-podderzhki/', '/uk/sluzhba-pidtrimki/'],
        ['/ru/page/dostavka/', '/uk/page/dostavka/'],
        ['/ru/obmen-vozvrat/', '/uk/obmen-vozvrat/'],
        ['/ru/diskont/', '/ru/diskont/'],
        ['/ru/certificates/', '/uk/certificates/'],
        ['/ru/page/about/', '/uk/page/about/'],
        ['/ru/warranty/', '/uk/warranty/']
    ]

    cabinet = [
        ['/ru/cabinet/', '/uk/cabinet/'],
        ['/ru/edit-profile/', '/uk/edit-profile/'],
        ['/ru/wishlist/', '/uk/wishlist/'],
        ['/ru/orders/', '/uk/orders/'],
        ['/ru/addresses/', '/uk/addresses/'],
        ['/ru/saved-news/', '/uk/saved-news/']
    ]

    cart = [
        ['/ru/cart/', '/uk/cart/']
    ]

    main_menu_urls = [
        ['/ru/sales/', '/uk/sales/'],
        ['/ru/contact-lenses/', '/uk/contact-lenses/'],
        ['/ru/frames/', '/uk/frames/'],
        ['/ru/sunglasses/', '/uk/sunglasses/'],
        ['/ru/contact-lenses-care/', '/uk/contact-lenses-care/'],
        ['/ru/articles/blog/', '/uk/articles/blog/']
    ]

    banners_urls = [
        ['/ru/contact-lenses/', '/uk/contact-lenses/'],
        ['/ru/sunglasses/', '/uk/sunglasses/'],
        ['/ru/frames/', '/uk/frames/'],
    ]

    footers_menu_urls = [
        ['/ru/sluzhba-podderzhki/', '/uk/sluzhba-pidtrimki/'],
        ['/ru/page/dostavka/', '/uk/page/dostavka/'],
        ['/ru/obmen-vozvrat/', '/uk/obmen-vozvrat/'],
        ['/ru/diskont/', '/ru/diskont/'],
        ['/ru/certificates/', '/uk/certificates/'],
        ['/ru/page/about/', '/uk/page/about/'],
        ['/ru/warranty/', '/uk/warranty/'],
        ['/ru/sitemap/', '/uk/sitemap/'],
        ['/ru/page/politica/', '/uk/page/politica/'],
        ['/ru/page/ps/', '/uk/page/ps/'],
        ['https://www.facebook.com/linza.com.ua', 'https://www.facebook.com/linza.com.ua'],
        ['https://www.instagram.com/linza.ua/', 'https://www.instagram.com/linza.ua/'],
    ]

    def aggregation_urls(lng: str, locator: list, index: int) -> str:
        if lng == 'ru':
            url = f'{LinsaUa.start_url}{locator[index][0]}'
        elif lng == 'uk':
            url = f'{LinsaUa.start_url}{locator[index][1]}'
        else:
            url = f'{LinsaUa.start_url}'
        return url

    def sales_url(lng='ru') -> str:
        sales_url = LinsaUa.aggregation_urls(lng, LinsaUa.main_menu_urls, 0)
        return sales_url

    def lens_url(lng='ru') -> str:
        lens_url = LinsaUa.aggregation_urls(lng, LinsaUa.main_menu_urls, 1)
        return lens_url

    def frames_url(lng='ru') -> str:
        frame_url = LinsaUa.aggregation_urls(lng, LinsaUa.main_menu_urls, 2)
        return frame_url

    def sunglass_url(lng='ru') -> str:
        sunglass_url = LinsaUa.aggregation_urls(lng, LinsaUa.main_menu_urls, 3)
        return sunglass_url

    def care_url(lng='ru') -> str:
        care_url = LinsaUa.aggregation_urls(lng, LinsaUa.main_menu_urls, 4)
        return care_url

    def blog_url(lng='ru') -> str:
        blog_url = LinsaUa.aggregation_urls(lng, LinsaUa.main_menu_urls, 5)
        return blog_url

    def cart_url(lng='ru') -> str:
        cart_url = LinsaUa.aggregation_urls(lng, LinsaUa.cart, 0)
        return cart_url

    def cabinet_url(lng='ru') -> str:
        cabinet_url = LinsaUa.aggregation_urls(lng, LinsaUa.cabinet, 0)
        return cabinet_url

    def edit_profile_url(lng='ru') -> str:
        edit_profile_url = LinsaUa.aggregation_urls(lng, LinsaUa.cabinet, 1)
        return edit_profile_url

    def wishlist_url(lng='ru') -> str:
        wishlist_url = LinsaUa.aggregation_urls(lng, LinsaUa.cabinet, 2)
        return wishlist_url

    def orders_url(lng='ru') -> str:
        orders_url = LinsaUa.aggregation_urls(lng, LinsaUa.cabinet, 3)
        return orders_url

    def addresses_url(lng='ru') -> str:
        addresses_url = LinsaUa.aggregation_urls(lng, LinsaUa.cabinet, 4)
        return addresses_url

    def saved_new_url(lng='ru') -> str:
        saved_new_url = LinsaUa.aggregation_urls(lng, LinsaUa.cabinet, 4)
        return saved_new_url