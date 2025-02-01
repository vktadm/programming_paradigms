def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    return step


if __name__ == '__main__':
    c1 = counter()
    c2 = counter(10)

    print(c1(), c2())
    print(c1(), c2())
    print(c1(), c2())
    print(c1(), c2())