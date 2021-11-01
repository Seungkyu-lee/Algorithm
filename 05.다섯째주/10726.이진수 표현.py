import sys

sys.stdin = open('10726.이진수 표현.txt')


def check():
    global N, M
    for i in range(N):
        if not M % 2:
            return False
        M //= 2
    else:
        return True


TC = int(input())
for tc in range(1, 1 + TC):
    N, M = map(int, input().split())
    ans = 'ON' if check() else 'OFF'
    print('#{} {}'.format(tc, ans))
