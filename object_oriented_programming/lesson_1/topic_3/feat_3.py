class Figure:
    type_fig = 'ellipse'
    color = 'red'

class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

def ex_1():
    """Выводит все локальные атрибуты"""
    fig1 = Figure()

    fig1.start_pt = (10, 5)
    fig1.end_pt = (100, 20)
    fig1.color = 'blue'

    delattr(fig1, 'color')

    print(*fig1.__dict__)

def ex_2():
    """Существует ли локальное свойство с именем job"""
    p1 = Person()
    print(hasattr(p1.__dict__, 'job'))

if __name__ == '__main__':
    ex_1()
    ex_2()