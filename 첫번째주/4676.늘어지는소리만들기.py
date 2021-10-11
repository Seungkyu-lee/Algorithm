import sys

sys.stdin = open('4676.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    sound = list(input())
    H = int(input())
    local = list(map(int,input().split()))
    local.sort(reverse=True)

    for i in local:
        sound.insert(i,'-')

    print('#{} {}'.format(tc,''.join(sound)))
