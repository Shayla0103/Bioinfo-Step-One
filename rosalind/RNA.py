# Test (copied)
# t = r'GATGGAACTTGACTACGTAAATT'

with open('rosalind_rna.txt', 'r') as f:
    t = f.read().strip()

t = t.replace('T', 'U')
print(t)