lst_in = [line.split() for line in ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']]
print(*(' '.join(line) for line in zip(*zip(*lst_in))), sep='\n')
# print(*zip())
