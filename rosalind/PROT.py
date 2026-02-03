from Bio.Seq import translate

filename = r"rosalind_prot.txt"
with open(filename, 'r') as f:
    # 去掉可能的首尾空格或换行符
    rna_string = f.read().strip()

# to_stop=True 会在遇到第一个终止密码子时停止，且不包含末尾的 '*'
protein = translate(rna_string, to_stop=True)
print(protein)