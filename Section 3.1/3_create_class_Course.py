class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title='', practices=0, duration=0):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in ('practices', 'duration') and type(value) == int and value > 0:
            object.__setattr__(self, key, value)
        elif key == 'title' and type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in ('title', 'practices', 'duration'):
            object.__delattr__(self, item)
