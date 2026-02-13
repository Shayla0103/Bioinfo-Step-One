import itertools


def solve_sign(input_path, output_path):
    """
    生成带符号全排列并写入文件。
    n! * 2^n 种组合。
    """
    try:
        # 1. 读取输入数据 (n)
        with open(input_path, 'r') as f:
            line = f.readline().strip()
            if not line:
                return
            n = int(line)

        # 2. 生成基础排列和符号组合
        elements = list(range(1, n + 1))
        # 全排列: n!
        perms = list(itertools.permutations(elements))
        # 符号组合: 2^n (使用 1 和 -1 作为系数)
        sign_combos = list(itertools.product([1, -1], repeat=n))

        # 3. 碰撞生成最终结果
        signed_permutations = []
        for p in perms:
            for s in sign_combos:
                # 对应位置数字乘以符号
                item = [p[i] * s[i] for i in range(n)]
                signed_permutations.append(item)

        # 4. 写入输出文件
        with open(output_path, 'w') as out_f:
            # 第一行写入总数
            out_f.write(f"{len(signed_permutations)}\n")
            # 后续行写入具体的排列
            for res in signed_permutations:
                # 使用 * 解包并用空格连接
                out_f.write(" ".join(map(str, res)) + "\n")

        print(f"计算完成！总计 {len(signed_permutations)} 种排列。")
        print(f"结果已保存至: {output_path}")

    except FileNotFoundError:
        print(f"错误：找不到输入文件 '{input_path}'。")
    except Exception as e:
        print(f"运行出错: {e}")


# ==========================================
# 主入口配置
# ==========================================
if __name__ == "__main__":
    INPUT_FILE = "rosalind_sign.txt"
    OUTPUT_FILE = "output_sign.txt"

    solve_sign(INPUT_FILE, OUTPUT_FILE)