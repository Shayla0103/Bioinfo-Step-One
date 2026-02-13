from Bio import SeqIO

# 记忆化字典，用于存储已计算过的子序列结果
memo = {}


def count_noncrossing_matchings(s):
    # 基本情况：空序列有一种匹配方式（即什么都不做）
    if len(s) == 0:
        return 1
    # 如果序列长度为奇数，不可能有完美匹配
    if len(s) % 2 != 0:
        return 0
    # 如果已经计算过，直接返回
    if s in memo:
        return memo[s]

    first = s[0]
    total = 0

    # 尝试将第一个碱基 s[0] 与每一个可能的 s[k] 配对
    # k 必须是奇数索引（1, 3, 5...），这样两边剩下的序列长度才是偶数
    for k in range(1, len(s), 2):
        current = s[k]

        # 检查是否可以配对
        if sorted([first, current]) in [['A', 'U'], ['C', 'G']]:
            # 分割成两部分
            left_part = s[1:k]
            right_part = s[k + 1:]

            # 检查左半部分的碱基组成是否平衡（A=U, G=C）
            if left_part.count('A') == left_part.count('U') and \
                    left_part.count('C') == left_part.count('G'):
                # 递归计算两边的可能性并相乘
                res_left = count_noncrossing_matchings(left_part)
                res_right = count_noncrossing_matchings(right_part)
                total += res_left * res_right

    # 结果对 1,000,000 取模
    memo[s] = total % 1000000
    return memo[s]


def solve_cat(input_path, output_path):
    try:
        # 1. 读取 FASTA 文件
        record = list(SeqIO.parse(input_path, "fasta"))[0]
        rna_s = str(record.seq)

        # 2. 清空记忆化字典并计算
        memo.clear()
        result = count_noncrossing_matchings(rna_s)

        # 3. 写入结果
        with open(output_path, 'w') as out_f:
            out_f.write(str(result) + "\n")

        print(f"计算完成！不交叉匹配总数 (mod 1M): {result}")

    except Exception as e:
        print(f"运行出错: {e}")


if __name__ == "__main__":
    INPUT_FILE = "rosalind_cat.txt"
    OUTPUT_FILE = "output_cat.txt"
    solve_cat(INPUT_FILE, OUTPUT_FILE)