import sys


# def to_tuple(line):
#     t = line.split(';')
#     if t[0].isdigit() and t[2].isdigit():
#         return int(t[0]), t[1], int(t[2]), t[3]
#     return tuple(t)
#

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ["Номер;Имя;Оценка;Зачет", "1;Портос;5;Да", "2;Арамис;3;Да", "3;Атос;4;Да", "4;д'Артаньян;2;Нет", "5;Балакирев;1;Нет"]
colums = 'Имя;Зачет;Оценка;Номер'

t = tuple(tuple(int(value) if value.isdigit() else value for value in row.split(";")) for row in lst_in)
t_sorted = tuple(zip(*sorted(zip(*t), key=lambda line: colums.find(line[0]))))
print(*t_sorted)
