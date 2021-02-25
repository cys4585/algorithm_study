# 스도쿠 검증
# D2
import sys
sys.stdin = open('input_1974.txt')
T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 1 + 2 + ... + 9 = 45

    for i in range(len(arr)):
        hori = 0
        ver = 0
        for j in range(len(arr)):
            hori += arr[i][j]
            ver += arr[j][i]
        if hori != 45 or ver != 45:
            result = 0
            break
    else:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        box += arr[k][l]
                if box != 45:
                    result = 0
                    break
                # 0 0 / 0 3 / 0 6
                # 3 0 / 3 3 / 6 3
                # 6 0 / 6 3 / 6 6
    print('#{} {}'.format(test_case, result))