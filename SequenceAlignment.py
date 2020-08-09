import numpy as np


def sequence_alignment(seq1, n1, seq2, n2, gap=2, mmt=1):
    opt = np.zeros((n1+1, n2+1), dtype=int)

    for i in range(n1+1):
        opt[i, n2] = gap * (n1-i)
    for i in range(n2+1):
        opt[n1, i] = gap * (n2-i)

    for i in reversed(range(n1)):
        for j in reversed(range(n2)):
            base_match = seq1[i] == seq2[j]
            aligned = opt[i+1, j+1] + (0 if base_match else mmt)
            gap1 = gap + opt[i+1, j]
            gap2 = gap + opt[i, j+1]
            opt[i, j] = min(aligned, gap1, gap2)

    seq1_out = []
    seq2_out = []
    i = 0
    j = 0
    while i < n1 or j < n2:
        if opt[i, j] == opt[i+1, j+1] + (0 if seq1[i] == seq2[j] else mmt):
            seq1_out.append(seq1[i])
            seq2_out.append(seq2[j])
            i += 1
            j += 1
        elif opt[i, j] == opt[i, j+1] + gap:
            seq1_out.append('-')
            seq2_out.append(seq2[j])
            j += 1
        else:
            seq1_out.append(seq1[i])
            seq2_out.append('-')
            i += 1

    return seq1_out, seq2_out
    
if __name__ == '__main__':
    out = sequence_alignment(['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C','C'], 10,
                             ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A'], 8,
                             2, 1)
    print(out)
