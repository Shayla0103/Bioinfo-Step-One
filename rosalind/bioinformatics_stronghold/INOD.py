def solve_inod(input_path, output_path):
    """
    计算拥有 n 个叶节点的进化树中的内部节点数量。
    公式：Internal Nodes = n - 2
    """
    try:
        # 1. 读取输入 n
        with open(input_path, 'r') as f:
            line = f.readline().strip()
            if not line:
                return
            n = int(line)

        # 2. 计算内部节点数
        # 这是一个固定的图论性质
        internal_nodes = n - 2

        # 3. 写入输出文件
        with open(output_path, 'w') as out_f:
            out_f.write(str(internal_nodes) + "\n")

        print(f"输入叶节点数: {n}")
        print(f"计算出的内部节点（祖先）数: {internal_nodes}")

    except Exception as e:
        print(f"运行出错: {e}")


# ==========================================
# 主入口配置
# ==========================================
if __name__ == "__main__":

    INPUT_FILE = "rosalind_inod.txt"
    OUTPUT_FILE = "output_inod.txt"

    solve_inod(INPUT_FILE, OUTPUT_FILE)