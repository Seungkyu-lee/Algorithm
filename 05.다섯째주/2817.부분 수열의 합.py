import sys

sys.stdin = open('2817.부분 수열의 합.txt')


def solve(idx, sum):
    global cnt
    if idx >= N:
        return
    tmp = sum + A[idx]
    if tmp == K:
        cnt += 1
    solve(idx + 1, sum)
    solve(idx + 1, tmp)


for tc in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    solve(0, 0)
    print('#{} {}'.format(tc, cnt))
