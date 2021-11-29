import sys
sys.stdin = open('./5188_sample_input.txt', 'r')

def my_func(y, x, sum_v):
    global result

    if y == N - 1 and x == N - 1:
        if not result or result > sum_v: result = sum_v
        return

    if result and result < sum_v: return
    
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if ny < N and nx < N:
            my_func(ny, nx, sum_v + board[ny][nx])


direction = ((1, 0), (0, 1))

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = None
    my_func(0, 0, board[0][0])
    print(f'#{tc} {result}')
