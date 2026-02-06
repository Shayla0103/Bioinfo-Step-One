import bisect


def get_lis(arr):
    """获取最长递增子序列"""
    n = len(arr)
    # tails[i] 存储长度为 i+1 的递增子序列的最小末尾元素
    tails = []
    # parents[i] 存储 arr[i] 在 LIS 中的前驱索引，用于回溯路径
    parent = [-1] * n
    # tail_indices[i] 存储 tails[i] 对应的元素在 arr 中的原始索引
    tail_indices = []

    for i, x in enumerate(arr):
        # 使用二分查找 x 应该插入的位置
        idx = bisect.bisect_left(tails, x)

        if idx < len(tails):
            tails[idx] = x
            tail_indices[idx] = i
        else:
            tails.append(x)
            tail_indices.append(i)

        # 记录路径：当前元素的前驱是长度减 1 的那个子序列的末尾
        if idx > 0:
            parent[i] = tail_indices[idx - 1]

    # 回溯构造序列
    curr = tail_indices[-1]
    lis = []
    while curr != -1:
        lis.append(arr[curr])
        curr = parent[curr]
    return lis[::-1]


def solve_lgis(input_file, output_file):
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        # 读取排列，处理可能的换行
        arr = []
        for line in f:
            arr.extend(map(int, line.split()))

    # 1. 计算最长递增子序列 (LIS)
    lis = get_lis(arr)

    # 2. 计算最长递减子序列 (LDS)
    # 技巧：求 LDS 等同于对原序列取反后求 LIS，或者改变比较逻辑
    # 这里我们采用对序列元素取负值的技巧
    negative_arr = [-x for x in arr]
    lds_neg = get_lis(negative_arr)
    lds = [-x for x in lds_neg]

    # 3. 写入文件
    with open(output_file, 'w') as f:
        f.write(" ".join(map(str, lis)) + "\n")
        f.write(" ".join(map(str, lds)) + "\n")

    print(f"处理完成！结果已写入 {output_file}")


# 执行
solve_lgis("rosalind_lgis.txt", "output_lgis.txt")