def id_even(num):
    return num % 2


lst = [4, 5, -7, -34, 10, 2, -8, -9, 3]
# sort_lst = sorted(lst, key=id_even)
sort_lst = sorted(lst, key=lambda num: num % 2)
print(sort_lst)


