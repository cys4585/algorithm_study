# 회전
# D2

import sys
sys.stdin = open('input_5097.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    in_arr = list(map(int, input().split()))
    # print(tc, N, M, in_arr)

    for i in range(M):
        in_arr.append(in_arr.pop(0))
    print('#{} {}'.format(tc, in_arr[0]))