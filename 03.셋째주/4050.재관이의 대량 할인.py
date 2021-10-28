import sys

sys.stdin = open('4050.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    shop = list(map(int, input().split()))

    shop.sort(reverse=True)  # 높은순으로 정렬
    lst = []
    for i in range(N):
        if i % 3 != 2:  # 3번째마다 값을 제외
            lst.append(shop[i])

    ans = sum(lst)
    print('#{} {}'.format(tc,ans))
