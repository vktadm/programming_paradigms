def is_string(lst):
    return all(map(lambda line: isinstance(line, str), lst))


print(is_string(['h', 'djsj', 1]))
