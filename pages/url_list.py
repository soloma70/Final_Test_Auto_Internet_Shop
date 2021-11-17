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

    def sales_url(lng='ru'):
        if lng == 'ru':
            sales_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[0][0]}'
        elif lng == 'uk':
            sales_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[0][1]}'
        else:
            sales_url = f'{LinsaUa.start_url}'
        return sales_url

    def blog_url(lng='ru'):
        if lng == 'ru':
            blog_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[5][0]}'
        elif lng == 'uk':
            blog_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[5][1]}'
        else:
            blog_url = f'{LinsaUa.start_url}'
        return blog_url

    def lens_url(lng='ru'):
        if lng == 'ru':
            lens_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[1][0]}'
        elif lng == 'uk':
            lens_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[1][1]}'
        else:
            lens_url = f'{LinsaUa.start_url}'
        return lens_url

    def frames_url(lng='ru'):
        if lng == 'ru':
            lens_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[2][0]}'
        elif lng == 'uk':
            lens_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[2][1]}'
        else:
            lens_url = f'{LinsaUa.start_url}'
        return lens_url

    def sunglass_url(lng='ru'):
        if lng == 'ru':
            lens_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[3][0]}'
        elif lng == 'uk':
            lens_url = f'{LinsaUa.start_url}{LinsaUa.main_menu_urls[3][1]}'
        else:
            lens_url = f'{LinsaUa.start_url}'
        return lens_url
