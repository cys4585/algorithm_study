# 보급로
# D4
import sys
sys.stdin = open('input_1249.txt')

def function(start_y, start_x):
    queue = list()
    queue.append([start_y, start_x, in_map[start_y][start_x]])

    while queue:
        now_y, now_x, now_time = queue.pop(0)
        # print(now_y, now_x, now_time)
        if working_time[now_y][now_x] < now_time: continue

        for dir in direction:
            ny, nx = now_y + dir[0], now_x + dir[1]
            if 0 <= ny < N and 0 <= nx < N:
                if working_time[ny][nx] > now_time + in_map[ny][nx]:
                    working_time[ny][nx] = now_time + in_map[ny][nx]
                    queue.append([ny, nx, working_time[ny][nx]])


direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌

for tc in range(1, int(input()) + 1):
    N = int(input())
    in_map = [list(map(int, input())) for _ in range(N)]
    # print(N, in_map)

    # S(출발지): 좌상단, G(도착지):우하단
    # S -> G 로가는 경로 중 복구 시간이 가장 짧은 경로의 총 복구 시간 구하기
    # 이동경로 : 상 하 좌 우 / 한 칸씩

    working_time = [[987654321] * N for _ in range(N)]
    # print(working_time)
    function(0, 0)
    print('#{} {}'.format(tc, working_time[N-1][N-1]))