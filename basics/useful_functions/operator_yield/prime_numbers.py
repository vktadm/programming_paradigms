def is_prime(value):
    if value <= 1:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True


def gen_prime(N):
    num = 2
    counter = 1
    while counter <= N:
        if is_prime(num):
            yield num
            counter += 1
        num += 1


N = 20
print(*gen_prime(N))
