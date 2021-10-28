import sys

sys.stdin = open('12004.구구단1.txt')

dic = {}
for i in range(1,10):
    for j in range(1,10):
        if not dic.get(i*j):
            dic[i*j] = 1

T = int(input())

for tc in range(1,T +1):
    N = int(input())
    if dic.get(N):
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))