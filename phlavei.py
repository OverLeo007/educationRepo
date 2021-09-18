n = int(input())
m = list(range(1, n + 1))
m = m + m[::-1][1:]
max_len = len(m)
for i in range(1, n + 1):
    m = list(range(1, i + 1))
    m = m + m[::-1][1:]
    print(' ' * (max_len - len(m)), *m)
for i in range(n - 1, 0, -1):
    m = list(range(1, i + 1))
    m = m + m[::-1][1:]
    print(' ' * (max_len - len(m)), *m)

