import random


class AuxMetods:
    """Класс вспомагательные медоты, используемые в параметризации поиска, для добавления различных строк"""

    def generate_number(n: int):
        return random.randint(10, n) * n // 10

    def generate_string(n: int):
        return "x" * n

    def russian_chars():
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def chinese_chars():
        return '的一是不了人我在有他这为之大来以个中上们'

    def special_chars():
        return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


