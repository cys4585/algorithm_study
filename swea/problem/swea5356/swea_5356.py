# 의석이의 세로로 말해요
# D3
# 다른 방법으로 풀기
import sys
sys.stdin = open("input_5356.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = [input() for _ in range(5)]

    max_len = 0
    for str_i in arr:
        if max_len < len(str_i):
            max_len = len(str_i)

    result = ''
    for i in range(max_len):
        for j in range(len(arr)):
            if len(arr[j]) > i:
                result += arr[j][i]

    # 간편하게 풀기도 가능
    # result = ''
    # for i in range(max_len):
    #     for j in range(len(arr)):
    #         try:
    #             result += arr[j][i]
    #         except:
    #             pass

    print('#{} {}'.format(test_case, result))
