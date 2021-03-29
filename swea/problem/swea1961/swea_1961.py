# 숫자 배열 회전
# D2
import sys
sys.stdin = open('input_1961.txt')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    # 123 --> 789 --> 987 --> 369
    # 456 --> 852 --> 658 --> 258
    # 789 --> 963 --> 329 --> 987

    # 결과를 담을 리스트
    result_arr = []

    # 90 / 180 / 270 도 => 총 3번 반복
    for _ in range(3):
        # 회전한 값을 담기 위한 임시 리스트
        tmp_arr = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # 90도 돌린 값을 tmp_arr 에 담는다.
                tmp_arr[i][j] = arr[N-1-j][i]
        # 다 담으면 기준 배열을 바꾼다.
        arr = tmp_arr
        # 기준 배열을 결과 리스트에 담는다.
        result_arr.append(arr)

    # 결과 출력
    # 각 배열의 첫번째요소들을 모두 출력하고, 두번째요소들, 세번째요소들, ... 순으로 출력해야한다.
    print('#{}'.format(test_case))
    for i in range(len(result_arr[0])):
        for j in range(3):
            for char in result_arr[j][i]:
                print(char, end='')
            print(end=' ')
        print()
