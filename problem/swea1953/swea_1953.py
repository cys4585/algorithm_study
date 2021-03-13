# 탈주법 검거
# 난이도 ?
import sys
sys.stdin = open('input_1953.txt')

def f(y, x, time, cnt):

    for dir in connect[in_map[y][x]]:
        ny, nx = y + direction[dir][0], x + direction[dir][1]
        if 0 <= ny < H and 0 <= nx < W:
            if in_map[ny][nx] == 0: continue
            d = connect[in_map[ny][nx]]


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
    H, W, start_y, start_x, time = map(int, input().split())
    in_map = [list(map(int, input().split())) for _ in range(H)]
    print(H, W, start_y, start_x, time)
    print(in_map)

    f(start_y, start_x, 1, 1)