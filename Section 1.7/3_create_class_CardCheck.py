import re
from string import ascii_lowercase, digits

class CardCheck:
    @staticmethod
    def check_card_number(number):
        return bool(re.match(r'^(\d{4}-?){4}$', number))

    @staticmethod
    def check_name(name):
        return bool(re.match(r'^[A-Z]*\ [A-Z]*$', name))

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")