def str_to_dict():
    lst_in = 'one=1 two=2 three=3'

    d = list(map(lambda item: item.split('='), lst_in.split()))
    d = dict([key, int(value)] for key, value in d)
    print(d)

def phone_numbers():
    pn = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'.split()

    d = dict.fromkeys([key[0:2] for key in pn], [])
    # d = {key[0:2]: [] for key in pn}

    [d[value[0:2]].append(value) for value in pn]

    print(d)

def frkeys():
    lst = ['+7', '+6', '+5', '+2']

    d = dict.fromkeys(lst, [])

if __name__ == '__main__':
    # str_to_dict()
    phone_numbers()