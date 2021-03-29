# 풍선팡
# D2
import sys
sys.stdin = open('input_9490.txt')

def pang_cnt(arr, i, j, pang):
    # 상 하 좌 우  (순서)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = arr[i][j]     # 터지는 꽃가루 카운팅
    # 네방향 탐색
    for dir in direction:
        # 한 방향당 이동할 칸 수
        for c in range(1, pang+1):
            # 배열의 범위 안에서만 움직이도록 제한
            if 0 <= c*dir[0] + i < len(arr) and 0 <= c*dir[1] + j < len(arr[0]):
                cnt += arr[c*dir[0] + i][c*dir[1] + j]  # 터지는 꽃가루 더하기
    return cnt

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    pang = 0
    # 배열의 모든 풍선을 조사
    for i in range(N):
        for j in range(M):
            pang = arr[i][j]    # pang : 상하좌우방향으로 터트릴 수 있는 풍선 수
            cnt = pang_cnt(arr, i, j, pang)
            # 최대값 비교해서 갱신
            if max_cnt < cnt:
                max_cnt = cnt

    print('#{} {}'.format(test_case, max_cnt))
