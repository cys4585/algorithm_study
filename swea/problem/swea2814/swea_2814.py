# 최장 경로 (D3)

# N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.

# 정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.
# 경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며,
# 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.
# 경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.

import sys
sys.stdin = open('input_2814.txt')

# v : vertex (정점)
# cnt : 경로의 길이 (방문한 정점의 수)
def my_func_dfs(v, cnt):
    global max_cnt
    visited[v] = 1
    cnt += 1
    last_vertex = True
    for i in range(1, N + 1):
        if visited[i]: continue
        if adj[v][i]:
            my_func_dfs(i, cnt)
            last_vertex = False
    # 현재 정점이 마지막 정점이면 경로 길이 갱신
    if last_vertex:
        if max_cnt < cnt:
            max_cnt = cnt
    visited[v] = 0


for tc in range(1, int(input()) + 1):
    # 1 <= N <= 10  (정점의 수)
    # 0 <= M <= 20  (간선의 수)
    N, M = map(int, input().split())
    # 0번은 안쓴다. (정점이 1번부터임...)
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj[v1][v2] = 1
        adj[v2][v1] = 1

    visited = [0] * (N + 1)
    max_cnt = 0
    # 경로의 길이 : 경로 상에 등장하는 정점의 개수
    for i in range(1, N+1):
        my_func_dfs(i, 0)
    print('#{} {}'.format(tc, max_cnt))