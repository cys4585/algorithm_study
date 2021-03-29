import sys
sys.stdin = open("input_1979_where_word.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # N : 퍼즐 사이즈
    # K : 문자 길이
    # 5 <= N <= 15
    # 2 <= K <= N
    N, K = map(int, input().split())

    # # 아직 못 푼 문제...
    # # N * N 배열
    # arr = [list(map(int, input().split())) for _ in range(N)]
    #
    # cnt = 0
    #
    # right = (0, 1)
    # down = (1, 0)
    #
    # r = 0
    # c = 0
    # while True:
    #     if arr[r][c]:
    #         r += right[0]
    #         r += right[1]
