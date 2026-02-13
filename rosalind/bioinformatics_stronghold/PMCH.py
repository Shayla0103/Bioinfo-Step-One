import math

input_file = r"rosalind_pmch.txt"  # 确认文件名正确

with open(input_file, 'r') as f:
    # 1. 正确读取 FASTA 序列（跳过第一行 ID）
    lines = f.readlines()
    s = "".join(line.strip() for line in lines if not line.startswith(">"))

    n_au = s.count('A')
    n_gc = s.count('G')

    # 2. 使用 math.factorial 既准确又高效
    # 你的逻辑：perfect_au = n_au!
    perfect_au = math.factorial(n_au)
    perfect_gc = math.factorial(n_gc)

    n_final = perfect_au * perfect_gc

print(n_final)