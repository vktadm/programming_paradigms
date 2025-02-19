class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # равнозначно строке ниже, но не рекомендуется использовать
        # if Vector.validate(x) and Vector.validate(y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(-1, 2)
res = Vector.get_coord(v)
print(res)

print(Vector.validate(5))

print(Vector.norm2(6, 9))
