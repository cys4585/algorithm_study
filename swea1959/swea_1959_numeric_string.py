import sys

sys.stdin = open("input_1959_numeric_string.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_1 = list(map(int, input().split()))
    list_2 = list(map(int, input().split()))

    # Ai : 짧은 문자열, Bj : 긴 문자열
    Ai = []
    Bj = []
    if N <= M:
        Ai = list_1
        Bj = list_2
    else:
        Ai = list_2
        Bj = list_1

    max_v = 0

    for i in range(len(Bj) - len(Ai) + 1):
        sum_num = 0
        for j in range(len(Ai)):
            sum_num += Ai[j] * Bj[i + j]

        if i == 0:
            max_v = sum_num
        elif max_v < sum_num:
            max_v = sum_num

    print('#{} {}'.format(test_case, max_v))



