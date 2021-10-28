import sys

sys.stdin = open('5251.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))

    # 너비우선 탐색
    D = [0Xffffff] * (N + 1)  # 초기값은 큰값으로 출발점은 0
    Q = [0]
    D[0] = 0

    while Q:
        u = Q.pop()
        # u의 인접 정점에 대해서
        for v, w in G[u]:  # u,v에 연결되어있는 노트 탐색
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                Q.append(v)

    print('#{} {}'.format(tc, D[N]))
