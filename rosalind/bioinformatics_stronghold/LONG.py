"""
寻找“最短超级字符串”本质上是一个 NP-hard 问题，但对于 Rosalind 这道题的数据规模，使用贪心算法可以得到正确解：
1. 寻找最大重叠：在所有片段对中，找到重叠部分最长的一对序列（假设序列 A 的尾部与序列 B 的头部重叠）。
2. 合并序列：将这两条序列合并成一条新的序列，并从原始集合中删除 A 和 B，加入合并后的新序列。
3. 循环往复：重复上述过程，直到集合中只剩下一个序列，这个序列就是我们要找的超级字符串。
重叠要求：题目保证重叠部分长度超过片段长度的一半，这极大地简化了搜索空间。
"""


def get_max_overlap(s1, s2):
    """计算 s1 尾部与 s2 头部最长重叠，要求重叠必须 > 一半长度"""
    n1, n2 = len(s1), len(s2)
    # 题目明确：重叠长度 > 序列长度的一半
    threshold = min(n1, n2) // 2

    for length in range(min(n1, n2), threshold, -1):
        if s1[n1 - length:] == s2[:length]:
            return length
    return 0


def solve_long_perfect(input_file, output_file):
    # 1. 读取 FASTA
    reads = []
    current_seq = ""
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if line.startswith(">"):
                if current_seq: reads.append(current_seq)
                current_seq = ""
            else:
                current_seq += line
        if current_seq: reads.append(current_seq)

    # 2. 全局贪心合并
    while len(reads) > 1:
        best_overlap = -1
        best_pair = (-1, -1)

        # 寻找全局最长重叠的一对 (i, j)
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i == j: continue

                length = get_max_overlap(reads[i], reads[j])
                if length > best_overlap:
                    best_overlap = length
                    best_pair = (i, j)

        # 3. 合并最长的一对
        if best_overlap > 0:
            i, j = best_pair
            s1, s2 = reads[i], reads[j]
            merged_seq = s1 + s2[best_overlap:]

            # 按照索引从大到小删除，避免索引偏移
            first, second = sorted([i, j], reverse=True)
            reads.pop(first)
            reads.pop(second)
            reads.append(merged_seq)
        else:
            # 如果找不到任何重叠（不符合题目预期）
            break

    # 4. 写入
    with open(output_file, "w") as f:
        f.write(reads[0] + "\n")
    print(f"最终序列长度: {len(reads[0])}")


solve_long_perfect("rosalind_long.txt", "output_long.txt")