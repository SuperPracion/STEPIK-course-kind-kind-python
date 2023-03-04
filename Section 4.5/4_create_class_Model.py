from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    unoque_id = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__gen_unique_id()

    def get_pk(self):
        return self._id

    @classmethod
    def __gen_unique_id(cls):
        ModelForm.unoque_id += 1
        return cls.unoque_id

form = ModelForm("Логин", "Пароль")
print(form.get_pk())