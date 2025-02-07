# s_lst = input().split()
s_lst = 'house=дом car=машина men=человек tree=дерево'.split()
tp = tuple(map(lambda itm: tuple(itm.split('=')), s_lst))
print(tp)
