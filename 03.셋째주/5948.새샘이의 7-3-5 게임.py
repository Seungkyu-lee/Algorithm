import sys

sys.stdin = open('5948.txt')
from itertools import combinations

for tc in range(1, int(input()) + 1):
    numbers = list(set(map(int, input().split())))

    comb = combinations(numbers, 3)
    comb_sum = list(sum(cmb) for cmb in comb)
    comb_sum = list(set(comb_sum))

    comb_sum.sort(reverse=True)
    print(comb_sum)
    print('#{} {}'.format(tc, comb_sum[4]))
