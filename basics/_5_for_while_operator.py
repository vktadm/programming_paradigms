from math import log

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

def sum_lists():
    a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]

    rez = []

    for i, row in enumerate(a):
        r = []
        for j, value in enumerate(row):
            r.append(value + b[i][j])
        rez.append(r)

    print(rez)

def row_to_column():
    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    """
    Before:
        1	2	3	4	
        5	6	7	8	
        9	10	11	12	
        13	14	15	16	
    After:
        1	5	9	13	
        2	6	10	14	
        3	7	11	15	
        4	8	12	16
    """
    print('Before:')
    for r in A:
        for x in r:
            print(x, end='\t')
        print()

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    print('After:')
    for r in A:
        for x in r:
            print(x, end='\t')
        print()

def pascal_triangle():
    n = 6 # Кол-во строк в треугольнике

    p = [[1] * (i + 1) for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if j != 0 and j != i:
                p[i][j] = p[i - 1][j - 1] + p[i - 1][j]

    for i in range(n):
        print(' ' * (n - i), end='')
        for j in range(i + 1):
            print(str(p[i][j]), end=' ')
        print()

def two_to_one_list():
    lst_in = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 8, 7, 6],
              [5, 4, 3, 2]]

    res_list = [value for row in reversed(lst_in) for value in reversed(row)]

    print(' '.join(map(str, res_list)))

def lst_to_matrix():
    lst = '1 2 3 4 5 6'.split()

    l = int(log(len(lst), 2))
    res_matrix = [[lst[j] for j in range(i * l, i * l + l)] for i in range(l)]

    print(res_matrix)

def poem():
    t = ["– Скажи-ка, дядя, ведь не даром",
         "Я Python выучил с каналом",
         "Балакирев что раздавал?",
         "Ведь были ж заданья боевые,",
         "Да, говорят, еще какие!",
         "Недаром помнит вся Россия",
         "Как мы рубили их тогда!"
         ]

    rez_t = [[word for word in row.split() if len(word) > 3 ] for row in t]
    print(rez_t)


if __name__ == '__main__':
    # while_operator_1()
    # while_operator_2()
    # sum_lists()
    # row_to_column()
    # pascal_triangle()
    # two_to_one_list()
    # lst_to_matrix()
    poem()