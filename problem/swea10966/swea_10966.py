# 물놀이를 가자
# D4
import sys
sys.stdin = open('input_10966.txt')

def find_water(sy, sx, scnt):
    queue = list()
    queue.append([sy, sx, scnt])
    visited = [[0] * M for _ in range(N)]
    while queue:
        y, x, cnt = queue.pop(0)
        visited[y][x] = 1
        if in_map[y][x] == 'L':
            if cnt_arr[y][x] == 0 or cnt_arr[y][x] > cnt:
                cnt_arr[y][x] = cnt
        for dir in direction:
            ny, nx = y + dir[0], x + dir[1]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx]: continue
                queue.append([ny, nx, cnt + 1])

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    in_map = [list(map(str, input())) for _ in range(N)]
    # print(N, M, in_map)

    # 땅으로 표현된 모든 칸(L)에서 어떤 물인 칸(W)으로 이동하기 위한 최소 이동 횟수 구하기
    # 그 이동 횟수의 총합을 출력

    cnt_arr = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if in_map[i][j] == 'W': find_water(i, j, 0)

    result = 0
    for i in range(N):
        for j in range(M):
            result += cnt_arr[i][j]
    print('#{} {}'.format(tc, result))