TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = DialogWindows() if TYPE_OS == 1 else DialogLinux()
        setattr(obj, 'name', *args)
        return obj

dlg = Dialog('name')




TYPE_OS = 1
dlg_1 = Dialog("123")
TYPE_OS = 2
dlg_2 = Dialog("1234")

assert isinstance(dlg_1, DialogWindows) and isinstance(dlg_2, DialogLinux), "создаваемые объекты не соответствуют нужным классам DialogWindows или DialogLinux"

assert dlg_1.name == "123", "неверное значение локального атрибута name класса DialogWindows"
assert dlg_2.name == "1234", "неверное значение локального атрибута name класса DialogLinux"

d1 = Dialog("12")
d2 = Dialog("123")

assert d1.name == "12" and d2.name == "123", "неверные значения в локальных атрибутах name разных объектов класса DialogLinux"
