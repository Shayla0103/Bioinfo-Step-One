import itertools


def solve_lexf(input_file, output_file):
    # 1. 读取输入数据
    with open(input_file, "r") as f:
        lines = f.readlines()
        # 第一行是字母表，用空格隔开
        alphabet = lines[0].split()
        # 第二行是长度 k
        k = int(lines[1].strip())

    # 2. 生成所有长度为 k 的排列 (允许重复)
    # repeat=k 表示将 alphabet 与自身进行 k 次笛卡尔积
    # itertools.product 会自动按照 alphabet 的顺序生成结果
    results = list(itertools.product(alphabet, repeat=k))

    # 3. 格式化并写入文件
    with open(output_file, "w") as out_f:
        for item in results:
            # 将元组 ('A', 'A') 转换为字符串 "AA"
            out_f.write("".join(item) + "\n")

    print(f"生成的排列总数: {len(results)}")
    print(f"结果已保存至: {output_file}")


# 执行
solve_lexf("rosalind_lexf.txt", "output_lexf.txt")