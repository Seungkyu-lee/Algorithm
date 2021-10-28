import sys

sys.stdin = open('2798.txt', 'r')
from itertools import combinations

# for tc in range(1, int(input()) + 1):
N, M = map(int, input().split())
card = sorted(list(map(int, input().split())))
lst = []
comb = list(combinations(card, 3))
for i in comb:
    if M < sum(i):
        continue
    else:
        lst.append(sum(i))
ans = max(lst)
print(ans)
