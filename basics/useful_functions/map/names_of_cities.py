print(*map(lambda name: name if len(name) > 5 else '-', input().split()), sep=' ')
print(*map(lambda x: ('-', x)[len(x) > 5], input().split()))
