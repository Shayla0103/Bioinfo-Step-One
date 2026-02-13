from Bio import SeqIO


def solve_sseq(input_path, output_path):
    """
    在序列 s 中寻找子序列 t 的索引位置。
    使用贪心算法：每次找到匹配后立即移动到下一个字符。
    """
    try:
        # 1. 使用 SeqIO 读取 FASTA 文件
        records = list(SeqIO.parse(input_path, "fasta"))
        if len(records) < 2:
            print("错误：FASTA 文件中至少需要两个序列。")
            return

        s = str(records[0].seq)
        t = str(records[1].seq)

        indices = []
        last_pos = 0

        # 2. 遍历 t 中的每个碱基
        for char in t:
            # 在 s 中从上一次找到的位置之后开始搜索
            # s.find(字符, 起始位置) 返回找到的第一个索引
            found_idx = s.find(char, last_pos)

            if found_idx != -1:
                # Rosalind 要求从 1 开始计数，所以 +1
                indices.append(found_idx + 1)
                # 下一次搜索必须从当前位置的后面开始
                last_pos = found_idx + 1
            else:
                print(f"未能在剩余序列中找到碱基: {char}")
                break

        # 3. 写入输出文件
        with open(output_path, 'w') as out_f:
            # 用空格分隔索引并写入
            out_f.write(" ".join(map(str, indices)) + "\n")

        print(f"计算完成！找到 {len(indices)} 个索引。")
        print(f"结果已保存至: {output_path}")

    except Exception as e:
        print(f"运行出错: {e}")


# ==========================================
# 主入口配置
# ==========================================
if __name__ == "__main__":
    INPUT_FILE = "rosalind_sseq.txt"
    OUTPUT_FILE = "output_sseq.txt"

    solve_sseq(INPUT_FILE, OUTPUT_FILE)