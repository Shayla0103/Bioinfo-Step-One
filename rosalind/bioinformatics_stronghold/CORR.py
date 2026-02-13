from Bio import SeqIO


def reverse_complement(seq):
    """计算 DNA 的反向互补序列"""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement[base] for base in reversed(seq))


def hamming_distance(s1, s2):
    """计算两个等长字符串的汉明距离"""
    return sum(1 for a, b in zip(s1, s2) if a != b)


def solve_corr(input_path, output_path):
    try:
        # 1. 读取所有 Reads
        reads = [str(record.seq) for record in SeqIO.parse(input_path, "fasta")]

        # 2. 统计频率确定正确集合
        # 注意：一个 Read 和它的反向互补被视为“同一种正确来源”
        all_reads = []
        for r in reads:
            all_reads.append(r)
            all_reads.append(reverse_complement(r))

        correct_set = set()
        incorrect_list = []

        for r in reads:
            # 如果该 Read 或其反向互补在原始数据中总共出现了至少 2 次
            if reads.count(r) + reads.count(reverse_complement(r)) >= 2:
                correct_set.add(r)
            else:
                incorrect_list.append(r)

        # 3. 纠错并准备输出
        results = []
        # 为了纠错，我们需要对比 correct_set 里的原序列及其反向互补
        candidates = []
        for c in correct_set:
            candidates.append(c)
            candidates.append(reverse_complement(c))

        for inc in incorrect_list:
            for cand in candidates:
                if hamming_distance(inc, cand) == 1:
                    results.append(f"{inc}->{cand}")
                    break  # 找到一个就跳出，题目保证解唯一

        # 4. 写入文件
        with open(output_path, 'w') as out_f:
            out_f.write("\n".join(results) + "\n")

        print(f"纠错完成！共修正 {len(results)} 条序列。")

    except Exception as e:
        print(f"运行出错: {e}")


if __name__ == "__main__":
    INPUT_FILE = "rosalind_corr.txt"
    OUTPUT_FILE = "output_corr.txt"
    solve_corr(INPUT_FILE, OUTPUT_FILE)