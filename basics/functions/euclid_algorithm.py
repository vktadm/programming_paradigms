from time import time


def get_nod(a, b):
    """Вычисляется НОД для двух натуральных чисел a b b
    по алгоритму Евклида.

    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """

    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

def test_node(func):
    # --- Тест №1 --------------
    a, b = 28, 35

    result = func(a, b)
    if result == 7:
        print('#test1 - ok')
    else:
        print('#test1 - fail')

    # --- Тест №2 --------------
    a, b = 100, 1

    result = func(a, b)
    if result == 1:
        print('#test2 - ok')
    else:
        print('#test2 - fail')

    # --- Тест №3 --------------
    a, b = 2, 100000000

    start = time()
    result = func(a, b)
    end = time()

    dt = end - start

    if result == 2 and dt < 1:
        print('#test3 - ok')
    else:
        print('#test3 - fail')

test_node(get_nod)