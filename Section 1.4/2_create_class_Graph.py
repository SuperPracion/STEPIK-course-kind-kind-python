class Graph:
    LIMIT_Y = [0, 10] #floor and ceilil

    def set_data(self, data):
        self.data = data

    def draw(self):
        floor, ceil = Graph.LIMIT_Y
        print(*filter(lambda x: floor <= x <= ceil, self.data))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()