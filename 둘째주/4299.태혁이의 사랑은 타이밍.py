import sys

sys.stdin = open('4299.txt', 'r')

for tc in range(1, int(input()) + 1):
    D, H, M = map(int, input().split())
    ans = 0
    ans += (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)
    if ans<0:
        ans =-1
    print('#{} {}'.format(tc, ans))
