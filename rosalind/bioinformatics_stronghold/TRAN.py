from Bio import SeqIO


def solve_tran(input_path, output_path):
    """
    计算两条 DNA 序列的转换/颠换比率。
    """
    try:
        # 1. 使用 SeqIO 读取 FASTA 格式数据
        records = list(SeqIO.parse(input_path, "fasta"))
        if len(records) < 2:
            print("错误：需要两条序列。")
            return

        s1 = str(records[0].seq)
        s2 = str(records[1].seq)

        transitions = 0
        transversions = 0

        # 定义转换组
        purines = {'A', 'G'}
        pyrimidines = {'C', 'T'}

        # 2. 遍历并分类突变
        for b1, b2 in zip(s1, s2):
            if b1 != b2:
                # 判断是否为转换 (同为嘌呤或同为嘧啶)
                if (b1 in purines and b2 in purines) or (b1 in pyrimidines and b2 in pyrimidines):
                    transitions += 1
                else:
                    # 否则为颠换
                    transversions += 1

        # 3. 计算比值
        ratio = transitions / transversions if transversions != 0 else 0

        # 4. 写入输出文件
        with open(output_path, 'w') as out_f:
            out_f.write(f"{ratio:.11f}\n")

        print(f"计算完成！Transitions: {transitions}, Transversions: {transversions}")
        print(f"比率: {ratio:.11f}")

    except Exception as e:
        print(f"运行出错: {e}")


# ==========================================
# 主入口配置
# ==========================================
if __name__ == "__main__":

    INPUT_FILE = "rosalind_tran.txt"
    OUTPUT_FILE = "output_tran.txt"

    solve_tran(INPUT_FILE, OUTPUT_FILE)