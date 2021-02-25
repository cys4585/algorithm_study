# 당근밭 옆 고구마밭
# D2
import sys
sys.stdin = open('input_8810.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    in_arr = list(map(int, input().split()))

    gin_julgi_flag = True
    gin_julgi_cnt = 0
    max_length = 0
    sum_length = 0
    max_v = 0
    sum_v = 0
    for i in range(N):
        sum_length += 1
        sum_v += in_arr[i]
        if i != N-1:
            if in_arr[i] < in_arr[i+1]:
                if gin_julgi_flag:
                    gin_julgi_cnt += 1
                    gin_julgi_flag = False
            else:
                gin_julgi_flag = True
                if max_length < sum_length:
                    max_length = sum_length
                    max_v = sum_v
                elif max_length == sum_length and max_v < sum_v:
                    max_v = sum_v
                sum_length = 0
                sum_v = 0
        else:
            if max_length < sum_length:
                max_length = sum_length
                max_v = sum_v
            elif max_length == sum_length and max_v < sum_v:
                max_v = sum_v
            sum_length = 0
            sum_v = 0
    if max_length == 1:
        max_v = 0

    print('#{} {} {}'.format(test_case, gin_julgi_cnt, max_v))