import re

# ?=表示开始向后看，不消耗字符，可以捕获重叠位置
# 使用 f-string，即f''将变量 t 放入正则表达式模式中，括号里的内容是一个整体
# finditer 返回包含起始位置的迭代器
# m.start() 返回这个匹配子串在母串中的起始索引位置。

file_path = 'rosalind_subs.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    s = lines[0].strip()
    t = lines[1].strip()

    matches = re.finditer(f'(?={t})', s)
    results = [str(m.start() + 1) for m in matches]

    print(" ".join(results))
