n = 4
a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]

for row in a:
    print(' '.join([str(elem) for elem in row]))