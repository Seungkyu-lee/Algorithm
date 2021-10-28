import sys

sys.stdin = open('5987.txt')

for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    run = [[] for _ in range(N)]
    