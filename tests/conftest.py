import pytest, random
from selenium import webdriver
from browser_set import ChromeSet
from datetime import datetime


@pytest.fixture(scope='module')
def web_driver(request):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    меняет размер окна, после выполнения основного кода закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = random.choice(ChromeSet.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(1280, 960)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='module')
def web_driver_desktop(request):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    устанавливает размер окна как в десктопах (ПК, ноутбук), после выполнения основного кода закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = random.choice(ChromeSet.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(1280, 960)
    begin_time = datetime.now()
    yield web_driver
    print(f'\nВремя тестирования: {datetime.now() - begin_time}')
    web_driver.quit()


@pytest.fixture(scope='module')
def web_driver_mobile(request):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    устанавливает размер окна как в мобильных устройствах, после выполнения основного кода закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = random.choice(ChromeSet.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(425, 960)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_var_size(request, width):
    """Фикстура рандомно передает в опции веб-драйвера браузера разные занчения User-Agent, загружает веб-драйвер Хром,
    принимает в качестве опции ширину окна для разных устройств (десктоп, мобильные) , после выполнения основного кода
    закрывает браузер"""

    option = webdriver.ChromeOptions()
    user_agent = random.choice(ChromeSet.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=ChromeSet.chrome_driver_path, options=option)
    web_driver.set_window_size(width, 960)
    yield web_driver
    web_driver.quit()

# @pytest.fixture(scope='module')
# def web_driver_with_cookies(request):
#     '''Фикстура загружает авторизуется, получает cookies и передает их в драйвер'''
#
#     print('\nПолучаем ключ авторизации и куки...')
#     response = requests.post(url=PetFriend.LOGIN_URL
#                              , data={"email": valid_email, "pass": valid_password})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#
#     option = webdriver.ChromeOptions()
#     option.add_argument(
#         "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
#     web_driver = webdriver.Chrome(executable_path=web_driver_path, options=option)
#     web_driver.set_window_size(1280, 960)
#     web_driver.implicitly_wait(3)
#     web_driver.get(PetFriend.START_URL)
#     cookie_list = response.request.headers.get('Cookie').split('=')
#     web_driver.add_cookie({"name":cookie_list[0], "value":cookie_list[1]})
#     yield web_driver
#     web_driver.quit()
