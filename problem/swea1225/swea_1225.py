# 암호생성기
# D3

import sys
sys.stdin = open('input_1225.txt')
for _ in range(10):
    tc = int(input())
    in_arr = list(map(int, input().split()))
    # print(tc, in_arr)

    # 한 사이클
    flag = True
    while flag:
        for sub_num in range(1, 6):
            num = in_arr.pop(0) - sub_num
            if num <= 0:
                num = 0
                in_arr.append(num)
                flag = False
                break
            in_arr.append(num)
    print('#{}'.format(tc), *in_arr)