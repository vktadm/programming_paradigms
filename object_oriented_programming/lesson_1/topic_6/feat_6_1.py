class SingletonFive:
    __instance = None
    quantity = 0

    def __new__(cls, *args, **kwargs):
        if cls.quantity < 5:
            cls.__instance = super().__new__(cls)
            cls.quantity += 1
        return cls.__instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    objs = [SingletonFive(str(n)) for n in range(10)]
    print(objs)
