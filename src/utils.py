def xor(a, b, pbar):
    pbar.update(1)
    return a ^ b


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]
