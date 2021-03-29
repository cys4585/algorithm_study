# 원재의 메모리 복구하기
# D3

import sys
sys.stdin = open("input_1289.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    bit_arr = list(map(int, input()))

    init_arr = [0] * len(bit_arr)

    cnt = 0
    for i in range(len(bit_arr)):
        if bit_arr[i] == 0:
            if init_arr[i] == 1:
                for j in range(i, len(bit_arr)):
                    init_arr[j] = 0
                cnt += 1
        else:
            if init_arr[i] == 0:
                for j in range(i, len(bit_arr)):
                    init_arr[j] = 1
                cnt += 1

    print('#{} {}'.format(test_case, cnt))