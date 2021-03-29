import sys
sys.stdin = open('exam01.txt')

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우

def f(idx, connected_cnt):
    global result
    global max_connected
    if sum(check) == len(need_connect):
        # print('#'*50)
        # print(check, len(need_connect))
        # for a in in_arr:
        #     print(a)
        # print()
        cnt = 0
        for i in range(N):
            for j in range(N):
                if in_arr[i][j] == 2:
                    cnt += 1
        if connected_cnt > max_connected:
            max_connected = connected_cnt
            result = cnt
        elif connected_cnt == max_connected:
            if cnt > 0 and result > cnt:
                result = cnt
        # print(result, cnt)
        return
    y, x = need_connect[idx]
    check[idx] = 1
    f(idx + 1, connected_cnt)
    check[idx] = 0
    # 4방향 탐색 /
    for dir in direction:
        ny, nx = y, x
        possible = False
        # 한 방향이 벽까지 갈 수 있는지 체크
        while True:
            ny, nx = ny + dir[0], nx + dir[1]
            if in_arr[ny][nx] != 0:
                break
            if ny == 0 or ny == N-1 or nx == 0 or nx == N-1:
                possible = True
                break
        ny, nx = y, x
        # 끝까지 갈 수 있으면 전선 연결
        if possible:
            while True:
                ny, nx = ny + dir[0], nx + dir[1]
                if 0 <= ny < N and 0 <= nx < N:
                    in_arr[ny][nx] = 2
                else:
                    break
            check[idx] = 1
            f(idx+1, connected_cnt+1)
            check[idx] = 0
            while True:
                ny, nx = ny - dir[0], nx - dir[1]
                if y == ny and x == nx:
                    break
                else:
                    in_arr[ny][nx] = 0



for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(tc, N, in_arr)

    need_connect = []
    for r in range(N):
        for c in range(N):
            if r == 0 or r == N-1 or c == 0 or c == N-1: continue
            if in_arr[r][c] == 1: need_connect.append([r, c])
    check = [0] * len(need_connect)
    max_connected = 0
    if tc == 6: pass
    result = 987654321
    f(0, 0)

    print('#{} {}'.format(tc, result))