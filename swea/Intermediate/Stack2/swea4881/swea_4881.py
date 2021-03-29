# 배열 최소 합
# D2

import sys
sys.stdin = open('input_4881.txt')

# y = 행, sum_v = 합
def function(y, sum_v):
    global result
    if result < sum_v: return   # result 보다 sum_v가 크면 -> 더 검사할 필요가 없음 -> 그냥 return (시간을 줄이기 위한 코드)
    if y == N:  # 마지막 행까지 검사를 다 했으면
        if result > sum_v:  # 더한 값이 최소합인지 조사하고, 최소합이면 result를 갱신한다.
            result = sum_v
        return
    for x in range(N):  # 열 반복
        if not used_x[x]:   # 그 열을 사용하지 않았다면
            sum_v += in_arr[y][x]   # 합에 그 열의 값을 더한다.
            used_x[x] = True        # 그 열을 사용했다고 표시
            function(y+1, sum_v)    # 그 다음 행에서 열들을 조사한다. (사용한 열은 체크했기 때문에 조사하지 않음)
            sum_v -= in_arr[y][x]   # 다른 조합을 검사하는데 방해주지 않기 위해 더해준 값을 그대로 빼준다.
            used_x[x] = False       # 조사가 끝났기 때문에 사용했다고 표시한 것을 다시 원래대로 돌려준다.


for test_case in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    used_x = [False] * N    # 사용한 열(x)을 체크하기 위한 배열
    result = 987654321      # 최소 합을 담기 위한 변수
    function(0, 0)

    print('#{} {}'.format(test_case, result))