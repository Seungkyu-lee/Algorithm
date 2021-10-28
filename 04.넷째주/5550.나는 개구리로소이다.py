import sys

sys.stdin = open('5550.나는 개구리로소이다.txt')

N = int(input())


def frog(word):
    cnt_c = 0
    cnt_r = 0
    cnt_o = 0
    cnt_a = 0
    cnt_k = 0
    result = 0

    for i in word:
        if i == "c":
            cnt_c += 1
        elif i == "r":
            cnt_r += 1
        elif i == "o":
            cnt_o += 1
        elif i == "a":
            cnt_a += 1
        else:
            cnt_k += 1

        if not cnt_c >= cnt_r >= cnt_o >= cnt_a >= cnt_k:
            return -1

        else:
            frogs = max([cnt_c, cnt_r, cnt_o, cnt_a, cnt_k]) - min([cnt_c, cnt_r, cnt_o, cnt_a, cnt_k])
            if frogs > result:
                result = frogs

    if not cnt_c == cnt_r == cnt_o == cnt_a == cnt_k:
        return -1

    return result


for tc in range(1, N+1):
    word = input()
    print("#{} {}".format(tc, frog(word)))
