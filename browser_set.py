from pathlib import Path

class ChromeSet:

    chrome_driver_path = Path.cwd().parent / 'webdriver' / 'chromedriver.exe'


class EdgeSet:

    edge_driver_path = Path.cwd().parent / 'webdriver' / 'msedgedriver.exe'


class GeckoSet:

    gecko_driver_path = Path.cwd().parent / 'webdriver' / 'geckodriver.exe'


class OperaSet:
    opera_driver_path = Path.cwd().parent / 'webdriver' / 'geckodriver.exe'
