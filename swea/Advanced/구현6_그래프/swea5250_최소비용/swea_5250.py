# 최소 비용 (D3)

# 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에,
# 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

# 다음은 각 지역의 높이를 기록한 표의 예로,
# 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며,
# 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.
# (표에 표시되지 않은 지역이나 대각병 방향으로는 이동 불가)
# 0 2 1
# 0 1 1
# 1 1 1

# 인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고,
# 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.

# 이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('input_5250.txt')

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def my_func(start_y, start_x):
    global min_cost
    INF = 0xffffff
    costs = [[INF] * N for _ in range(N)]
    costs[start_y][start_x] = 0

    queue = list()
    queue.append((start_y, start_x))
    while queue:
        y, x = queue.pop(0)
        cost = costs[y][x]
        # 도착지 도달하면 최소비용 갱신
        if y == N-1 and x == N-1:
            if min_cost > cost:
                min_cost = cost
        # 현 위치에서 4방향 탐색 (상하좌우)
        for dir in direction:
            nr, nc = y + dir[0], x + dir[1]
            # 배열 범위만 탐색
            if 0 <= nr < N and 0 <= nc < N:
                # 현 위치에서 다음 위치로 가는데 드는 비용 조사
                tmp_cost = cost + 1
                # 다음 위치의 높이가 더 높으면 비용 추가
                if in_arr[nr][nc] > in_arr[y][x]:
                    tmp_cost += (in_arr[nr][nc] - in_arr[y][x])
                # 다음 위치로 가는 다른 경로와 비교해서 비용 갱신,
                # 갱신 될 때만 다시 queue에 넣어준다.
                if costs[nr][nc] > tmp_cost:
                    costs[nr][nc] = tmp_cost
                    queue.append((nr, nc))


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 0xffffff
    my_func(0, 0)
    print('#{} {}'.format(tc, min_cost))