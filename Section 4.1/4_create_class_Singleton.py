class Singleton:
    main = None

    def __new__(cls, *args, **kwargs):
        if cls.main is None:
            Singleton.main = super().__new__(cls)

        return cls.main


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


game = Game('!')
print(id(game))
game1 = Game('2')
print(id(game1))
