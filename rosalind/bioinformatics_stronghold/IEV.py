n1, n2, n3, n4, n5, n6 = 19544, 19325, 16582, 18100, 16470, 16680
n4_aa = 0.25 * 2 * n4
n5_aa = 0.5 * 2 * n5
n6_aa = 1 * 2 * n6
total_aa = sum([n4_aa, n5_aa, n6_aa])

total_offs = sum([n1, n2, n3, n4, n5, n6] * 2)
total_dominant = total_offs - total_aa
print(total_dominant)
