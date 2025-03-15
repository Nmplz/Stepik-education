# _protected
# __private
class Clock:

    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if self.check_time(tm):
            self.__time = tm

    def check_time(self, time):
        if isinstance(time, int) and 0 <= time < 10**4:
            return True
        return False

    def get_time(self):
        return self.__time


clock = Clock(4530)
