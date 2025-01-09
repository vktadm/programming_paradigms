class Point:
    "Класс для представления координат точки на плоскости."
    color = 'red'
    circle = 2

    def set_coords_wrong():
        """Не будет вызываться из экземпляров класса"""
        print("Вызов метода set_coords")

    def set_coords(self):
        """Доступен для вызова из экземпляров класса"""
        print("Вызов метода set_coords " + str(self))
        # Адрес self будет совпадать с адресом экземпляра класса

    def set_coordinates(self, x, y):
        # Создаются локальные атрибуты
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

if __name__ == '__main__':
    print(Point.set_coords_wrong) # Вывод значения атрибута
    # >> <function Point.set_coords at 0x10074dc60>
    Point.set_coords_wrong() # Вызов ф-ии, ошибки не возникнет

    pt = Point()
    print(pt.set_coords_wrong) # Вывод значения атрибута
    # >> <bound method Point.set_coords of <__main__.Point object at 0x1033aca70>>

    pt.set_coords()  # Выполниться

    # pt.set_coords_wrong() # Вызывает ошибку, тк в качестве аргумента передается self,
    # а в объявлении функции отсутствует self

    # Point.set_coords() # Вызовет ошибку, тк не передается аргумент self
    Point.set_coords(pt) # Будет работать

    pt.set_coordinates(2, 10)
    print(*pt.__dict__)

    print(pt.get_coordinates())

    f = getattr(pt, 'get_coordinates') # Можем присвоить функцию, тк методы класса = атрибуты класса
    # ссылается не на данные, а на функцию
    print(f())