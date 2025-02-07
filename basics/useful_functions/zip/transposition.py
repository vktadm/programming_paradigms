lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']

print(*(' '.join(line) for line in zip(*map(str.split, lst_in))), sep='\n')
