import sys

sys.stdin = open('2805.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    m_idx = N // 2
    s = e = m_idx

    ans = 0
    for i in range(N):
        for j in range(s, e + 1):
            ans += int(arr[i][j])
        if i < m_idx:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print('#{} {}'.format(tc,ans))
