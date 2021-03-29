# 노드의 거리
# D2
import sys
sys.stdin = open('input_5102.txt')

def function(start_node, count):
    queue = list()
    visited = [0] * (V+1)
    queue.append([start_node, count])
    while queue:
        node, cnt = queue.pop(0)
        visited[node] = 1
        if node == G: return cnt
        for node_num, is_connected in enumerate(adj[node]):
            if is_connected and not visited[node_num]:
                queue.append([node_num, cnt + 1])
    return 0

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    in_arr = []
    for _ in range(E):
        in_arr += map(int, input().split())
    S, G = map(int, input().split())
    # print(V, E, in_arr, 'start:', S, 'goal:', G)

    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(0, E*2, 2):
        adj[in_arr[i]][in_arr[i+1]] += 1
        adj[in_arr[i+1]][in_arr[i]] += 1
    # print(adj)

    print('#{} {}'.format(tc, function(S, 0)))