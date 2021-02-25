# 진기의 최고급 붕어빵
# D3
import sys
sys.stdin = open('input_1860.txt')
T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)

    # N : 붕어빵 구매자 수
    # arr : 각 구매자 도착시간
    # 0초부터 빵을 만들기 시작, M초의 시간 동안 K개의 붕어빵을 만든다.
    # 구매자는 하나씩만 사는거라고 가정. 조건이 없으니

    result = 'Possible'

    if M > arr[0]:
        result = 'Impossible'
    else:
        for i in range(len(arr)):
            arr[i] = arr[i]//M
        M = 1

        fish = 0
        for i in range(1, arr[-1]):
            fish += K
            buyer = arr.count(i)
            if buyer > fish:
                result = 'Impossible'
                break
            fish -= buyer
    print('#{} {}'.format(test_case, result))