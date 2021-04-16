# 정사각형 방

# n^2개의 방이 N*N 형태로 늘어서 있다.

# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N^2 이하의 수 Aij가 적혀 있으며,
# 이 숫자는 모든 방에 대해 서로 다르다.

# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.

# 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가
# 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.

# 처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

# 1 <= N <= 10^3
# 1 <= Aij <= N^2

import sys
sys.stdin = open('input_1861.txt')


def visit_room(start_room_num, y, x, cnt):
    global max_cnt
    global room_num
    stack = list()
    stack.append((start_room_num, y, x, cnt))

    # 방문 시작
    while stack:
        start_room_num, y, x, cnt = stack.pop()
        visited[y][x] = 1
        for dir in direction:
            ny, nx = y + dir[0], x + dir[1]
            if 0 <= ny < N and 0 <= nx < N:
                # 여기서는 방문표시가 된 방도 방문을 해야한다.
                # why?
                #   이 함수가 실행됐다는 것은 max_cnt 갱신의 가능성이 있다는 것 (이미 갱신 가능성은 출발지에서 걸러짐)
                #   만약, 이전의 경우에서 4번 방에서 시작해서 (4, 5, 6, ...) 이 카운팅 되어있을 때,
                #   지금의 출발지가 3번 방이라면
                #   [(4번에서 출발한 경우의 cnt) + 1 == (3번방에서 출발한 경우의 cnt)] 이다.
                if in_arr[y][x] + 1 == in_arr[ny][nx]:
                    stack.append((start_room_num, ny, nx, cnt + 1))
    # 방문 종료 후
    # 방문한 방 수, 출발한 방 갱신
    if max_cnt < cnt:
        max_cnt = cnt
        room_num = start_room_num
    elif max_cnt == cnt and room_num > start_room_num:
        max_cnt = cnt
        room_num = start_room_num


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    # 지금 방 번호 + 1 == 다음 방 번호
    # 만약 시작하려고 하는 방이 이미 방문되어 있다면 -> max_cnt를 갱신할 가능성이 없다.
    # 이유 :
    #   만약 4번, 5번방이 붙어있고,
    #   이전에 4번 방에서 출발한 경우를 카운팅 했고,
    #   지금 출발할려고 하는 방이 5번 방 이라고 했을 때
    #   5번 방은 방문표시가 되어있을 것이다. (4번 방에서 출발 했을 때 이미 4, 5를 카운팅 했을 것이다.)
    #   그리고, 그 뒤의 방들(6, 7, 8, ...)도 이미 4번 방에서 출발한 경우에서 카운팅이 되어있다.
    #   그렇다면, [(5번에서 출발한 경우의 cnt) + 1 == (4번방에서 출발한 경우의 cnt)] 이다.
    # 그래서 출발하기 전에 현재 방이 방문되어 있다면 함수를 실행하지 않는다.

    max_cnt = 0
    room_num = 987654321
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 이미 지금의 방이 방문되어 있다면 (카운팅을 한 방이라면) -> continue
            # (이미 다른 방에서 출발한 경우의 카운팅에 포함되어 있는 방이기 때문)
            if visited[i][j]: continue
            visit_room(in_arr[i][j], i, j, 1)

    print(f'#{tc} {room_num} {max_cnt}')