class Point:
    "Класс для представления координат точки на плоскости."

    color = 'red'
    circle = 2

class Car:
    pass

if __name__ == '__main__':
    p = Point() # Экземпляр класса

    print(Point.__dict__) # Вывести все атрибуты класса
    print(p.__dict__) # Вывести атрибуты экземпляра класса >> {}

    print(type(p) == Point)
    print(isinstance(p, Point))

    p.color = 'green' # Локальный атрибут
    print(p.__dict__) # >> {'color': 'green'}

    p.quantity = 12 # Создать локальный атрибут
    print(p.__dict__) # >> {'color': 'green', 'quantity': 12}

    Point.type_pt = 'type 1' # Создать атрибут класса
    print(Point.__dict__['type_pt'])

    setattr(Point, 'new_atr', 'new value') # Добавить новый атрибут
    print(Point.new_atr)

    setattr(Point, 'type_pt', 'type 2') # Переопределить старый атрибут
    print(Point.type_pt)

    print(getattr(Point, 'not_existing_attr', False)) # return False
    print(getattr(p, 'new_atr', False)) # return 'new_value'

    del Point.new_atr # Удалить атрибут
    print(hasattr(Point, 'new_atr')) # Проверяет существует ли атрибут
    print(hasattr(p, 'circle')) # в том числе и в атрибутах родителя

    delattr(Point, 'type_pt')
    print(hasattr(Point, 'type_pt'))  # Вернет False

    del p.color
    print(p.color) # Выведет атрибут Point

    print(Point.__doc__["color"])