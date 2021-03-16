# 물놀이를 가자
# D4
import sys
sys.stdin = open('input_10966.txt')
from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    in_map = [input() for _ in range(N)]

    result = 0
    water_locs = deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if in_map[i][j] == 'W':
                water_locs.append((i, j, 0))
                visited[i][j] = 1

    while water_locs:
        # print(queue)
        y, x, cnt = water_locs.popleft()
        if in_map[y][x] == 'L': result += cnt
        # print(y, x, cnt, result)
        for dir in direction:
            ny, nx = y + dir[0], x + dir[1]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx]: continue
                visited[ny][nx] = 1
                water_locs.append((ny, nx, cnt + 1))

    print('#{} {}'.format(tc, result))