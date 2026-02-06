from Bio import SeqIO
from Bio.Seq import Seq


def solve_orf_to_file(input_filename, output_filename):
    # 1. 读取 DNA 序列
    try:
        record = SeqIO.read(input_filename, "fasta")
    except Exception as e:
        print(f"读取文件出错: {e}")
        return

    dna_seq = record.seq
    rev_dna_seq = dna_seq.reverse_complement()

    # 存储所有发现的蛋白质序列（使用 set 自动去重）
    protein_results = set()

    # 2. 定义处理链的内部函数
    def find_proteins_in_chain(sequence):
        seq_len = len(sequence)
        # 遍历三个起始相位 (0, 1, 2)
        for frame in range(3):
            # 在当前阅读框内，以 3 为步长寻找所有 ATG
            # 注意范围要减去 2 以防索引越界
            for i in range(frame, seq_len - 2, 3):
                if sequence[i:i + 3] == "ATG":
                    # 从该 ATG 位置开始翻译到末尾
                    full_trans = sequence[i:].translate(table=1)

                    # 只有当翻译结果中包含终止符 '*' 时，才是一个有效的 ORF
                    if "*" in full_trans:
                        # split("*")[0] 截取第一个终止符之前的内容
                        protein_seq = str(full_trans.split("*")[0])
                        protein_results.add(protein_seq)

    # 3. 分别处理正向链和反向互补链
    find_proteins_in_chain(dna_seq)
    find_proteins_in_chain(rev_dna_seq)

    # 4. 将结果写入输出文件
    with open(output_filename, "w") as out_f:
        for p in protein_results:
            out_f.write(p + "\n")

    print(f"处理完成！结果已写入: {output_filename}")


# 执行函数
solve_orf_to_file("rosalind_orf.txt", "output_orf.txt")