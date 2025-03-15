class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:

    def __init__(self):
        self.rating = 0

    @staticmethod
    def raiting_check(rating):
        if not 0 <= rating <= 5:
            raise ValueError("неверное присваиваемое значение")

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.raiting_check(value)
        self.__rating = value
