import pytest
from selenium import webdriver
from fake_useragent import UserAgent
from browser_set import ChromeSet
from pages.headers import Headers
from pages.test_sets import AuthSets
from pages.url_list import LinsaUa


@pytest.fixture(scope='module')
def web_driver_desktop(request):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    устанавливает размер окна как в десктопах (ПК, ноутбук), после выполнения основного кода закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = UserAgent()
    option.add_argument(f"User-Agent={user_agent.random}")
    option.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(1280, 960)
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='module')
def web_driver_mobile(request):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    устанавливает размер окна как в мобильных устройствах, после выполнения основного кода закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = UserAgent()
    option.add_argument(f"User-Agent={user_agent}")
    option.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(480, 960)
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_var_size(request, width):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    принимает в качестве опции ширину окна для разных устройств (десктоп, мобильные) , после выполнения основного кода
    закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = UserAgent()
    option.add_argument(f"User-Agent={user_agent}")
    option.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(width, 960)
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()

@pytest.fixture(scope='module')
def web_driver_auth_desktop(request):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    устанавливает размер окна как в десктопах (ПК, ноутбук), авторизует тестового пользователя, проверяет переход
    в кабинет. После выполнения основного кода выходит из кабинета и закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = UserAgent()
    option.add_argument(f"User-Agent={user_agent.random}")
    option.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(1280, 960)
    web_driver.delete_all_cookies()
    #
    page = Headers(web_driver, 10)
    # Открытие всплывающего окна авторизации
    page.login_btn_click()

    # Ввод данных авторизации, скриншот и переход в кабинет
    page.input_login_passw(AuthSets.auth_phone, AuthSets.auth_passw)
    page.save_screen_browser('auth_cabinet')
    page.auth_submit()
    page.wait_download_cabinet()
    assert page.get_relative_link() == LinsaUa.cabinet[0][0] or page.get_relative_link() == LinsaUa.cabinet[0][
        1], 'ERROR! Bad transactoin!'

    yield web_driver
    page.exit_cabinet()
    web_driver.quit()
