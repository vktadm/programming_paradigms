def get_list():
    """Вычисляет среднее арифметическое для последовательности."""
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)


a = get_list()
print(list(a))