import math

NAME = 'mymodule'


def floor(x):
    print('Функция из модуля mymodule')
    return x


print(NAME)
print(__name__) # mymodule
