lst_in = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'.split()

n = int(len(lst_in) ** 0.5)
l = len(lst_in)

matrix = (lst_in[i:i + n] for i in range(0, l - n, n))
[print(*line) for line in matrix]

print('----Other solve----')

s = iter(lst_in)
print(*[' '.join(x) for x in zip(s, s, s)], sep='\n')
