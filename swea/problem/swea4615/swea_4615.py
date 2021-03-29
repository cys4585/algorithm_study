# 재미있는 오셀로 게임
# D3
import sys
sys.stdin = open('input_4615.txt')
T = int(input())
for test_case in range(1, T+1):
    # N * N 바둑판
    # M : 돌을 놓는 횟수
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(M)]
    # [1, 2, 1] -> 1,2 위치에 흑돌
    # [1, 1, 2] -> 1,1 위치에 백돌
    # [x, y, c]

    # 0열, 0행은 안씀
    board = [[0] * (N+1) for _ in range(N+1)]
    for i in range(len(board)//2, len(board)//2 + 2):
        for j in range(len(board)//2, len(board)//2 + 2):
            if i == j:
                board[i][j] = 2
            else:
                board[i][j] = 1

    # 8방향 (12시부터 시계방향) / (x, y)
    direction = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    for a in arr:
        x, y = a[0], a[1]
        board[y][x] = a[2]
        # 8방향 검사
        for dir in direction:
            dx = dir[0]
            dy = dir[1]
            # 한 방향당 모든 칸 조사 (한 칸씩 이동하면서 그 칸의 숫자를 체크한다.)
            check_arr = []
            qx = x + dx
            qy = y + dy
            while 0 < x + dx < N + 1 and 0 < y + dy < N + 1:
                # 빈칸이면 -> 그쪽 방향은 의미가 없으니 종료
                if board[y+dy][x+dx] == 0:
                    break
                # 빈칸이거나 내 돌과 다른 돌이면 -> 그 돌의 위치를 check_arr에 추가
                elif board[y][x] != board[y+dy][x+dx]:
                    check_arr.append([y+dy, x+dx])
                # 내 돌과 같은 돌을 만나면 -> check_arr에 있던 위치의 돌을 내 돌로 바꾼다. / 그 방향 조사 종료, 다음 방향 조사
                else:
                    for change in check_arr:
                        cy, cx = change[0], change[1]
                        board[cy][cx] = board[y][x]

                    break   # 지금 방향 조사 종료, 다음 방향 조사
                dx += dir[0]
                dy += dir[1]

    # '#test_case 흑돌개수 백돌개수' 출력
    black = 0
    white = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(test_case, black, white))