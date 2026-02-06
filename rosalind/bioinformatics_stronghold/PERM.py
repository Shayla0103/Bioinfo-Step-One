import itertools
import math


def solve_perm(n, output_filename):
    # 1. 创建 1 到 n 的列表
    nums = list(range(1, n + 1))

    # 2. 计算全排列总数 (n!)
    total_count = math.factorial(n)

    # 3. 生成所有全排列
    # itertools.permutations 返回一个迭代器，节省内存
    all_perms = list(itertools.permutations(nums))

    # 4. 写入文件
    with open(output_filename, "w") as f:
        # 第一行写入总数
        f.write(f"{total_count}\n")

        # 遍历每一个排列并写入
        for p in all_perms:
            # 将元组 (1, 2, 3) 转换为字符串 "1 2 3"
            line = " ".join(map(str, p))
            f.write(line + "\n")

    print(f"n={n} 的全排列已生成，共 {total_count} 组，已保存至 {output_filename}")


# 从文件读取输入 (Rosalind 的输入通常只有一个数字)
with open("rosalind_perm.txt", "r") as f:
    n_val = int(f.read().strip())

solve_perm(n_val, "output_perm.txt")