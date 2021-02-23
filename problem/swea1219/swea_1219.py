# 길찾기
# D4
import sys
sys.stdin = open('input_1219.txt')

def dfs(v):
    visited[v] = 1
    for i in range(100):
        if adj[v][i] and not visited[i]:
            dfs(i)

for _ in range(10):
    test_case, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adj = [([0] * 100) for _ in range(100)]

    for i in range(0, len(arr), 2):
        adj[arr[i]][arr[i+1]] = 1

    visited = [0] * 100
    dfs(0)

    print('#{} {}'.format(test_case, visited[99]))
