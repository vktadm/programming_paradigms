import re

def while_operator_1():
    slags = ['osnovnye--metody-----slovarey',
             'peremennyye-operator----prisvaivaniya--tipy---dannykh',
             'funkciya------enumerate--primery---ispolzovaniya'
             ]

    for slag in slags:
        while '--' in slag:
            slag = slag.replace('--', '-')
        print(slag)

def while_operator_2():
    n = 0
    while n <= 2 or type(n) != int:
        n = int(input('Введите N > 2: '))

    rez = [1, 1]
    i = 2

    while i <= n:
        rez.append(rez[i - 2] + rez[i - 1])
        i += 1

    print(' '.join(map(str, rez)))

if __name__ == '__main__':
    while_operator_1()
    while_operator_2()
