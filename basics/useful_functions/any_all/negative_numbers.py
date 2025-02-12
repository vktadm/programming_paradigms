lst_in = [2, 4, 6, 8, 22, -56]
# lst_in = list(map(int, input().split()))

print(any(map(lambda num: num <= 0, lst_in)))