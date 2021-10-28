import sys

sys.stdin = open('10761.txt', 'r')


def move(r, p):
    if r < p:
        return r + 1
    elif r > p:
        return r - 1
    else:
        return r


for tc in range(1, int(input()) + 1):
    N = input().split()
    Button = []
    B = []
    O = []

    for i in range(1, int(N[0]) * 2, 2):
        # 로봇 순서 입력
        Button.append(N[i])
        if N[i] == 'B':
            B.append(int(N[i + 1]))
        else:
            O.append((int(N[i + 1])))

    ans = 0
    b = o = 1

    for i in Button:
        while True:
            ans += 1
            if O:
                moveO = move(o, O[0])
            if B:
                moveB = move(b, B[0])

            if i == 'B':
                if b == moveB:
                    B.pop(0)
                    o = moveO
                    break
            else:
                if o == moveO:
                    O.pop(0)
                    b = moveB
                    break
            o = moveO
            b = moveB
    print('#{} {}'.format(tc,ans))
