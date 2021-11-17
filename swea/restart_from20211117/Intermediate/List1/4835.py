import sys
sys.stdin = open("./4835_sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # N: 정수의 개수 (10 <= N <= 100)
    # M: 구간의 개수 (2 <= M < N)
    N, M = list(map(int, input().split()))
    # n_list: N개의 정수
    n_list = list(map(int, input().split()))

    max_v, min_v = 0, 0
    for i in range(M):
        max_v += n_list[i]
        min_v += n_list[i]

    last = N - M + 1
    for i in range(1, last):
        sum_v = 0
        for j in range(i, i + M):
            sum_v += n_list[j]
        if max_v < sum_v: max_v = sum_v
        elif sum_v < min_v: min_v = sum_v

    print(f'#{tc} {max_v - min_v}')