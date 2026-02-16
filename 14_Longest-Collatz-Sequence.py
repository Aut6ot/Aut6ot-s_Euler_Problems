def collatzinator(n):
    seq_len = 0
    while n != 1:
        seq_len += 1
        # print(n)
        if n % 2 == 0:
            # n is even
            n = int(n / 2)
        else:
            # n is odd
            n = int(n * 3 + 1)
    seq_len += 1  # account for 1 at the end
    return seq_len


max_len = 0
for x in range(1, 1000001):
    seq_len = collatzinator(x)
    if seq_len > max_len:
        max_len = seq_len
        print(f"NEW HIGH SCORE: {x} with {seq_len} terms!")
