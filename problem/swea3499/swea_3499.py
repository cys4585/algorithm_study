# 퍼펙트 셔플
# D3

import sys
sys.stdin = open('input_3499.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    card_arr = input().split()

    # 반 나누기 (홀수개면 -> 앞부분이 한개 더 가진다)
    half = len(card_arr) // 2
    if len(card_arr) % 2:
        half += 1

    # # how 1 : 반을 나눠서 옮겨담고, 그걸 다시 합친다.
    # tmp_arr_1 = card_arr[:half]
    # tmp_arr_2 = card_arr[half:]
    #
    # # 카드를 하나씩 가져와서 저장
    # for i in range(len(card_arr)):
    #     if i % 2 == 0:
    #         card_arr[i] = tmp_arr_1.pop(0)
    #     else:
    #         card_arr[i] = tmp_arr_2.pop(0)
    # print('#{}'.format(test_case), *card_arr)

    # how 2 : index를 이용해서 반을 나누는 작업을 생략한다.
    result_arr = []
    for i in range(half):
        result_arr.append(card_arr[i])
        # 마지막 i+half는 리스트의 범위를 넘어가기 때문에
        if i + half < len(card_arr):
            result_arr.append(card_arr[i+half])

    print('#{}'.format(test_case), *result_arr)