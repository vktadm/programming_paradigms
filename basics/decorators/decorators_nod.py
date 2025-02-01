import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        func_result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Время выполнения - {dt}')
        return func_result

    return wrapper


@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_nod_fast(a, b):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    nod1 = get_nod(2, 1000000)
    nod2 = get_nod_fast(2, 1000000)
    print(nod1, nod2)
