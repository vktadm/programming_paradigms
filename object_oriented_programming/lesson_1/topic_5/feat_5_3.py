import random as rnd

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

if __name__ == '__main__':
    class_list = [Line, Rect, Ellipse]

    elements = [rnd.choice(class_list)(*[rnd.randint(0, 10) for _ in range(4)]) for _ in range(217)]

    for element in elements:
        if isinstance(element, Line):
            element.sp = element.ep = (0, 0)
    print(elements)