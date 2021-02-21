# 농작물 수확하기
# D3

import sys
sys.stdin = open("input_2805.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    center_row = N // 2
    start_col = N // 2
    width = 1

    result = 0

    for row in range(N):
        for wid in range(width):
            result += arr[row][start_col + wid]
        if row < center_row:
            width += 2
            start_col -= 1
        else:
            width -= 2
            start_col += 1

    print('#{} {}'.format(test_case, result))