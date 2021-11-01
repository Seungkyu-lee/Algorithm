import sys

sys.stdin = open('11387.몬스터 사냥.txt')

for tc in range(1, 1 + int(input())):
    D, L, N = map(int, input().split())
    ans = N * D + D * L * N * (N - 1) // 200
    print('#{} {}'.format(tc, ans))
