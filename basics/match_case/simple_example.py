def ex1():
    cmd = 'bottom'

    match cmd:
        case 'top' | 'bottom':
            print('Вверх или вниз')
        case 'lift':
            print('Влево')
        case 'right':
            print('Вправо')
        case _:
            print('Другое')

    print('Процессы завершены')


def ex2():
    cmd = 'top'

    match cmd:
        case 'top':
            print('Вверх')
        case command:
            # создает переменную и ссылается на значение cmd
            # command = cmd
            # отрабатывает всегда
            # все другие блоки case игнорируются
            print(f'команда: {command}')

    print('Процессы завершены')


def ex3():
    cmd = 'left'

    match cmd:
        case 'top':
            print('Вверх')
        case _: # wildcard
            print(f'Другая команда')

    print('Процессы завершены')


def ex4():
    cmd = 'Строка'

    match cmd:
        # case str() as command:
        case str(command):
            print(f'Переменная {command} является str')
        case _: # wildcard
            print(f'Другой тип')

    print('Процессы завершены')


def ex5():
    """Проверка типов данных с учетом наследования"""
    cmd = 5

    match cmd:
        case str():
            print('Строка')
        case bool():
            print('Булево значение')
        case int() as command if 0 <= command < 10:
            print('Целочисленный тип')
        case float():
            print('Значение с плавающей точкой')

    print('Процесс закончен')


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    ex5()
