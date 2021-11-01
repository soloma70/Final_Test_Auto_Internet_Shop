import pytest, requests, os, random
from selenium import webdriver
from pages.browser_option import DriverChromeOption


@pytest.fixture(scope='module')
def web_driver(request):
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
    после выполнения основного кода закрывает браузер'''

    option = webdriver.ChromeOptions()
    user_agent = random.choice(DriverChromeOption.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=DriverChromeOption.chrome_driver_path, options=option)
    web_driver.set_window_size(1280, 960)
    # web_driver.implicitly_wait(3)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='module')
def web_driver_decktop(request):
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
    после выполнения основного кода закрывает браузер'''

    option = webdriver.ChromeOptions()
    user_agent = random.choice(DriverChromeOption.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=DriverChromeOption.chrome_driver_path, options=option)
    web_driver.set_window_size(1280, 960)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='module')
def web_driver_mobile(request):
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
    после выполнения основного кода закрывает браузер'''

    option = webdriver.ChromeOptions()
    user_agent = random.choice(DriverChromeOption.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=DriverChromeOption.chrome_driver_path, options=option)
    web_driver.set_window_size(425, 960)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def web_driver_var_size(request, width):
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
    после выполнения основного кода закрывает браузер'''

    option = webdriver.ChromeOptions()
    user_agent = random.choice(DriverChromeOption.chrome_user_agent)
    option.add_argument(f"User-Agent={user_agent}")
    web_driver = webdriver.Chrome(executable_path=DriverChromeOption.chrome_driver_path, options=option)
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
