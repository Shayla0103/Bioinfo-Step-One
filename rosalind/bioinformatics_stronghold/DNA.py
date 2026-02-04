
with open('rosalind_dna.txt', 'r') as f:
    # .read() 读取全文
    # .strip() 去掉首尾的所有空白字符（包括换行符 \n、回车符 \r 和空格）
    s = f.read().strip()

# 统计四种碱基的出现次数
a_count = s.count('A')
c_count = s.count('C')
g_count = s.count('G')
t_count = s.count('T')

# 按顺序打印结果，用空格隔开
print(f"{a_count} {c_count} {g_count} {t_count}")