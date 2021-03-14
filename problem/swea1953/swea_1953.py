# 탈주법 검거
# 난이도 ?
import sys
sys.stdin = open('input_1953.txt')

def f(sy, sx, time):
    queue = list()
    queue.append([sy, sx, time])
    while queue:
        y, x, t = queue.pop(0)
        visited[y][x] = 1
        for dir in connect[in_map[y][x]]:
            ny, nx = y + direction[dir][0], x + direction[dir][1]
            if 0 <= ny < H and 0 <= nx < W:
                if dir == '상' and '하' not in connect[in_map[ny][nx]]: continue
                elif dir == '하' and '상' not in connect[in_map[ny][nx]]: continue
                elif dir == '좌' and '우' not in connect[in_map[ny][nx]]: continue
                elif dir == '우' and '좌' not in connect[in_map[ny][nx]]: continue
                if t + 1 <= T and not visited[ny][nx]: queue.append([ny, nx, t + 1])

# 상 : 0 / 하 : 1 / 좌 : 2 / 우 : 3
connect = [[], ['상', '하', '좌', '우'], ['상', '하'], ['좌', '우'], ['상', '우'], ['하', '우'], ['하', '좌'], ['상', '좌']]
# 상 하 좌 우
direction = {
    '상':(-1, 0),
    '하':(1, 0),
    '좌':(0, -1),
    '우':(0, 1)
}

for tc in range(1, int(input()) + 1):
    H, W, start_y, start_x, T = map(int, input().split())
    in_map = [list(map(int, input().split())) for _ in range(H)]
    # print(H, W, start_y, start_x, T)
    # print(in_map)

    visited = [[0] * W for _ in range(H)]

    # time 시간이 흐른 후, 탈주범이 위치할 수 있는 장소의 개수
    f(start_y, start_x, 1)
    cnt = 0
    for i in range(H):
        for j in range(W):
            cnt += visited[i][j]
    print('#{} {}'.format(tc, cnt))