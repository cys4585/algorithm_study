import sys
sys.stdin = open('./5209_sample_input.txt', 'r')


def permutation(factory_n, sum_v):
    global min_sum_v
    if factory_n == N:
        if min_sum_v > sum_v: min_sum_v = sum_v
        return
    if min_sum_v < sum_v: return

    for product_n in range(N):
        if used[product_n]: continue
        used[product_n] = 1
        permutation(factory_n + 1, sum_v + in_arr[product_n][factory_n])
        used[product_n] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    min_sum_v = 987654321

    permutation(0, 0)

    print(f'#{tc} {min_sum_v}')