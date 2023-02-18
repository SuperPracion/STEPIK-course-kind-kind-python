class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        if  'method' not in request or request['method'] == 'GET':
            return f"GET: {self.func(0)}"
        else:
            return None


@HandlerGET
def index(request):
    return "главная страница сайта"

res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"
#
res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"