# 최소 생산 비용 (D3)

# A사는 여러 곳에 공장을 갖고 있다.
# 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

# 각 제품의 공장별 생산비용이 주어질 때
# 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

# 예를 들어 3개의 제품을 생산하려는 경우
# 각 공장별 생산비용은 다음과 같이 주어진다.
#     A    B    C
# 1  73   21    21
# 2  11   59    40
# 3  24   31    83
# 이 때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면
# 생산 비용이 21 + 11 + 31 = 63 으로 최소가 된다.

import sys
sys.stdin = open('input_5209.txt')

# factory : 공장 idx
def permutation(factory, sum_v):
    global min_sum_v
    # 마지막 공장까지 다 조사했으면
    if factory == N:
        # 최소값 갱신하고 종료
        if min_sum_v > sum_v:
            min_sum_v = sum_v
        return
    # 조사 중간에 이미 최소값을 넘었다면 -> 종료
    elif min_sum_v < sum_v:
        return
    # i : product idx
    for i in range(N):
        # 이미 짝이 이루어진 제품은 패스
        if used[i]: continue
        used[i] = 1
        permutation(factory + 1, sum_v + in_arr[i][factory])
        used[i] = 0


for tc in range(1, int(input()) + 1):
    # N : 제품수 = 공장수
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    min_sum_v = 987654321

    permutation(0, 0)

    print('#{} {}'.format(tc, min_sum_v))