class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda side: type(side) in (int, float), [self.a, self.b, self.c])):
            return 1
        elif not all(map(lambda side: side > 0, [self.a, self.b, self.c])):
            return 1
        elif (self.a >= self.b + self.c) or (self.b >= self.c + self.a) or (self.c >= self.a + self.b):
            return 2
        else:
            return 3

if __name__ == '__main__':
    a, b, c = 5, 5, 10

    tr = TriangleChecker(a, b, c)
    print(tr.is_triangle())