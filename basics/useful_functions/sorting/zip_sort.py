t1 = tuple(map(int, input().split()))
t2 = tuple(map(int, input().split()))

print(*map(sum, zip(sorted(t1), sorted(t2, reverse=True))))
