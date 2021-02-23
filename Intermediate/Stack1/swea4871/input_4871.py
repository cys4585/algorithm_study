# 그래프 경로
# D2

import sys
sys.stdin = open('input_4871.txt')

def dfs(v):
    visited[v] = 1
    for i in range(1, V+1):
        if adj[v][i] == 1 and not visited[i]:
            dfs(i)

T = int(input())
for test_case in range(1, T+1):
    # V : 노드
    # E : 간선 (Edge)
    V, E = map(int, input().split())
    # edges : 간선 정보
    edges = [list(map(int, input().split())) for _ in range(E)]
    # S : 출발 노드
    # G : 도착 노드
    S, G = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1)]

    # 방향성 그래프이기 때문에,
    # adj[i][j] = 1는 하고
    # adj[j][i] = 1은 하면 안된다. (이는 양방향 경로인 경우에 하는 것)
    for edge in edges:
        i, j = edge[0], edge[1]
        adj[i][j] = 1

    visited = [0] * (V+1)

    dfs(S)

    print('#{} {}'.format(test_case, visited[G]))
