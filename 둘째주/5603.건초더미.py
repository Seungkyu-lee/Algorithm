import sys

sys.stdin = open('5603.txt', 'r')


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(int(input()))

    avg = sum(arr)//N
    ans = 0
    for i in range(N):
        ans += abs(arr[i]-avg)
    print('#{} {}'.format(tc, ans//2))
