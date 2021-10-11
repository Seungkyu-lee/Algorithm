import sys

sys.stdin = open('3074.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 심사대 개수, 입국자 수
    t = [int(input()) for _ in range(N)]
    ans = 0

    l, r = 1, max(t) * M

    while l <= r:
        m = (l + r) // 2
        people = sum([m // time for time in t])

        if people >= M:
            ans = m
            r = m - 1
        else:
            l = m + 1

    print('#{} {}'.format(tc,ans))
