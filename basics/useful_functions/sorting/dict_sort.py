def str_to_tuple(s):
    value, key = s.split(':')
    return int(key), value


lst_in = [
    'смартфон:120000',
    'яблоко:2',
    'сумка:560',
    'брюки:2500',
    'линейка:10',
    'бумага:500'
]

lst = dict(sorted(map(str_to_tuple, lst_in))[0:3])
print(*lst.values())
