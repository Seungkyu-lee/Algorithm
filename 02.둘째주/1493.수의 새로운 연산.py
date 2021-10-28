import sys

sys.stdin = open('1493.txt', 'r')


def find(t):
    x = y = 1
    cur = 1
    while cur < t:
        x += 1
        cur += x
    back = cur - t
    x -= back
    y += back
    return x, y


for tc in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    px, py = find(p)
    qx, qy = find(q)

    cnt = step = 1
    for _ in range(px + qx - 1):
        step += 1
        cnt += step
    for _ in range(py + qy - 1):
        cnt += step
        step += 1
    print('#{} {}'.format(tc, cnt))
