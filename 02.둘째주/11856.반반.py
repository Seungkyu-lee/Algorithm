import sys

sys.stdin = open('11856.txt', 'r')

for tc in range(1,1+int(input())):
    S = input()
    end = False
    for i in S:
        if S.count(i) == 2:
            pass
        else:
            end = True
            break

    if end ==True:
        print('#{} {}'.format(tc,'No'))
    else:
        print('#{} {}'.format(tc, 'Yes'))