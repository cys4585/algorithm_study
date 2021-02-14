import sys

sys.stdin = open("input_4828_min_max.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # # 내가 푼 풀이
    # min_v = nums[0]
    # max_v = nums[0]
    #
    # for i in range(1, N):
    #     if min_v > nums[i]:
    #         min_v = nums[i]
    #     if max_v < nums[i]:
    #         max_v = nums[i]
    #
    # print('#{} {}'.format(test_case, max_v - min_v))

    # 버블 정렬로 풀기
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print('#{} {}'.format(test_case, nums[-1]-nums[0]))