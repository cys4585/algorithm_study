# 미로1
# D4
import sys
sys.stdin = open('input_1226.txt')

def function(start):
    visited = [[0] * 16 for _ in range(16)]
    queue = list()
    queue.append(start)
    while queue:
        y, x = queue.pop(0)
        visited[y][x] = 1
        if maze[y][x] == '3': return 1
        for dir in direction:
            ny, nx = y + dir[0], x + dir[1]
            if maze[ny][nx] != '1' and not visited[ny][nx]:
                queue.append([ny, nx])
    return 0

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우

for _ in range(10):
    tc = int(input())
    maze = [input() for _ in range(16)]
    # print(tc, in_arr)

    S = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '2': S = [i, j]
    # print(start)

    print('#{} {}'.format(tc, function(S)))