import sys

sys.stdin = open('10912.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = list(str(input()))
    cnt = []

    for q in arr:
        if q not in cnt:
            cnt.append(q)
        else:
            cnt.remove(q)
    cnt.sort()
    cnt = ''.join(cnt)
    if len(cnt) !=0:
        print('#{} {}'.format(tc, cnt))
    else:
        print('#{} Good'.format(tc))

