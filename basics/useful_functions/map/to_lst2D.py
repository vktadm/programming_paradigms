import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['1 2 3 4', '5 6 7 8', '9 10 11 12']

lst2D = [list(map(int, line.split())) for line in lst_in]
print(lst2D)
