import sys

sys.stdin = open('1861.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    room = 999999999999

    for x in range(N):
        for y in range(N):
            cnt = 1
            q = [(x, y)]
            while q:
                qq = q.pop()
                for i in range(4):
                    nr = qq[0] + dx[i]
                    nc = qq[1] + dy[i]
                    if 0 <= nr < N and 0 <= nc < N and (mapp[nr][nc] - mapp[qq[0]][qq[1]]) == 1:
                        cnt += 1
                        q.append((nr, nc))
            if cnt > max_cnt:
                max_cnt = cnt
                room = mapp[x][y]
            elif cnt == max_cnt:
                if mapp[x][y] < room:
                    room = mapp[x][y]
    print('#{} {} {}'.format(tc, room, max_cnt))
