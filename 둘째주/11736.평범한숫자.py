import sys

sys.stdin = open('11736.txt', 'r')
for tc in range(1, int(input())+1):
    n= int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    for q in range(1,n-1):
        if arr[q-1]<arr[q]<arr[q+1] or arr[q+1]<arr[q]<arr[q-1]:
            cnt+=1

    print('#{} {}'.format(tc,cnt))