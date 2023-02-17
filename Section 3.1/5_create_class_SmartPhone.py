class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if type(app) not in [type(application) for application in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self, name='ВКонтакте'):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max=1024, name='YouTube'):
        self.name = name
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list: dict, name='Phone'):
        self.name = name
        self.phone_list = dict


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
ph = AppPhone({"Балакирев": 1234567890, "Работа": 112})
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
