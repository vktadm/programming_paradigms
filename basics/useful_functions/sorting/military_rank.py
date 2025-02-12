import sys


rank = 'рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник'

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ["Атос=лейтенант", "Портос=прапорщик", "д'Артаньян=капитан", "Арамис=лейтенант", "Балакирев=рядовой"]

lst = map(lambda line: line.split('='), [line for line in lst_in])
lst = sorted(lst, key=lambda line: rank.find(line[1]))
# print(*lst)
