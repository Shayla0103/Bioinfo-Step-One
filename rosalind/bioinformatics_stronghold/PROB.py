import math


def solve_prob(input_path, output_path):

    try:
        # 1. 读取数据
        with open(input_path, 'r') as f:
            dna_s = f.readline().strip()
            # 获取所有 GC 含量的浮点数列表
            gc_array = [float(x) for x in f.readline().split()]

        if not dna_s or not gc_array:
            raise ValueError("输入文件内容缺失，请检查 DNA 序列或 GC 数组。")

        # 2. 执行计算
        # 统计固定序列 s 中的碱基分布
        gc_count = dna_s.count('G') + dna_s.count('C')
        at_count = dna_s.count('A') + dna_s.count('T')

        results = []
        for x in gc_array:
            # 使用对数性质：log(P) = count_GC * log(x/2) + count_AT * log((1-x)/2)
            prob_log = (gc_count * math.log10(x / 2)) + (at_count * math.log10((1 - x) / 2))
            results.append(f"{prob_log:.3f}")

        # 3. 写入结果
        with open(output_path, 'w') as out_f:
            out_f.write(" ".join(results) + "\n")

        print(f"成功！结果已保存至: {output_path}")

    except FileNotFoundError:
        print(f"错误：找不到输入文件 '{input_path}'，请确认文件路径。")
    except Exception as e:
        print(f"运行出错: {e}")


if __name__ == "__main__":
    INPUT_FILE = "rosalind_prob.txt"
    OUTPUT_FILE = "output_prob.txt"

    solve_prob(INPUT_FILE, OUTPUT_FILE)
