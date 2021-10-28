import sys

sys.stdin = open('7568.덩치.txt')
N = int(input())
person = []
for i in range(N):
    person.append(list(map(int, input().split())))

for i in person:
    rank = 1
    for j in person:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
