import datetime as dt
from functools import reduce


def task1():
    """
    Функция, вычисляющая произведения эл-в массива.
    """
    return reduce(lambda x, y: x * y, list(map(int, input('Введите список целых чисел: ').split(' '))))


def task2(unsorted_dict):
    """
    Сортировка словаря в алфавитном порядке.
    """
    # return dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
    return dict(sorted(zip(unsorted_dict.values(), unsorted_dict.keys())))


def task3(values):
    """
    Возвращает слова, состоящие из 5 букв, отсортированные в алфавитном порядке.
    """
    return list(sorted(filter(lambda value: len(value) == 5, values)))


def task4():
    """
    Возвращает текущую дату.
    """
    current_date = dt.datetime.now()
    # print(current_date.day, current_date.month, current_date.year)
    return f'День: {current_date.day}\nМесяц: {current_date.month}\nГод: {current_date.year}'


def task5():
    """
    Возвращает последовательность Фибоначи.
    """
    quantity = int(input('Введите кол-во чисел Фибоначи для вывода: '))
    fibonacci = lambda n: reduce(lambda x, n: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
    return fibonacci(quantity)


def task6():
    """
    Возвращает пересечения строк.
    """
    # todo:
    values1 = [3, 6, 7, 8, 9, 2, 1, 0, 12, 45]
    values2 = [7, 9, 0, 12, 15, 5, 6, 11, 43]

    return list(filter(lambda x: x in values2, values1))


def task7():
    """
    Сортировка.
    """
    values = [-6, -1, 3, -5, -15, 4, 1, 9, 8, 6, -3, -4, 12, -10, 7]
    return sorted(values, key=lambda i: 0 if i == 0 else -1 / i)


def task8():
    """
    Суммирование 2-х списков.
    """
    values1 = [7, 2, 3, -5, 6, 7, 0, 1, 12, 45, 9, 33]
    values2 = [32, 87, 12, -2, 4, 7, 1, 3, 9, 2, 4, 2]

    return list(map(lambda value1, value2: value1 + value2, values1, values2))


def task9():
    """
    Находит все анаграммы слова в строке.
    """
    values = ["каприз", "клоун", "колба", "колун", "крона", "уклон", "колыбель", "карта"]
    target = "кулон"

    return list(filter(lambda x: (set(target) == set(x)), values))


def check_password(passw):
    res_dict = [
        lambda passw: any(x.isupper() for x in passw) or '\nВ пароле должна быть хотя бы одна буква в верхнем регистре',
        lambda passw: any(x.islower() for x in passw) or '\nВ пароле должна быть хотя бы одна буква в нижнем регистре ',
        lambda passw: any(x.isdigit() for x in passw) or '\nВ пароле должна быть хотя бы одна цифра',
        lambda passw: any(
            x in '!@#$%^&*()-+' for x in passw) or '\nПароль должен содержать один из спецсимволов !@#$%^&*()-+',
        lambda passw: len(passw) >= 9 or '\nПароль должен содержать не менее 9 символов']

    result = [x for x in [i(passw) for i in res_dict] if x != True]

    if not result:
        result.append('Надежный пароль')
    return result


st = input('Введите пароль для проверки: ')
print(*check_password(st))
# print(task1())
# unsorted_dict = {'фрукт': 'яблоко', 'цвет': 'антрацит', 'артикул': 'в5678',
#                  'модель': 'бабочка', 'наименование': 'книга', 'жанр': 'триллер'}
# print(task2(unsorted_dict))

# values = ['физалис', 'груша', 'слива', 'арбуз',
#           'банан', 'апельсин', 'яблоко', 'папайя']
#
# print(task3(values))
# print(task4())
# print(*task5())
# print(*task6())
# print(*task7())
# print(*task8())
# print(*task9())
