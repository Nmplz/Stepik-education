class WordString:
    def __init__(self, string=""):
        self.__string = string

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, indx):
        if indx < len(self.__string):
            return self.__string.split()[indx]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, input_str):
        if isinstance(input_str, str):
            self.__string = input_str
