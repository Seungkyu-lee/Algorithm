N = (10 ** 6 + 1)
prim = [1] * N
prim[0] = prim[1] = 0

for i in range(2, N):
    if prim[i] == 1:
        for j in range(i * 2, N, i):
            prim[j] = 0

for i in range(N):
    if prim[i] == 1:
        print(i, end=' ')
