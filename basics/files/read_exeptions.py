try:
    with open('file.txt', encoding='utf-8') as file:
        data = file.readlines()
        # int(data)
        print(data)
except FileNotFoundError:
    print('Невозможно прочитать файл!')
except:
    print('Ошибка при работе с файлом!')
finally:
    print(file.closed)
