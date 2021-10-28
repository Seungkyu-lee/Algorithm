import sys

sys.stdin = open('4261.txt')
from itertools import product, combinations

keypad = {
    '1': '', '2': 'abc', '3': 'def',
    '4': 'ghi', '5': 'jkl', '6': 'mno',
    '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
}
for tc in range(1, int(input()) + 1):
    S, N = input().split()
    N = int(N)
    word = input().split()

    cnt = 0

    for w in word:
        for i in range(len(w)):
            if w[i] not in keypad[S[i]]:
                break
        else:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
