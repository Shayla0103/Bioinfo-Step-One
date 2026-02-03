# Solution #1
import pandas as pd
from Bio import SeqIO

filename = r"rosalind_cons.txt"
df = []
for record in SeqIO.parse(filename, "fasta"):
    df.append(record)
df = pd.DataFrame(df)

a, c, g, t = [], [], [], []
max_seq = []
for col in df.columns:
    all_counts = df[col].value_counts()
    a.append(str(all_counts.get('A', 0)))
    c.append(str(all_counts.get('C', 0)))
    g.append(str(all_counts.get('G', 0)))
    t.append(str(all_counts.get('T', 0)))
    max_seq.append(all_counts.idxmax())

print(''.join(max_seq))
print('A:', ' '.join(a))
print('C:', ' '.join(c))
print('G:', ' '.join(g))
print('T:', ' '.join(t))


# Solution #2:
# 内存友好：Pandas 的 value_counts() 在每一列都要创建一个序列对象，开销较大。纯 Python 方案直接在原地累加。
# 逻辑统一：NumPy 的向量化操作 (sequences == b) 避免了显式的 for 循环，速度非常快。
# 代码简洁：省去了将 SeqRecord 转为列表再转为 DataFrame 的复杂步骤。
import numpy as np
from Bio import SeqIO


def solve_cons_numpy(input_filename, output_filename):
    # 1. 使用 SeqIO 读取序列并转换为字符列表的 NumPy 矩阵
    records = list(SeqIO.parse(input_filename, "fasta"))
    # 将所有序列转换为二维字符数组，形状为 (序列数, 序列长度)
    data = np.array([list(str(rec.seq)) for rec in records])

    bases = ['A', 'C', 'G', 'T']
    n_length = data.shape[1]

    # 2. 计算 Profile 矩阵
    # 利用 NumPy 的广播机制：一次性比较整个矩阵并按列求和 (axis=0)
    profile = np.array([(data == base).sum(axis=0) for base in bases])

    # 3. 生成 Consensus 序列
    # argmax(axis=0) 找到每一列出现次数最多的碱基索引
    max_indices = profile.argmax(axis=0)
    consensus = "".join([bases[i] for i in max_indices])

    # 4. 将结果写入文件
    with open(output_filename, 'w') as f:
        # 写入共识序列
        f.write(consensus + '\n')

        # 写入 Profile 矩阵
        for i, base in enumerate(bases):
            # 将 NumPy 数组转为字符串并用空格连接
            counts_str = " ".join(profile[i].astype(str))
            f.write(f"{base}: {counts_str}\n")


# 运行脚本
solve_cons_numpy("rosalind_cons.txt", "output.txt")
print("NumPy 计算完成，结果已写入 output.txt")