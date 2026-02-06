from Bio import SeqIO


def solve_revp(input_file, output_file):
    # 1. 读取 FASTA 文件 (REVP 题目通常只有一个序列)
    record = SeqIO.read(input_file, "fasta")
    dna_seq = record.seq
    n = len(dna_seq)

    results = []

    # 2. 遍历所有可能的长度 (4 到 12)
    # 注意：反向回文序列的长度必然是偶数
    for length in range(4, 13):
        # 3. 滑动窗口遍历序列
        for i in range(n - length + 1):
            # 截取当前子串
            substring = dna_seq[i:i + length]

            # 检查是否等于其反向互补序列
            if substring == substring.reverse_complement():
                # 记录结果：起始位置(从1开始), 长度
                results.append(f"{i + 1} {length}")

    # 4. 将结果写入 txt 文件
    with open(output_file, "w") as f:
        f.write("\n".join(results) + "\n")

    print(f"分析完成！共找到 {len(results)} 个限制位点。")
    print(f"结果已保存至: {output_file}")


# 执行
solve_revp("rosalind_revp.txt", "output_revp.txt")