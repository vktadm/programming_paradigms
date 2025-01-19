def loop_brk():
    max_val = 10
    i = 0

    print('Для завершения введите "q"')
    while i <= max_val:
        s = input('Введите любой символ: ')
        if s == "q":
            break
        i += 1
    else:
        print('Цикл завершился в штатном режиме!')

if __name__ == '__main__':
    loop_brk()