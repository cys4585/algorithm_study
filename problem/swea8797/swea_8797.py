# 당근수확 4
# D2
import sys
sys.stdin = open('input_8797.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 당근밭 N*N (홀수)
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    center = N // 2     # 중간값
    start_idx = 0       # 경계 인덱스
    end_idx = N - 1     # 경계 인덱스
    sum_arr = [0] * 4   # 당근밭 1 2 3 4 영역
    for i in range(N):
        sum_y = 0
        sum_x = 0
        for j in range(start_idx + 1, end_idx):
            sum_y += in_arr[i][j]
            sum_x += in_arr[j][i]
        if i < center:
            start_idx += 1
            end_idx -= 1
            sum_arr[0] += sum_y
            sum_arr[3] += sum_x
        else:
            start_idx -= 1
            end_idx += 1
            sum_arr[2] += sum_y
            sum_arr[1] += sum_x

    print('#{} {}'.format(test_case, max(sum_arr)-min(sum_arr)))