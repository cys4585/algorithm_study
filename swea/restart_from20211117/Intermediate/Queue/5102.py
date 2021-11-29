import sys
sys.stdin = open('./5102_sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    result = 0
    queue = [(S, 0)]
    visited = [0] * (V + 1)
    while queue:
        node, cnt = queue.pop(0)
        visited[node] = 1
        if node == G:
            if not result or result > cnt:
                result = cnt
        else:
            for s, g in edges:
                if s == node and not visited[g]:
                    queue.append((g, cnt + 1))
                elif g == node and not visited[s]:
                    queue.append((s, cnt + 1))
    print(f'#{tc} {result}')
