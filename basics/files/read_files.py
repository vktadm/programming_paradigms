file = open('file.txt')
encode_file = open('encode_file.txt', encoding='Windows-1251')

print('---- Simple file----')
print(file.read(10))  # максимальное кол-во символов для чтения
print(f'Файловая позиция - {file.tell()}')
print(file.read(10))  # следующие 10 символов
file.seek(0)
print(file.read(5))

print('\n----Decode file----')
print(encode_file.read())

print('\n----Построчное чтение----')
file.seek(0)
print(file.readline(), end='')

print(file.readlines())

file.close()