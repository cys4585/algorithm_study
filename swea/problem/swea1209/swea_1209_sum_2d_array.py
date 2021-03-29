import sys
sys.stdin = open("input_1209_sum_2d_array.txt", "r")
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    input_list = []
    for i in range(100):
        input_list.append(list(map(int, input().split())))

    max_v, diagonal_sum_v_1, diagonal_sum_v_2 = 0, 0, 0
    for i in range(100):
        row_v, col_v = 0, 0
        for j in range(100):
            if i == j:
                diagonal_sum_v_1 += input_list[i][j]
            if i + j == len(input_list) - 1:
                diagonal_sum_v_2 += input_list[i][j]
            row_v += input_list[i][j]
            col_v += input_list[j][i]
        if max_v < row_v:
            max_v = row_v
        if max_v < col_v:
            max_v = col_v

    if max_v < diagonal_sum_v_1:
        max_v = diagonal_sum_v_1
    if max_v < diagonal_sum_v_2:
        max_v = diagonal_sum_v_2

    print('#{} {}'.format(test_case, max_v))
