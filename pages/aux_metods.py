from random import choice
from string import ascii_letters, digits

class AuxMetods:
    """Класс вспомагательные методы, используемые в параметризации поиска, для добавления различных строк"""

    def generate_string(n: int) -> str:
        return "x" * n

    def russian_chars() -> str:
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def english_chars() -> str:
        return 'abcdefghijklmnopqrstuvwxyz'

    def random_chars(length: int) -> str:
        random_str = ''.join(choice(ascii_letters) for i in range(length))
        return random_str

    def random_num(length: int) -> int:
        random_int = int(''.join(choice(digits) for i in range(length)))
        return random_int

    def random_phone(length: int) -> str:
        rand_phone = f"73{''.join(choice(digits) for i in range(length-2))}"
        return rand_phone

    def chinese_chars() -> str:
        return '的一是不了人我在有他这为之大来以个中上们'

    def special_chars() -> str:
        return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


