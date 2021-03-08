# 보급로
# D4
import sys
sys.stdin = open('input_1249.txt')

def function(S, G):
    y, x = S
    for dir in direction:
        ny, nx = dir[0] + y, dir[1] + x
        if y <= G[0] and x <= G[1]:
            function([ny, nx], G)



next = (1, 1)
direction = [(1, 0), (0, 1)]  # 하 우

for tc in range(1, int(input()) + 1):
    N = int(input())
    in_map = [list(map(int, input())) for _ in range(N)]
    # print(N, in_map)

    # S(출발지): 좌상단, G(도착지):우하단
    # S -> G 로가는 경로 중 복구 시간이 가장 짧은 경로의 총 복구 시간 구하기
    # 이동경로 : 상 하 좌 우 / 한 칸씩

    G = (N-1, N-1)
    visited = [[0] * N for _ in range(N)]
    min_v = 987654321
    function([0, 0], [0, 1])
    print('#{} {}'.format(tc, min_v))