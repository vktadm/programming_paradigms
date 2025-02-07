a = [i for i in range(1, 5)]
b = [i for i in range(5, 11)]
s = 'python'

z = zip(a, b, s)
t1, t2, t3 = zip()
# t1, t2, t3 = zip(*z)
print(t1, t2, t3, sep='\n')