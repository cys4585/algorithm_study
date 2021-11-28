import sys
sys.stdin = open('./5105_sample_input.txt', 'r')

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    S = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                S = (i, j, 0)
                break
        if S: break

    queue = [S]
    visited = [[0] * N for _ in range(N)]
    result = 0
    while queue:
        y, x, cnt = queue.pop(0)
        if maze[y][x] == 3:
            result = cnt - 1
            break
        visited[y][x] = 1
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] == 1 or visited[ny][nx]: continue
                queue.append((ny, nx, cnt + 1))
    print(f'#{tc} {result}')
