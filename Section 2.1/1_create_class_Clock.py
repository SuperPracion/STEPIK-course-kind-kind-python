class Clock:
    def __init__(self, time):
        self.set_time(time)

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    def __check_time(self, tm):
        return type(tm) == int and 0 <= tm < 100_000


clock = Clock(4530)
print(clock.get_time())