import sys
sys.stdin = open('./4881_sample_input.txt', 'r')

def my_func(row, sum_value):
    global min_value
    if min_value and min_value < sum_value:
        return
    if row == N:
        if not min_value or min_value > sum_value:
            min_value = sum_value
        return

    for i in range(N):
        if used_col[i] == 1: continue
        used_col[i] += 1
        my_func(row + 1, sum_value + arr_2d[row][i])
        used_col[i] -= 1

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr_2d = [list(map(int, input().split())) for _ in range(N)]

    min_value = None

    used_col = [0] * N
    my_func(0, 0)
    print(f'#{tc} {min_value}')
