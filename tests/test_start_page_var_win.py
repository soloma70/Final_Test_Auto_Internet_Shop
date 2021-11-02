# -*- encoding=utf8 -*-

import time, pytest
from pages.start_page import StartPage


@pytest.mark.parametrize("width",
                         [320, 425, 960, 1101, 1201, 1280, 1440, 2440]
    , ids=[' win size 320x960', ' win size 425x960', ' win size 960x960', ' win size 1100x960'
    , ' win size 1200x960', ' win size 1280x960', ' win size 1440x960', ' win size 2450x960'])
def test_start_page_var_win_width(web_driver_var_size, width):
    """Тест проверяет загрузку стартовой страницы сайта на различных устройствах, десктопных и мобильных,
    передавая в качестве параметра различную ширину окна браузера"""

    page_start = StartPage(web_driver_var_size, 5)
    if width == 320 or width == 425 or width == 960:
        assert page_start.start_img_mobile.is_displayed() == True, "ERROR screen"
    else:
        assert page_start.start_img.is_displayed() == True, "ERROR screen"