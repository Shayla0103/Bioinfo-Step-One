# 定义映射关系：A->T, T->A, C->G, G->C
table = str.maketrans('ATCG', 'TAGC')

# Test (copied)
s = r'AAAACCCGGT'

# translate 负责替换，[::-1] 负责翻转
with open('rosalind_revc.txt', 'r') as f:
    s = f.read().strip()
    s_revc = s.translate(table)[::-1]

print(s_revc)
