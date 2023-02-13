import re
import random
import string


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        words = string.ascii_letters + string.digits
        while True:
            email = f"{''.join(random.choices(words, k=random.randint(1, 100)))}@gmail.com"
            if cls.check_email(email):
                break
        return email


    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email) and '@' in email and email.count('@') == 1:
            left, right = email.split('@')
            return (email.count('..') == 0 and right.count('.') >= 1 and
                    len(right) <= 50 and len(left) <= 100 and
                    bool(re.match(r'^[a-zA-Z\.\_]+\@[a-zA-Z\.\_]+$', email)))
        else:
            return False

    @classmethod
    def __is_email_str(cls, email):
        return isinstance(email, str)
