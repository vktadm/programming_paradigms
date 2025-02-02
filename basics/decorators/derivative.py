from functools import wraps
import math


# Декоратор функции с параметром
def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func) # сохранение параметров передаваемой функции
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, *kwargs) - func(x, *args, *kwargs)) / dx
            return res

        # wrapper.__doc__ = func.__doc__ # сохраняем описания функции при декорировании
        # wrapper.__name__ = func.__name__  # сохраняем имя функции при декорировании
        return wrapper

    return func_decorator


@df_decorator(dx=0.000001)
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


if __name__ == '__main__':
    df = sin_df(math.pi / 3)
    print(df)

    print(sin_df.__name__)  # не сохраняет имя "sin_df"
    print(sin_df.__doc__)
