n, k = 29, 3

f1, f2 = 1, 1
for i in range(3, n + 1):
    f1, f2 = f2, f2 + f1 * k
print(f2)