import sys

sys.stdin = open('10912.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = list(str(input()))
    ans = []

    for q in arr:
        if q not in ans:
            ans.append(q)
        else:
            ans.remove(q)
    ans.sort()
    ans = ''.join(ans)
    if len(ans) !=0:
        print('#{} {}'.format(tc, ans))
    else:
        print('#{} Good'.format(tc))

