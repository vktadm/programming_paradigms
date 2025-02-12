import random as rd

rd.seed(1)
lst = [rd.randint(-5, 5) for _ in range(10)]

print(lst)