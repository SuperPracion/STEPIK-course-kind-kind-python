import re

def check_email(email):
    if __is_email_str(email):
        return bool(re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email))
    else:
        return False

def __is_email_str(email):
    return isinstance(email, str)

print(check_email('sc_lib@list.ru'))