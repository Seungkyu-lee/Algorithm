import sys

sys.stdin = open('2806.txt', 'r')


def p(idx, c):
    for i in range(idx):
        if idx - i == abs(c - map_list[i]):
            return True
    return False


def dfs(idx):
    if idx == N:
        global ans
        ans += 1
        return
    for i in range(N):
        if visit[i]: continue
        if p(idx, i): continue
        visit[i] = 1
        map_list[idx] = i
        dfs(idx + 1)
        visit[i] = 0
    return


for tc in range(1, int(input()) + 1):
    N = int(input())
    map_list = [0 for _ in range(N)]
    visit = [0] * N
    ans = 0
    dfs(0)
    print('#{} {}'.format(tc, ans))
