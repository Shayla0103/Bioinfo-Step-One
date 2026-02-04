# Solution #1
from Bio import SeqIO
input_filename = r"rosalind_lcsm.txt"
records = list(SeqIO.parse(input_filename, "fasta"))
seqs = [str(r.seq) for r in records] # 将序列转为字符串方便操作

lcsm = ''
for start_n in range(len(seqs[0])):
    for stop_n in range(start_n + len(lcsm) + 1, len(seqs[0]) + 1):
        # 只关心比当前已找到的 lcsm 更长的子串，
        # 如果想要找到所有符合条件的子串，需要将输出结果lcsm从字符串改为列表
        # 但是当前只需要输出任意一个子串就行。
        substring = seqs[0][start_n: stop_n]

        if all(substring in s for s in seqs):
            # 如果都在，且比之前的长，则更新
            if len(substring) > len(lcsm):
                lcsm = substring
        else:
            # 如果当前子串已经不在所有序列中了，更长的子串肯定也不在，直接跳出内层循环
            break
print(lcsm)


# Solution #2
from Bio import SeqIO


def solve_lcsm():
    # 1. 读入并排序，选最短的作为基准，减少搜索空间
    records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
    seqs = [str(r.seq) for r in records]
    seqs.sort(key=len)
    shortest = seqs[0]
    others = seqs[1:]

    def get_common_substring(length):
        """检查是否存在长度为 length 的公共子串"""
        # 获取最短序列中所有长度为 length 的子串，放入集合（去重且查找快）
        candidates = {shortest[i:i + length] for i in range(len(shortest) - length + 1)}

        for s in others:
            # 过滤 candidates：只保留同时存在于当前序列 s 中的子串
            candidates = {sub for sub in candidates if sub in s}
            if not candidates:
                return None
        return list(candidates)[0] if candidates else None

    # 2. 对长度进行二分搜索
    low = 1
    high = len(shortest)
    best_lcsm = ""

    while low <= high:
        mid = (low + high) // 2
        found = get_common_substring(mid)
        if found:
            best_lcsm = found
            low = mid + 1  # 尝试找更长的
        else:
            high = mid - 1  # 找短一点的

    return best_lcsm


print(solve_lcsm())

"""
最优工程解法：二分搜索长度 + Set 过滤这种方法将时间复杂度从 $O(L^3)$ 降低到了 $O(L^2 \log L)$。
1. 二分搜索长度：传统暴力法每增加一个长度都要重新扫描。二分法利用了单调性：如果长度为 100 的子串不存在，
那么长度为 101 的也肯定不存在。这让搜索次数从 $1000$ 次降到了 $\log_2(1000) \approx 10$ 次。
2. 集合过滤 (Set Intersection)：我的代码中 candidates = {sub for sub in candidates if sub in s} 这一行是灵魂。
它不是在每一条序列里盲目找子串，而是不断缩小可能性的范围。处理到第 5-10 条序列时，candidates 集合通常就已经缩减到只剩几个甚至零个了，
后续序列的匹配几乎是瞬时完成的。
3. 内存与速度的平衡：虽然后缀树是 $O(N)$，但在 Python 中构建后缀树对象的内存开销极大，代码极其复杂（容易写错）。
二分法利用 Python 原生的 in 关键字（底层是高度优化的 C 代码），实际运行速度往往比手写的复杂算法更快。📊 

性能对比（估计值）你的原始代码：处理 100 条 1kb 序列约需 30 - 60 秒。
二分搜索法：处理相同数据约需 0.1 - 0.5 秒。
"""