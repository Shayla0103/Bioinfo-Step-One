def solve_pper(n, k):
    m = 1000000
    result = 1
    for i in range(k):
        # 从 n, n-1, n-2... 一直乘 k 次
        result = (result * (n - i)) % m
    return result


print(solve_pper(90, 8))
