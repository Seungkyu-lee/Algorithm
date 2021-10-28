import sys

sys.stdin = open('4047.txt')

for tc in range(1, int(input()) + 1):
    card = input()
    dump = set()
    S = 13
    D = 13
    H = 13
    C = 13
    for c in range(0, len(card), 3):
        T, X, Y = card[c], card[c + 1], card[c + 2]
        dump.add((T, int(X + Y)))
    if len(dump) != len(card) // 3:
        print('#{} ERROR'.format(tc))
    else:
        for d in dump:
            if d[0] == 'S':
                S -= 1
            elif d[0] == 'D':
                D -= 1
            elif d[0] == 'H':
                H -= 1
            elif d[0] == 'C':
                C -= 1

        print('#{} {} {} {} {}'.format(tc, S, D, H, C))
