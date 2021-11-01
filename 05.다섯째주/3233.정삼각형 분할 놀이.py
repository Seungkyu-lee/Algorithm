import sys
sys.stdin=open('3233.정삼각형 분할 놀이.txt')

for tc in range(1,1+int(input())):
    A,B = map(int, input().split())

    N = A//B
    ans = N**2
    print('#{} {}'.format(tc,ans))