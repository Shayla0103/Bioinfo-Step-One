"""g1 = {"AABB": 1/16, "AABb": 2/16, "AAbb": 1/16,
      "AaBB": 2/16, "AaBb": 4/16, "Aabb": 2/16,
      "aaBB": 1/16, "aaBb": 2/16, "aabb": 1/16
    }
p = {"Aa": {'AA': 1/4, 'Aa': 2/4, 'aa': 1/4},  # Aa*Aa后代概率
     "AA": {'AA': 1/2, 'Aa': 1/2},  # AA*Aa后代概率
     "aa": {'Aa': 1/2, 'aa': 1/2}  # aa*Aa后代概率#
     }
# 发现，无论亲本基因是AA, Aa, aa中的哪一个，只要与Aa杂交，后代中Aa的概率就是0.5，因此AaBb就是0.25
"""

import math


def independent_alleles(k, n_target):
    # 总人口数 n = 2^k
    total_population = 2 ** k
    p = 0.25

    prob_at_least_n = 0

    # 累加从 N 到 total_population 的所有概率
    for i in range(n_target, total_population + 1):
        # 二项分布公式: C(n, i) * p^i * (1-p)^(n-i)
        combination = math.comb(total_population, i)
        probability = combination * (p ** i) * ((1 - p) ** (total_population - i))
        prob_at_least_n += probability

    return round(prob_at_least_n, 3)


# 示例输入: k=2, N=1
# 预期输出: 0.684
print(independent_alleles(5, 7))
