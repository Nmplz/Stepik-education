class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        a, b = self.LIMIT_Y
        # print(' '.join(str(x) for x in self.data  if x in range(min(self.LIMIT_Y), max(self.LIMIT_Y)+1)))
        print(*filter(lambda x: a <= x <= b, self.data))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
