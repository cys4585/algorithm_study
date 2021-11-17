import sys
sys.stdin = open('./4837_sample_input.txt', 'r')

import itertools

A = [i for i in range(1, 13)]

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))

    combi = list(itertools.combinations(A, N))
    cnt  = 0
    for sub in combi:
        if sum(sub) == K: cnt += 1

    print(f'#{tc} {cnt}')