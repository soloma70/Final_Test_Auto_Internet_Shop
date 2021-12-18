## Финальное тестовое задание курса "Автоматизация тестирования" ##
# Функциональное тестирование сайта магазина "Линза UA"
Страница сайта интернет-магазина: https://linza.com.ua/
## Вступление.
Этот репозиторий содержит автотесты сайта интернет-магазина оптики и контактных линз "Линза UA".    
Тесты выполнены с применением PageObject и фреймворков Pytest и Selenium.    
Тесты, кроме ***test_crossbrowser.py*** запускаются в браузере Chrome.    
Для запуска ***test_crossbrowser.py*** необходимы браузеры Firefox, Edge, Opera, Safari. Версии браузеров и ссылки на скачивание находятся в ***browser_versions.txt***.    
Ссылка на описание тест-кейсов:    
https://docs.google.com/spreadsheets/d/1ZCOuL6OwdR9urhH52DM8sfgB9VsDuglPrcQqCuLsHMw/edit?usp=sharing
## Файлы.
В папке ***.tests*** находятся автотесты для тестируемых страниц магазина.    
В папке ***.pages*** находятся файлы с классами и методами для работы с соответствующими страницами сайта. Так же там находятся файлы с тестовыми данными, описаниями url сайта и вспомагательными методами.    
В папку ***.tests/screenshots*** сохраняются скриншоты, создающиеся при выполении тестов.    
Из папки ***.webdriver*** загружается веб-драйвер Chrome.    
## Как запускать тесты.
1. Установить зависимости:    
```
pip3 install -r requirements
```
2. Скачать Selenium WebDriver с https://chromedriver.chromium.org/downloads (выбрать версию, совместимую с вашим браузером) и скопировать в папку ***.webdriver***.
3. Запустить тесты можно:    
- из среды разработки (например, PyCharm) как отдельными тестами, так и одним файлом теста    
- из командной строки как файл теста, так и отдельный тест в файле:     
```
pytest -v <test_file_name>::<test_name>
```
- из командной строки тесты, помеченые соответствующим декоратором:     
```
pytest -v smoke (positive, negative, integration)
```
