class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Удаление объекта {str(self)}')

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

if __name__ == '__main__':
    point = Point(3, 5)
    point_2 = Point()
    point_2 = 0
    point.set_coords(10, 20)
    print(point.get_coords())