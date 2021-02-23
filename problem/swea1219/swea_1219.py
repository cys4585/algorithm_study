# 길찾기
# D4
import sys
sys.stdin = open('input_1219.txt')

def dfs(v):
    # 방문하면, 방문했다는 표시를 남긴다.
    visited[v] = 1
    for i in range(100):
        # 인접행렬이면서, 방문한적이 없는 곳이면 그곳을 방문한다. (함수호출)
        if adj[v][i] and not visited[i]:
            dfs(i)

for _ in range(10):
    test_case, E = map(int, input().split())
    # 노드간의 관계에 대한 정보 (길이 있는 노드들의 정보)
    arr = list(map(int, input().split()))

    # 노드간의 관계를 파악하기 위한 행렬 만들기 (길이 있는지 없는지 확인)
    adj = [([0] * 100) for _ in range(100)]
    # 인접행렬 (단일방향으로만)
    for i in range(0, len(arr), 2):
        adj[arr[i]][arr[i+1]] = 1
    # adj행렬 원소 -> 1이면 길이 있는 것, 0이면 길이 없는 것

    visited = [0] * 100
    dfs(0)

    print('#{} {}'.format(test_case, visited[99]))
