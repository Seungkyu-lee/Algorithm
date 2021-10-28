import sys
sys.stdin = open('3260.txt')

for tc in range(1, int(input())+1):
    A,B = map(int, input().split())

    ans = A+B
    print('#{} {}'.format(tc, ans))