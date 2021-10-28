import sys

sys.stdin = open('4672.수진이의 팰린드롬.txt')


T = int(input())
W = input()

ans = [] * 27
for c in W:
    ans[int(chr(c) - 'a')] += 1

print(ans)
