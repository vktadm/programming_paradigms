import sys


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = 'зонт=1000 палатка=10000 спички=22 котелок=543'

t = [tuple(line.split('=')) for line in lst_in.split()]
print(*map(lambda itm: itm[0], filter(lambda itm: int(itm[1]) > 500, t)))
# print(t)
# print(*filter(
#     lambda weight: weight < 500, map(lambda itm:
#                                      tuple(itm.split('='), l)))