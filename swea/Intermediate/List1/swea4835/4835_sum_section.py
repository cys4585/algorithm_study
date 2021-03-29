import sys

sys.stdin = open("input_4835_sum_section.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N : 정수의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    # nums_list : N개의 정수 리스트
    nums_list = list(map(int, input().split()))

    # # 내가 푼 풀이
    # sum_min = 0
    # sum_max = 0
    #
    # for i in range(N - M + 1):
    #     if i == 0:
    #         for j in range(M):
    #             sum_min += nums_list[j]
    #         sum_max = sum_min
    #     else:
    #         sum_tmp = 0
    #         for j in range(i, i+M):
    #             sum_tmp += nums_list[j]
    #         # for j in range(M):
    #         #     sum_tmp += nums_list[i+j]
    #         # for j in nums[i:i+M]:
    #         #     sum_tmp += j
    #
    #         if sum_tmp < sum_min:
    #             sum_min = sum_tmp
    #         if sum_tmp > sum_max:
    #             sum_max = sum_tmp
    #
    # print('#{} {}'.format(test_case, sum_max-sum_min))

    # 수업에서 푼 풀이
    sum_v = 0
    for i in range(M):
        sum_v += nums_list[i]

    sum_max = sum_v
    sum_min = sum_v

    # sum_v 에서 다음 부분을 더하고, 첫 부분을 빼면 다음 구간의 합을 구할 수 있음
    for i in range(M, N):
        sum_v = sum_v + nums_list[i] - nums_list[i - M]

        if sum_max < sum_v:
            sum_max = sum_v
        if sum_min > sum_v:
            sum_min = sum_v

    print('#{} {}'.format(test_case, sum_max - sum_min))