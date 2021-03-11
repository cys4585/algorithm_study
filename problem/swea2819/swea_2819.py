# 격자판의 숫자 이어 붙이기
# D4
import sys
sys.stdin = open('input_2819.txt')

def function(y, x, number):
    # print(y, x, number, len(cases))
    if len(number) == 7:
        cases.add(number)
        return

    for dir in direction:
        ny, nx = y + dir[0], x + dir[1]
        if 0 <= ny < N and 0 <= nx < N:
            function(ny, nx, number + in_grid[ny][nx])

N = 4
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # 상 하 좌 우

for tc in range(1, int(input()) + 1):
    # size : 4 * 4
    # data : 0 ~ 9 사이의 숫자
    # 임의의 위치에서 시작, 동서남북으로 인접한 위치로 총 여섯번 이동, 각 칸에 적혀있는 숫자를 차례대로 이어붙인다 (총7자리의 수가됨)
    # 한 번 거쳤던 격자칸을 다시 겨처도 됨, 0으로 시작하는 0102001 같은 수도 괜찮음
    in_grid = [input().split() for _ in range(4)]
    # print(in_grid)

    # 만들 수 있는 서로 다른 일곱 자리 수들의 개수 구하기
    cases = set()
    for i in range(N):
        for j in range(N):
            function(i, j, in_grid[i][j])
    print('#{} {}'.format(tc, len(cases)))