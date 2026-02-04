n, m = 82, 19

# 初始状态：第1个月只有1对刚出生的兔子
# 列表长度为 m，代表 m 个年龄等级
ages = [0] * m
ages[0] = 1

for month in range(1, n):
    # 1. 算出这个月谁能生崽：除了 ages[0] 以外的所有兔子都是成熟的
    new_born = sum(ages[1:])

    # 2. 兔子变老：从 m-1 岁到 1 岁依次往后挪一个位置（逆序更新，防止数据覆盖）
    # 注意：原本在 ages[m-1] 的兔子因为寿命到了，直接消失（死亡）
    for j in range(m - 1, 0, -1):
        ages[j] = ages[j - 1]

    # 3. 刚出生的宝宝填入 ages[0]
    ages[0] = new_born

# 第 n 个月结束后的总数就是所有年龄段之和
print(sum(ages))


