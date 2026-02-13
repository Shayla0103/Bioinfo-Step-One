def solve_tree(input_path, output_path):
    """
    计算将无环图补全为树所需的最少边数。
    核心公式：(n - 1) - 当前边数
    """
    try:
        with open(input_path, 'r') as f:
            # 第一行是节点总数 n
            line = f.readline().strip()
            if not line:
                return
            n = int(line)

            # 读取剩下的所有行，每一行代表一条边
            current_edges = 0
            for edge_line in f:
                if edge_line.strip():
                    current_edges += 1

        # 计算结果
        # 一个树需要 n-1 条边，现在的缺口就是我们要补的边数
        min_edges_to_add = (n - 1) - current_edges

        # 写入结果
        with open(output_path, 'w') as out_f:
            out_f.write(str(min_edges_to_add) + "\n")

        print(f"节点数: {n}, 当前边数: {current_edges}")
        print(f"需要添加的边数: {min_edges_to_add}")

    except Exception as e:
        print(f"运行出错: {e}")


# ==========================================
# 主入口配置
# ==========================================
if __name__ == "__main__":
    INPUT_FILE = "rosalind_tree.txt"
    OUTPUT_FILE = "output_tree.txt"

    solve_tree(INPUT_FILE, OUTPUT_FILE)