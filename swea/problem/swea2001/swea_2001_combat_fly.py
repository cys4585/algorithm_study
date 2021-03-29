import sys
sys.stdin = open("input_2001_combat_fly.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # N : 영역
    # M : 파리채 크기
    N, M = map(int, input().split())
    # N * N 배열 (원소는 파리의 마리수를 의미)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 5 <= N <= 15
    # 2 <= M <= N
    # 각 영역의 파리의 마리수는 30 이하

    # 파리채를 한번 내리쳤을 때 잡을 수 있는 파리의 최대값 구하기

    max_v = 0
    # row
    for i in range(N - M + 1):
        # col
        for j in range(N - M + 1):
            sum_v = 0
            # 파리채 row
            for k in range(i, M + i):
                # 파리채 col
                for l in range(j, M + j):
                    sum_v += arr[k][l]
            if max_v < sum_v:
                max_v = sum_v
    print('#{} {}'.format(test_case, max_v))