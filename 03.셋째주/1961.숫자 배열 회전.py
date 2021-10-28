import sys

sys.stdin = open('1961.txt')


def rotate(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N - 1 - i] = arr[i][j]

    return new_arr


for tc in range(1, int(input()) + 1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    a = rotate(ARR)
    b = rotate(a)
    c = rotate(b)

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, a[i])) , ''.join(map(str, b[i])) , ''.join(map(str, c[i])))
