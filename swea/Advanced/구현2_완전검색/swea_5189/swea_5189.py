# 전자카트

# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

# 각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을 ,2번 부터 N번은 관리구역 번호이다.

# 두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

# N이 3인 경우 가능한 경우 가능한 경로는 1-2-3-1, 1-3-2-1 이며
# 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.
# 0 18 34
# 48 0 55
# 18 7 0
# e[1][2] + e[2][3] + e[3][1] = 18 + 55 + 18 = 91
# e[1][3] + e[3][2] + e[2][1] = 34 + 7 + 48 = 89

import sys
sys.stdin = open('input_5189.txt')


def function(idx, sum_v):
    global min_v
    if 0 not in visited:
        if min_v > sum_v:
            min_v = sum_v
        return
    for i in range(N):
        if i == idx: continue
        if visited[i]: continue
        if i == 0 and 0 in visited[1:]: continue
        visited[i] = 1
        function(i, sum_v + in_arr[idx][i])
        visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_v = 987654321
    function(0, 0)

    print(f'#{tc} {min_v}')