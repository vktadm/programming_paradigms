def is_prime(x):
    d = x - 1
    if d < 0:
        return False

    while d > 1:
        if x % d == 0:
            return False
        d -= 1

    return True


nums = [i for i in range(30)]
print(*filter(is_prime, nums))
