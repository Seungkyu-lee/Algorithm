import sys

sys.stdin = open('3499.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    cnt = []
    n = N // 2
    if N % 2 == 0:
        for i in range(n):
            cnt.append(card[i])
            cnt.append(card[n])
            n += 1

    else:
        for i in range(n):
            cnt.append(card[i])
            cnt.append(card[n + 1])
            n += 1
        cnt.append(card[N // 2])

    print(f'#{tc}', ' '.join(cnt))
