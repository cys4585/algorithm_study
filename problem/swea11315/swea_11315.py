# 오목 판정
# D3
import sys
sys.stdin = open('input_11315.txt')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    # 가로 -> 열 조사
    # 세로 -> 행 조사
    # 대각 \ -> row+1 col+1
    # 대각 / -> row+1 col-1

    # 다섯개 이상 연속하면 YES
    # 4개 이하면 NO
    result = 'NO'

    # 가로, 세로 검사
    for i in range(N):
        horizontal_cnt = 0
        vertical_cnt = 0
        for j in range(N):
            # 가로 바둑돌 조사
            if arr[i][j] == 'o':
                horizontal_cnt += 1
            else:
                horizontal_cnt = 0
            # 5번 연속하면
            if horizontal_cnt == 5:
                result = 'YES'

            # 세로 조사
            if arr[j][i] == 'o':
                vertical_cnt += 1
            else:
                vertical_cnt = 0
            # 5번 연속하면
            if vertical_cnt == 5:
                result = 'YES'

    # 대각선 \, / 검사
    for k in range(N - 4):
        for i in range(N - 4):
            row = k
            # \ 방향
            diagonal_cnt_1 = 0
            # / 방향
            diagonal_cnt_2 = 0
            for j in range(i, i + 5):
                # \ 방향
                if arr[row][j] == 'o':
                    diagonal_cnt_1 += 1
                else:
                    diagonal_cnt_1 = 0
                if diagonal_cnt_1 == 5:
                    result = 'YES'
                # / 방향
                if arr[row][N - j - 1] == 'o':
                    diagonal_cnt_2 += 1
                else:
                    diagonal_cnt_2 = 0
                if diagonal_cnt_2 == 5:
                    result = 'YES'

                row += 1

    print('#{} {}'.format(test_case, result))