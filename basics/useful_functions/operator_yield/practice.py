def get_sum(total):
    for number in range(1, total):
        numbers = range(1, number + 1)
        yield sum(numbers)


def balak_seq(max_len):
    a, b, c = 1, 1, 1
    for _ in range(max_len):
        yield a
        a, b, c = b, c, sum([a, b, c])


N = int(input())

# gen = get_sum(N + 1)
# print(list(gen))

print(*balak_seq(N))
