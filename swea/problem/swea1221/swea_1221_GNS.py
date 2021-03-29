import sys
sys.stdin = open("input_1221_GNS.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    tc = input().split()
    input_list = list(input().split())
    len_of_tc = int(tc[1])

    translation = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    ## how 1
    # for i in range(len_of_tc - 1):
    #     min_v = translation.index(input_list[i])
    #     min_i = i
    #     for j in range(i + 1, len_of_tc):
    #         num = translation.index(input_list[j])
    #         if min_v > num:
    #             min_v = num
    #             min_i = j
    #     input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    # print(tc[0])
    # print(*input_list)

    ## how 2
    output_list = []
    for i in range(len(translation)):
        for j in range(len(input_list)):
            if translation[i] == input_list[j]:
                output_list.append(input_list[j])
    print(tc[0])
    print(*output_list)