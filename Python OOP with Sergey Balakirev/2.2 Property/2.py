class WindowDlg:
    def __init__(self, tilte, width, height):
        self.__title = tilte
        self.__width = width
        self.__height = height

    def show(self):
        return print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if 0 < width < 10 * 3:
            self.__width = width
        self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if 0 < height < 10 * 3:
            self.__height = height
        self.show()
