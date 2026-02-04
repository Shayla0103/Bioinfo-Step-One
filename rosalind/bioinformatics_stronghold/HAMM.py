with open('rosalind_hamm.txt', 'r') as f:
    # 读取第一行并去换行，读取第二行并去换行
    line1 = f.readline().strip()
    line2 = f.readline().strip()

    distance = sum(1 for a, b in zip(line1, line2) if a != b)
    print(distance)