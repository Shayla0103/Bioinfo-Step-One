from Bio import SeqIO

def get_max_gc(filename):
    max_id = ""
    max_gc = 0

    # SeqIO.parse 自动处理 FASTA 逻辑，不管后缀是 .txt 还是 .fasta
    for record in SeqIO.parse(filename, "fasta"):
        # 计算 GC 含量
        g_count = record.seq.count('G')
        c_count = record.seq.count('C')
        gc_content = (g_count + c_count) / len(record.seq) * 100

        if gc_content > max_gc:
            max_gc = gc_content
            max_id = record.id

    return max_id, max_gc


# 运行
id, gc = get_max_gc('rosalind_gc.txt')
print(f"{id}\n{gc:.6f}")


# Solution 2:
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# 读取文件并计算每个序列的 GC 含量
results = {rec.id: gc_fraction(rec.seq) * 100 for rec in SeqIO.parse("rosalind_gc.txt", "fasta")}

# 找到最大值对应的 ID
best_id = max(results, key=results.get)

print(f"{best_id}\n{results[best_id]:.6f}")