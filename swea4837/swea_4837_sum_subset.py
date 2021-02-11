import sys

sys.stdin = open("input_4837_sum_subset.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # 집합 A의 부분 집합 중
    # 원소의 갯수가 N개, 원소들의 합이 K인 부분집합의 갯수 출력하기
    N, K = map(int, input().split())

    result = 0

    my_list = []
    bit = [0] * 12
    for a in range(2):
        bit[0] = a
        for b in range(2):
            bit[1] = b
            for c in range(2):
                bit[2] = c
                for d in range(2):
                    bit[3] = d
                    for e in range(2):
                        bit[4] = e
                        for f in range(2):
                            bit[5] = f
                            for g in range(2):
                                bit[6] = g
                                for h in range(2):
                                    bit[7] = h
                                    for i in range(2):
                                        bit[8] = i
                                        for j in range(2):
                                            bit[9] = j
                                            for k in range(2):
                                                bit[10] = k
                                                for l in range(2):
                                                    bit[11] = l
                                                    tmp = 0
                                                    for bit_1 in bit:
                                                        if bit_1 == 1:
                                                            tmp += 1
                                                    if tmp == N:
                                                        list_4 = [0] * 12
                                                        for ii in range(12):
                                                            list_4[ii] = bit[ii]
                                                        my_list.append(list_4)

    for list_4 in my_list:
        A_subset = []
        for i in range(len(list_4)):
            if list_4[i] == 1:
                A_subset.append(A[i])
        sum_v = 0
        for a in A_subset:
            sum_v += a
        if sum_v == K:
            result += 1

    print('#{} {}'.format(test_case, result))