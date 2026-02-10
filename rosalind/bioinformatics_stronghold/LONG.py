"""
给出最多50条长度几乎一致的DNA string（因此没有必要先找出最短的一条），
它们来自同一条线性染色体（因此没必要考虑反向阅读的和互补的情况），
存在唯一的方式让它们组合成完整的染色体，前后能互补的必然只有一对（因此只需要判断任意两条DNA string是否存在前后互补的关系，不用考虑有某一条DNA string因为存在重复而在合并过程中被完全抹除）
重叠长度超过他们的一半，那说明最少有一半肯定是一样的，就用当前项除2所得整数的那个长度前半段和后半段去匹配，完全重合就说明匹配完成，不完全重合就不匹配
"""

from Bio import SeqIO


def solve_long_half_logic(input_file, output_file):
    # 1. 读取所有序列
    records = list(SeqIO.parse(input_file, "fasta"))
    reads = [str(r.seq) for r in records]

    # 初始锚点：以第一项为起始序列
    current_contig = reads.pop(0)

    while reads:
        found_match = False

        for i in range(len(reads)):
            target = reads[i]
            n_target = len(target)
            half = n_target // 2

            # 取 target 的前半段和后半段作为“探测针”
            first_half = target[:half]
            last_half = target[n_target - half:]

            # 情况 A: target 接在 current_contig 的【后面】
            # 逻辑：target 的前半段 (first_half) 必须出现在 current_contig 的尾部区域
            # 我们只需要看 current_contig 最后 n_target 长度的范围内是否包含 first_half
            search_region_tail = current_contig[-(n_target - 1):]
            if first_half in search_region_tail:
                # 定位重合的起始位置
                offset = search_region_tail.find(first_half)
                overlap_len = len(search_region_tail) - offset
                # 合并：保留 contig，加上 target 剩余的部分
                current_contig = current_contig + target[overlap_len:]
                reads.pop(i)
                found_match = True
                break

            # 情况 B: target 接在 current_contig 的【前面】
            # 逻辑：target 的后半段 (last_half) 必须出现在 current_contig 的头部区域
            search_region_head = current_contig[:n_target - 1]
            if last_half in search_region_head:
                # 定位重合的结束位置
                offset = search_region_head.find(last_half)
                overlap_len = offset + half
                # 合并：加上 target 前面不重合的部分，拼接 contig
                current_contig = target[:n_target - overlap_len] + current_contig
                reads.pop(i)
                found_match = True
                break

        if not found_match:
            break

    with open(output_file, "w") as f:
        f.write(current_contig + "\n")

    print(f"组装完成！最终长度: {len(current_contig)}")


solve_long_half_logic("rosalind_long.txt", "output_long.txt")