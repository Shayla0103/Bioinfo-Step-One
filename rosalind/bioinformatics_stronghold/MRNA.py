"""
1. 简并性：在蛋白质翻译过程中，大多数氨基酸可以由多个不同的密码子（Codons）编码。
例如，甲硫氨酸（M）只有一个密码子（AUG），但亮氨酸（L）有 6 个不同的密码子。
2. 终止密码子（Stop Codon）：每一个 mRNA 序列的末尾必须有一个终止密码子。
在标准遗传密码表中，终止密码子共有 3 种（UAG, UGA, UAA）。
3. 乘法原理：要计算有多少种可能的 mRNA，只需将蛋白质序列中每个氨基酸对应的密码子数量相乘，
最后再乘以终止密码子的数量（3）。
4. 取模运算：由于结果会非常巨大，题目要求输出结果对 1,000,000 取模（Modulo 1,000,000）。
在 Python 中，我们可以在每一步相乘后取模，防止数字过大。
"""


def solve_mrna(protein_seq):
    # 建立氨基酸到其密码子数量的映射字典
    codon_counts = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1,
        'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1,
        'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2,
        'E': 2, 'G': 4
    }

    modulo = 1000000

    # 初始可能数设为 3（因为末尾必有一个终止密码子，共有3种可能）
    total_possibilities = 3

    # 遍历蛋白质序列，依次相乘
    for aa in protein_seq:
        if aa in codon_counts:
            total_possibilities *= codon_counts[aa]
            # 每一步都取模，保持数字在合理范围内
            total_possibilities %= modulo

    return total_possibilities


# 读取文件数据
with open("rosalind_mrna.txt", "r") as f:
    protein_sequence = f.read().strip()

result = solve_mrna(protein_sequence)
print(result)
