# 최소합 D3

# N * N 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른족이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면
# 이 때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

# 1 2 3
# 2 3 4
# 3 4 5
# 위 경우, 1 2 3 4 5 순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

import sys
sys.stdin = open('input_5188.txt')

direction = [(1, 0), (0, 1)]

def brute_force(y, x, sum_v):
    global result
    sum_v += in_arr[y][x]
    # 도착했으면
    if y == N-1 and x == N-1:
        # 이때까지의 최소합과 지금의 합을 비교해서 최소합 갱신
        if result > sum_v:
            result = sum_v
        return
    # 도착 안했는데 지금까지의 합이 최소합을 넘어서면 -> 이쪽 방향은 가망 X
    elif result < sum_v:
        return

    # 2방향 탐색 (하, 우)
    for dir in direction:
        dy, dx = dir
        ny, nx = y + dy, x + dx
        if ny < N and nx < N:
            brute_force(ny, nx, sum_v)


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    result = 987654321
    brute_force(0, 0, 0)

    print('#{} {}'.format(tc, result))