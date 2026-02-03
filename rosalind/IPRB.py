k, m, n = 30, 26, 26
t = k + m + n

# m + n
p_mn = (m / t) * (n / (t-1)) * 0.5
p_nm = (n / t) * (m / (t-1)) * 0.5

# m + m
p_mm = (m / t) * ((m-1) / (t-1)) * 0.25

# n + n
p_nn = (n / t) * ((n-1) / (t-1))

p = 1 - p_mn - p_nm - p_mm - p_nn
print(f"{p:.5f}")