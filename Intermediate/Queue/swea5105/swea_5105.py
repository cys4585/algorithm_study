# 미로의 거리
# D3
import sys
sys.stdin = open('input_5105.txt')

def function(im_here, cnt):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우
    queue = list()
    queue.append([im_here[0], im_here[1], cnt])
    visited = [[0] * N for _ in range(N)]
    while queue:
        # print(queue)
        # print(visited)
        y, x, cnt = queue.pop(0)
        visited[y][x] = 1
        if in_arr[y][x] == 3: return cnt - 1
        for dir in direction:
            ny, nx = dir[0] + y, dir[1] + x
            if 0 <= ny < N and 0 <= nx < N:
                if in_arr[ny][nx] != 1 and not visited[ny][nx]:
                    queue.append([ny, nx, cnt+1])
    return 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input())) for _ in range(N)]
    # print(tc, N, in_arr)

    # 출발 : 2 / 도착 : 3
    start = None
    for i in range(N):
        for j in range(N):
            if in_arr[i][j] == 2:
                start = (i, j)
                break
    # print(start)

    print('#{} {}'.format(tc, function(start, 0)))
