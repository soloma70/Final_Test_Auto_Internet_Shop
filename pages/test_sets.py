class AuthSets:
    auth_name = 'Пупкин Василий'
    auth_phone = '+380668754059'
    auth_email = 'vasja_pupkin@gmail.com'
    auth_passw = 'vV123456'
    adress = [['Харьков', 'просп. Гагаріна', '72', '25'],
               ['Запорожье', 'вул. Цитрусова', '4', '56']]
    birthday = '15.06.1985'
    my_wish_list = 'Тестовый список желаний'
    test_wish_list = 'User Stories Wishlist'

class RegSets:
    reg_name = 'Иванов Сергей'
    # Для регистрации используется телефон без +380
    # При регистрации запрашивает код подтверждения по SMS - 6 цифр. Для успешной регистрации телефон д.б. реальным
    reg_phone = '681474653'
    reg_passw = 'I123456i'
    reg_phone_neg_test = '681475353'


class SendOrderSets:
    name = 'Пупкин Василий'
    email = 'vasja_pupkin@gmail.com'
    phone = '505555555'
    courier = [['Харьков', 'просп. Гагаріна', '72', '25'],
               ['Запорожье', 'вул. Цитрусова', '4', '56']]
    nova_poshta = [['Харьков', '39'],
                   ['Запорожье', '22']]


class MainMenuSets:
    amount_menu_points = 6


class LensSets:
    interogo = ['INTEROJO', 'Fusion', 'Сферические', 'Месяц', '8.6', '14.2', ''
        , 'Контактные линзы FUSION New', 'INTEROJO']

    cooper_vision = ['COOPER VISION', 'ClearLux', 'Сферические', 'Однодневные', '8.6', '14.1', ''
        , 'Контактные линзы ClearLux OneDay Aspheric', 'COOPER VISION']

    sauflon = ['SAUFLON', 'ClearLux', 'Сферические', 'Полгода', '8.4', '14.0', ''
        , 'Контактные линзы CLEARLUX 42 UV', 'SAUFLON']

    O2O2 = ['', 'O2O2', 'Торические', 'Месяц', '8.6', '14.2', ''
        , 'Контактные линзы O2O2 Toric', 'INTEROJO']

    # brands 3, line 3, type 3, repl mode 3, base curv 2, diameter 2, dioptr 3
    filter_set_positive = [
        ['BAUSCH+LOMB', 'GELFLEX', 'Maxima Optics'],
        ['Fusion', 'Air Optix', 'FreshLook'],
        ['Сферические', 'Мультифокальные', 'Карнавальные'],
        ['Однодневные', 'Месяц', 'Полгода'],
        ['8.4', '8.6'],
        ['14.2', '14.5'],
        ['-04.00', '+0.75', '-2.75']
    ]

    filter_set_negative = [
        [''],
        [''],
        [''],
        [''],
        [''],
        [''],
        ['']
    ]

    filter_set_uc = [
        ['INTEROJO'],
        ['Fusion'],
        ['Сферические'],
        ['Месяц'],
        ['8.6'],
        ['14.2'],
        ['-4.00', '-2.75']
    ]


class FramesSets:
    police = ['POLICE', 'мужские', 'квадратная', 'Полноободковая', ''
        , ['Оправа Police VPL886 0700 57']
        , 'POLICE']

    guess = ['GUESS', 'женские', '', '', ''
        , ['Оправа GUESS GU2707 056 53'], 'GUESS']

    ray_ban = ['RAY-BAN', 'унисекс', '', '', ''
        , ['Оправа RX 6397 2932 54']
        , 'RAY-BAN']

    sky = ['', 'детские', 'квадратная', 'Полноободковая', ''
        , ['Оправа SKY SKO 0922 BLU'], 'SKY']

    # brands 2, sex 4
    filter_set_positive = [
        ['FURLA', 'SKY'],
        ['мужские', 'женские', 'детские', 'унисекс'],
    ]

    filter_set_negative = [
        [''],
        [''],
    ]

    filter_set_uc = [
        'CARRERA',
        'мужские'
    ]


class SunglassSets:
    police = ['POLICE', 'мужские', 'маска', '',
              ['Солнцезащитные очки Police SPLA28 06AA 99'], 'POLICE']

    furla = ['FURLA', 'женские', '', '',
             ['Солнцезащитные очки Furla SFU347 579Y 55'], 'FURLA']

    ray_ban = ['RAY-BAN', 'унисекс', '', '',
               ['Солнцезащитные очки RAY-BAN 4273 601/71 52']
        , 'RAY-BAN']

    polaroid = ['', 'детские', 'кошачий глаз', '',
                ['Солнцезащитные очки PK PLD 8032/S C9A49M9'], 'POLAROID']

    versace = ['VERSACE', 'женские', '', '',
               ['Солнцезащитные очки VE 4393 533587 46'], 'VERSACE']

    # brands 5, sex 4
    filter_set_positive = [
        ['ALEXANDER MCQUEEN', 'GUCCI', 'MICHAEL KORS', 'PUMA', 'VOGUE'],
        ['мужские', 'женские', 'детские', 'унисекс'],
    ]

    filter_set_negative = [
        [''],
        [''],
    ]

    filter_set_uc = [
        'VOGUE',
        'женские',
    ]


class CareSets:
    soleko = ['SOLEKO', '20мл', 'УВЛАЖНЯЮЩИЕ КАПЛИ',
              ['Капли Ekinos drops', 'Капли Queens I-Fresh Yal drops 20ml'], 'SOLEKO', 'SOLEKO']

    alcon = ['ALCON', '120мл', 'МНОГОФУНКЦИОНАЛЬНЫЙ РАСТВОР',
              ['Alcon Opti-Free Express'], 'ALCON', 'ALCON']

    olmi = ['ТОВ "ОЛМІ"', '', 'Контейнер',
             ['Контейнер для линз B&L'], 'ТОВ "ОЛМІ"', 'OLMI']

    # brands 5, sex 4, temple length 4, bridge width 2, eyepiece width 2
    filter_set_positive = [
        ['Menicon Co., Ltd', 'INTEROJO', 'AVIZOR', 'Фармзавод Єльфа А.Т.'],
        ['100мл', '350мл', '3мл'],
        ['Дорожный набор', 'ДЛЯ ЖЕСТКИХ ЛИНЗ (GPL)', 'УВЛАЖНЯЮЩИЕ КАПЛИ'],
    ]

    filter_set_negative = [
        [''],
        ['50мл'],
        [''],
    ]

    filter_set_uc = [
            'ALCON',
            '120мл',
            'МНОГОФУНКЦИОНАЛЬНЫЙ РАСТВОР',
            'Opti-Free Express'
            ]

    set_vol = '355мл'
