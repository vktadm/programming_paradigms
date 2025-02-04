from random import randint, seed
from string import ascii_lowercase, ascii_uppercase


def gen_password(size):
    chars = ascii_lowercase + ascii_uppercase
    while True:
        yield ''.join([chars[randint(0, len(chars))] for _ in range(size)]) + '@mail.ru'


N = int(input())
seed(1)
gen = gen_password(N)
for _ in range(5):
    print(next(gen))
