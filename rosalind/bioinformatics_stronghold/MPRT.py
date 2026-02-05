import requests
import re
from Bio import SeqIO
from io import StringIO


def solve_mprot_to_file(input_file, output_file):
    # 正则表达式：(?=...) 用于处理重叠匹配（如 NNST）
    # N 开头，后接非 P，再接 S 或 T，再接非 P
    motif_regex = r'(?=N[^P][ST][^P])'

    with open(input_file, "r") as f:
        protein_ids = [line.strip() for line in f if line.strip()]

    results = []

    for original_id in protein_ids:
        # 获取基础 ID 用于拼接 URL (例如 B5ZC00_ABC -> B5ZC00)
        accession_id = original_id.split('_')[0]
        url = f"https://rest.uniprot.org/uniprotkb/{accession_id}.fasta"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"警告: 无法获取 ID {original_id} 的数据 (HTTP {response.status_code})")
                continue

            # 解析 FASTA
            record = SeqIO.read(StringIO(response.text), "fasta")
            sequence = str(record.seq)

            # 寻找匹配位置（m.start() + 1 是因为 Rosalind 要求从 1 开始计数）
            positions = [str(m.start() + 1) for m in re.finditer(motif_regex, sequence)]

            # 只有找到基序时才记录结果
            if positions:
                results.append(original_id)
                results.append(" ".join(positions))

        except Exception as e:
            print(f"处理 {original_id} 时发生错误: {e}")

    # 将所有结果写入输出文件
    with open(output_file, "w") as out_f:
        for line in results:
            out_f.write(line + "\n")

    print(f"分析完成！结果已保存至: {output_file}")


# 执行函数
solve_mprot_to_file("rosalind_mprt.txt", "output_mprt.txt")