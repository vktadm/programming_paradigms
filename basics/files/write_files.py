try:
    with open('out.txt', 'a+') as file:
        file.write('Hello!\n')
        file.writelines(['How are you?\n', 'Hello!\n'])
        file.seek(0)
        data = file.readlines()
        print(data)
except:
    print('Ошибка при работе с файлом!')
