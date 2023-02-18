class RenderDigit:
    def __call__(self, value):
        try:
            return int(value)
        except:
            return None

class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return [self.render(i) for i in func().split()]
        return wrapper


@InputValues(render=RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)