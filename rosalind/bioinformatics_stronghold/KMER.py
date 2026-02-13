import itertools
from Bio import SeqIO


def solve_kmer(input_path, output_path):
    """
    统计 DNA 序列中所有可能的 4-mer 出现的频率（按字典序）。
    """
    try:
        # 1. 读取 FASTA 文件中的 DNA 序列
        record = list(SeqIO.parse(input_path, "fasta"))[0]
        dna_s = str(record.seq)

        # 2. 生成所有可能的 4-mer 字典（按字典序）
        # itertools.product 可以生成笛卡尔积，'ACGT' 的 4 次方正好是字典序
        k = 4
        bases = ['A', 'C', 'G', 'T']
        all_kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]

        # 初始化计数字典，例如 {'AAAA': 0, 'AAAC': 0, ...}
        kmer_counts = {kmer: 0 for kmer in all_kmers}

        # 3. 使用滑动窗口统计频率
        # 窗口长度为 4，步长为 1
        for i in range(len(dna_s) - k + 1):
            window = dna_s[i:i + k]
            if window in kmer_counts:
                kmer_counts[window] += 1

        # 4. 按照字典序提取计数值
        results = [str(kmer_counts[kmer]) for kmer in all_kmers]

        # 5. 写入输出文件
        with open(output_path, 'w') as out_f:
            out_f.write(" ".join(results) + "\n")

        print(f"统计完成！共扫描了 {len(dna_s) - k + 1} 个窗口。")
        print(f"结果已保存至: {output_path}")

    except Exception as e:
        print(f"运行出错: {e}")


if __name__ == "__main__":

    INPUT_FILE = "rosalind_kmer.txt"
    OUTPUT_FILE = "output_kmer.txt"

    solve_kmer(INPUT_FILE, OUTPUT_FILE)