import sys
sys.stdin = open('./4875_sample_input.txt', 'r')

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def my_func(visited, maze, now):
    global result
    if maze[now[0]][now[1]] == '3':
        result = 1
        return
    visited[now[0]][now[1]] = 1
    for dy, dx in direction:
        ny, nx = now[0] + dy, now[1] + dx
        if 0 <= ny < N and 0 <= nx < N:
            if maze[ny][nx] == '1': continue
            if visited[ny][nx]: continue
            my_func(visited, maze, [ny, nx])



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    S = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                S = [i, j]
                break
        if S: break

    result = 0
    my_func(visited, maze, S)

    print(f'#{tc} {result}')
