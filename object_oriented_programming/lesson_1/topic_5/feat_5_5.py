class Graph:

    def __init__(self, data, is_show=True):
        self.data = data[:] # Копирует список
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if not self.is_show:
            print("Отображение данных закрыто")
            return
        print(' '.join(self.data))

    def show_graph(self):
        if not self.is_show:
            print("Отображение данных закрыто")
            return
        print(f'Графическое отображение данных: {" ".join(map(str, self.data))}')

    def show_bar(self):
        if not self.is_show:
            print("Отображение данных закрыто")
            return
        print(f'Столбчатая диаграмма: {" ".join(map(str, self.data))}')

    def set_show(self, fl_show):
        self.is_show = fl_show

if __name__ == '__main__':
    data = list(map(int, '8 11 10 -32 0 7 18'.split(' ')))

    gr = Graph(data)
    gr.show_bar()
    gr.set_show(False)
    gr.show_table()

