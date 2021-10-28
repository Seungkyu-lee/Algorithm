import sys

sys.stdin = open('10580.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    info = [[] for _ in range(N)]

    for i in range(N):
        info[i] = list(map(int, input().split()))

    ans = 0
    for i1 in range(N - 1):
        for i2 in range(i1 + 1, N):
            l1, r1 = info[i1]
            l2, r2 = info[i2]

            if (l1 > l2 and r1 < r2) or (l1 < l2 and r1 > r2):
                ans += 1
    print('#{} {}'.format(tc, ans))
