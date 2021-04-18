# 장훈이의 높은 선반

# 서점에는 높이가 B인 선반이 하나 있는데 장훈이는 키가 매우 크기 때문에,
# 선반 위의 물건을 자유롭게 사용할 수 있다.

# 어느 날 장훈이는 자리를 비웠고, 이 서점에 있는 N명의 점원들이
# 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생겼다.

# 각 점원의 키는 Hi로 나타나는데, 점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 하였다.

# 점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.

# 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고,
# 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.

# 탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데
# 탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서
# 높이가 가장 낮은 탑을 알아내려고 한다.

import sys
sys.stdin = open('input_1486.txt')


def function(idx, sum_v):
    global min_v
    if sum_v >= B:
        if min_v > sum_v:
            min_v = sum_v
        return
    for i in range(idx, N):
        if used[i]: continue
        used[i] = 1
        function(i, sum_v + in_arr[i])
        used[i] = 0


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    # 1 <= N <= 20
    # 1 <= B <= S
    # S : 점원들 키의 합
    in_arr = list(map(int, input().split()))

    used = [0] * N
    min_v = 987654321
    function(0, 0)

    print(f'#{tc} {min_v - B}')