class RegSets:
    reg_name = 'Пупкин Василий Васильевич'
    reg_phone = '0505555555'
    reg_passw = 'V123456'

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
    police = ['POLICE', 'мужские', '', '17', '', 'квадратная', 'Повноободкова', '', '', 'Нет'
        , ['Оправа Police VPL886 D82M 54', 'Оправа Police VPLA47 08H5 55', 'Оправа Police VPLA47 0301 55']
        , ' POLICE ']

    guess = ['GUESS', 'женские', '135', '17', '48', '', '', '', '', 'Нет'
        , ['Оправа GUESS GU2670 032 52', 'Оправа GUESS GU2658 052 50'], 'GUESS']

    ray_ban = ['RAY-BAN', 'унисекс', '130', '18', '48', '', '', '', '', 'Нет'
        , ['Оправа RY 1601 3685 48', 'Оправа RY 1601 3811 48', 'Оправа RY 1601 3813 48']
        , 'RAY-BAN']

    sky = ['', 'детские', '140', '16', '', 'квадратная', 'Повноободкова', '', '', 'Нет'
        , ['Оправа SKY SKO 0922 BLU'], 'SKY']

    # brands 2, sex 4, temple length 3, bridge width 2, eyepiece width 2
    filter_set_positive = [
        ['FURLA', 'SKY'],
        ['мужские', 'женские', 'детские', 'унисекс'],
        ['130', '145', '150'],
        ['15', '21'],
        ['45', '59']
    ]

    filter_set_negative = [
        [''],
        [''],
        ['144'],
        ['12'],
        ['60']
    ]

    filter_set_uc = [
        ['CARRERA'],
        ['мужские'],
        ['145'],
        ['20'],
        ['50']
    ]


class SunglassSets:
    police = ['POLICE', 'мужские', '', '', '', 'маска', '', '',
              ['Солнцезащитные очки Police SPLA28 06AA 99'], 'POLICE']

    furla = ['FURLA', 'женские', '115', '', '', '', '', '',
             ['Солнцезащитные очки Furla SFU309 0579 99'], 'FURLA']

    ray_ban = ['RAY-BAN', 'унисекс', '125', '', '', '', '', '',
            ['Солнцезащитные очки RB 4345 65320N 58', 'Солнцезащитные очки RB 4345 710/13 58',
           'Солнцезащитные очки RB 4345 601/71 58', 'Солнцезащитные очки RJ 9062S 70788G 48',
           'Солнцезащитные очки RB 4337 61974L 59', 'Солнцезащитные очки RJ 9506S 223/2P 52',
           'Солнцезащитные очки RB 4347 601/71 60', 'Солнцезащитные очки RB 4347 65318G 60',
           'Солнцезащитные очки RB 4345 653011 58']
        , 'RAY-BAN']

    polaroid = ['', 'детские', '125', '', '', 'кошачий глаз', '', '',
           ['Солнцезащитные очки PK PLD 8032/S C9A49M9', 'Солнцезащитные очки PK PLD 8032/S 80749MF'], 'POLAROID']

    versace = ['VERSACE', 'женские', '120', '', '', '', '', '',
              ['Солнцезащитные очки VE 4393 533587 46', 'Солнцезащитные очки VE 4393 52171W 46'], 'VERSACE']

    # brands 5, sex 4, temple length 4, bridge width 2, eyepiece width 2
    filter_set_positive = [
        ['ALEXANDER MCQUEEN', 'GUCCI', 'MICHAEL KORS', 'PUMA', 'VOGUE'],
        ['мужские', 'женские', 'детские', 'унисекс'],
        ['120', '135', '142', '152'],
        ['1', '133'],
        ['35', '55']
    ]

    filter_set_negative = [
        ['BALENCIAGA'],
        [''],
        ['160'],
        ['138'],
        ['40']
    ]

    filter_set_uc = [
        ['GUCCI'],
        ['женские'],
        ['135'],
        ['1'],
        ['55']
    ]


class SearchSets:
    pass