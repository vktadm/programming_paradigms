class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        # for item in self.data:
        #     if item >= self.LIMIT_Y[0] and item <= self.LIMIT_Y[1]:
        #         result.append(item)
        # print(" ".join(map(str, result)))
        print(*filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1], self.data))

if __name__ == '__main__':
    graph_1 = Graph()
    graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])

    graph_1.draw()