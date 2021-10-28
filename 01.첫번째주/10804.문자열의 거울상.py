import sys

sys.stdin = open('10804.txt', 'r')

mirror = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p',
}

for tc in range(1, int(input()) + 1):
    arr = input()
    mir = []
    for i in arr:
        mir.append(mirror[i])
    cnt = ''.join(mir[::-1])

    print('#{} {}'.format(tc, cnt))
