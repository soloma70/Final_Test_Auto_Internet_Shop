from urllib.parse import urlparse


class BasePage(object):
    """ Конструктор класса - метод init, получающий объект веб-драйвера, адрес страницы и время ожидания элемента"""

    def __init__(self, driver, url, wait=3):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(wait)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_url(self, url: str):
        self.driver.get(url)

    def save_screen_browser(self, name: str):
        self.driver.save_screenshot(f'screenshots\\{name}.png')

