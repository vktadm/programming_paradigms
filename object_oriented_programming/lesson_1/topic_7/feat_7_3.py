from re import fullmatch
from string import ascii_lowercase


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper()

    @staticmethod
    def check_card_number(number):
        # XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)
        return bool(fullmatch(r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}', number))

    @classmethod
    def check_name(cls, name):
        return len(name.split()) == 2 and all([symbol in cls.CHARS_FOR_NAME + ' ' for symbol in name])


is_number = CardCheck.check_card_number("1244-5678-9012-0000-5643")
is_name = CardCheck.check_name("SERGEI BAL*AKIREV")

print(is_number, is_name)
