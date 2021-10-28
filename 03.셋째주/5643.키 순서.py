import sys

sys.stdin = open('5643.txt')

for tc in range(1, 1 + int(input())):
    N = int(input())
    M = int(input())
    klass = [[0] * N for _ in range(N)]

    for i in range(M):
        a, b = map(int, input().split())
        klass[a - 1][b - 1] = 1
    for i in klass:
        print(i)

    for i in range(N):
        for r in range(N):
            for c in range(N):
                if klass[r][i] + klass[i][c] == 2:
                    klass[r][c] = 1
    print('####################')
    for i in klass:
        print(i)

    cnt = [0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            if klass[i][j] == 1:
                cnt[i] += 1
                cnt[j] += 1

    print(cnt)
    print(cnt.count(N - 1))
