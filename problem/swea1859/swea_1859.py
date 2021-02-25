# 백만 장자 프로젝트
# D2
import sys
sys.stdin = open('input_1859.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0

    max_v = 0
    for i in range(len(arr)-1, -1, -1):
        if max_v < arr[i]:
            max_v = arr[i]
        else:
            result = result + (max_v - arr[i])

    print('#{} {}'.format(test_case, result))
