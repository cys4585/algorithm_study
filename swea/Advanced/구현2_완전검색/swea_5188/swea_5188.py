# 최소합

# N*N 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면,
# 이 때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

# 1 2 3
# 2 3 4
# 3 4 5
# 그림의 경우 1 2 3 4 5 순으로 움직이고 최소합계는 15가 된다.
# 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

import sys
sys.stdin = open('input_5188.txt')


def function(y, x, sum_v):
    global max_v
    if y == N - 1 and x == N - 1:
        if max_v > sum_v:
            max_v = sum_v
        return
    elif max_v < sum_v:
        return

    for dir in direction:
        ny, nx = y + dir[0], x + dir[1]
        if ny < N and nx < N:
            function(ny, nx, sum_v + in_arr[ny][nx])


direction = [(1, 0), (0, 1)]

for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 987654321
    function(0, 0, in_arr[0][0])

    print(f'#{tc} {max_v}')