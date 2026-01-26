# 读取输入（通常从 Rosalind 下载的 .txt 文件内容复制进来）
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# 统计四种碱基的出现次数
a_count = s.count('A')
c_count = s.count('C')
g_count = s.count('G')
t_count = s.count('T')

# 按顺序打印结果，用空格隔开
print(f"{a_count} {c_count} {g_count} {t_count}")