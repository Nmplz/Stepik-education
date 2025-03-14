# здесь объявляются все необходимые классы

# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))


# здесь создаются объекты классов и вызываются нужные методы
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data.copy()
        self.is_show = is_show

    def check_show(func):
        def wrapper(self):
            if not self.is_show:
                return "Отображение данных закрыто"
            else:
                return func(self)

        return wrapper

    def set_data(self, data):
        self.data = data.copy()

    @check_show
    def show_table(self):
        return " ".join(map(str, self.data))

    @check_show
    def show_graph(self):

        print(f"Графическое отображение данных: {self.show_table()}")

    @check_show
    def show_bar(self):
        print(f"Столбчатая диаграмма: {self.show_table()}")

    def set_show(self, fl_show):
        self.is_show = fl_show


gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
print(gr.show_table())
