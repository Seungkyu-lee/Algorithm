import sys

sys.stdin = open('15649.N과M(1).txt')

from itertools import permutations

N, M = map(int, input().split())
arr = []
for i in range(1, N + 1):
    arr.append(i)

ans = permutations(arr, M)

for i in ans:
    print(' '.join(map(str, i)))
