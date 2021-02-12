import sys

sys.stdin = open("input_4843_special_sort.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    original_list = list(map(int, input().split()))

    for i in range(len(original_list)):
        if i % 2:
            min_v = original_list[i]
            min_i = i
            for index, value in enumerate(original_list[i:]):
                if min_v > value:
                    min_v = value
                    min_i = index + i
            original_list[i], original_list[min_i] = original_list[min_i], original_list[i]
        else:
            max_v = original_list[i]
            max_i = i
            for index, value in enumerate(original_list[i:]):
                if max_v < value:
                    max_v = value
                    max_i = index + i
            original_list[i], original_list[max_i] = original_list[max_i], original_list[i]

    print('#{}'.format(test_case), end=' ')

    for i in range(10):
        print(original_list[i], end=' ')
    print()