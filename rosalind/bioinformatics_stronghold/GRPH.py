# Solution #1
from Bio import SeqIO

records = list(SeqIO.parse("rosalind_grph.txt", "fasta"))
n = len(records)
k = 3
for x in range(n):
    rec_x = records[x]
    for y in range(n):
        rec_y = records[y]
        if rec_x.id == rec_y.id:
            continue
        if rec_x.seq[-k:] == rec_y.seq[:k]:
            print(rec_x.id, rec_y.id)


# Solution #2
from Bio import SeqIO


def solve_grph(input_file, output_file):
    records = list(SeqIO.parse(input_file, "fasta"))
    k = 3

    with open(output_file, "w") as f:
        for s in records:
            for t in records:
                # 排除自环
                if s.id == t.id:
                    continue

                # 检查 s 的后缀是否匹配 t 的前缀
                if s.seq.endswith(t.seq[:k]):
                    # 写入文件，注意每行末尾加换行符
                    f.write(f"{s.id} {t.id}\n")


# 调用函数
solve_grph("rosalind_grph.txt", "output_grph.txt")
print("分析完成，结果已保存至 output_grph.txt")