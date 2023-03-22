class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if not self.min_length <= len(string) or not len(string) <= self.max_length:
            raise ValueError('недопустимая строка')
        if self.chars:
            if not any(chr in self.chars for chr in string):
                raise ValueError('недопустимая строка')

        return string


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self.login = None
        self._password = None

    def form(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')
        
        self._login = self.login_validator.is_valid(request['login'])
        self._password = self.password_validator.is_valid(request['password'])