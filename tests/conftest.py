import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from fake_useragent import UserAgent
from browser_set import ChromeSet, EdgeSet, GeckoSet, OperaSet
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
def web_driver_var_size(request, width: int):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    принимает в качестве опции ширину окна для разных устройств (десктоп, мобильные), после выполнения основного кода
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


@pytest.fixture(scope='function')
def web_driver_gecko(request, width: int):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер
    FireFox, принимает в качестве опции ширину окна для разных устройств (десктоп, мобильные),
    после выполнения основного кода закрывает браузер"""

    option = webdriver.FirefoxOptions()
    user_agent = UserAgent()
    option.set_preference("general.useragent.override", user_agent.random)
    web_driver = webdriver.Firefox(executable_path=GeckoSet.gecko_driver_path, options=option)
    web_driver.set_window_size(width, 960)
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_edge(request, width: int):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Edge,
    устанавливает размер окна как в десктопах (ПК, ноутбук), после выполнения основного кода закрывает браузер"""

    option = Options()
    option.use_chromium = True
    web_driver = webdriver.Edge(executable_path=EdgeSet.edge_driver_path)
    web_driver.set_window_size(width, 960)
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_opera(request, width: int):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер
    Opera, принимает в качестве опции ширину окна для разных устройств (десктоп, мобильные),
    после выполнения основного кода закрывает браузер"""

    web_driver = webdriver.Opera(executable_path=OperaSet.opera_driver_path)
    web_driver.set_window_size(width, 960)
    web_driver.delete_all_cookies()
    yield web_driver
    web_driver.quit()
