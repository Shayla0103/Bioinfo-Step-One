from Bio import SeqIO
from Bio.Seq import Seq


def solve_splc(input_file, output_file):
    # 1. 读取 FASTA 文件
    # records[0] 是 DNA，records[1:] 是所有内含子
    records = list(SeqIO.parse(input_file, "fasta"))
    main_dna = str(records[0].seq)
    introns = [str(r.seq) for r in records[1:]]

    # 2. 依次剔除内含子
    # 因为内含子不重叠，直接使用字符串替换为空即可
    clean_dna = main_dna
    for intron in introns:
        clean_dna = clean_dna.replace(intron, "")

    # 3. 翻译
    # to_stop=True 翻译到终止密码子停止，且不包含 "*"
    protein_seq = Seq(clean_dna).translate(to_stop=True)

    # 4. 写入文件
    with open(output_file, "w") as f:
        f.write(str(protein_seq) + "\n")

    print(f"剪接完成！蛋白质长度: {len(protein_seq)}")
    print(f"结果已保存至: {output_file}")


# 执行
solve_splc("rosalind_splc.txt", "output_splc.txt")