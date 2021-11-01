import sys
sys.stdin=open('6019.기차 사이의 파리.txt')

for tc in range(1,1+int(input())):
    D,A,B,F = map(int, input().split())
    train_time = D/(A+B)
    ans = F*train_time
    print('#{} {}'.format(tc,ans))
