# 등산로 조성
# 난이도 ?
import sys
sys.stdin = open('input_1949.txt')

# y,x : 좌표
# k : 공사 가능 높이
# cnt : 이동한 횟수
def f(y, x, k, cnt):
    global max_cnt
    last = True     # 현재 위치가 마지막 위치인지 판단할 변수
    for dir in direction:
        ny, nx = y + dir[0], x + dir[1]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx]: continue    # 이미 방문한 곳은 가지 않는다.
            # 현재 위치보다 높이가 낮은 곳이면
            if in_map[y][x] > in_map[ny][nx]:
                last = False    # 지금이 마지막 위치가 아니다.
                visited[ny][nx] = 1     # 방문 표시
                f(ny, nx, k, cnt + 1)
                visited[ny][nx] = 0     # 다른 케이스에 영향을 안주기 위해 다시 0을 준다.
            # 다음 위치를 공사했을 때 이동할 수 있다면
            elif in_map[y][x] > in_map[ny][nx] - k:
                    last = False    # 지금이 마지막 위치가 아니다.
                    tmp = in_map[ny][nx]    # 다른 케이스에 영향을 안주기 위해 지금 값을 보관
                    in_map[ny][nx] = in_map[y][x] - 1   # 공사
                    visited[ny][nx] = 1     # 방문 표시
                    f(ny, nx, 0, cnt + 1)   # k=0 -> 이제 공사를 하지 못함
                    visited[ny][nx] = 0     # 다른 케이스에 영향 안주기 위해
                    in_map[ny][nx] = tmp    # 보관해둔 값으로 다시 복원 (다른 케이스 조사를 위해)
    # for 반복문이 끝났는데 last == True 이면 더이상 이동할 곳이 없는 것임
    if last:
        if cnt > max_cnt:
            max_cnt = cnt


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우

for tc in range(1, int(input()) + 1):
    # N : 지도의 크기 N * N
    # K : 최대 공사 가능 깊이
    N, K = map(int, input().split())
    # 각 value : 산의 높이
    in_map = [list(map(int, input().split())) for _ in range(N)]
    # print(N, K, in_map)

    # 가장 높은 산에서 출발
    # 현재 위치보다 더 낮은 산으로만 이동할 수 있다
    # 단, 공사를 해서 산의 높이를 낮췄을 때, 현재 위치보다 더 낮은 산이라면 그 곳으로도 이동할 수 있다
    # 공사는 단 한 군데만 가능하다

    start_points = []   # 시작 지점 좌표들
    start_v = 0   # 시작 지점 산의 높이
    for i in range(N):
        for j in range(N):
            if in_map[i][j] > start_v:
                start_v = in_map[i][j]
                start_points = [[i, j]]
            elif in_map[i][j] == start_v:
                start_points.append([i, j])

    visited = [[0] * N for _ in range(N)]

    max_cnt = 0
    for y, x in start_points:
        visited[y][x] = 1
        f(y, x, K, 1)
        visited[y][x] = 0

    print('#{} {}'.format(tc, max_cnt))