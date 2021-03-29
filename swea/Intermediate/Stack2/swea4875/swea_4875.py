# 미로
# D2
import sys
sys.stdin = open('input_4875.txt')
for test_case in range(1, int(input()) + 1):
    N = int(input())    # N * N 크기
    in_arr = [list(map(int, input())) for _ in range(N)]

    im_here = None
    destination = None
    for i in range(N):
        for j in range(N):
            if in_arr[i][j] == 3:
                destination = [i, j]
            elif in_arr[i][j] == 2:
                im_here = [i, j]

    stack = []
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우
    result = 0
    while True:
        # print(im_here, destination)
        if im_here == destination:
            result = 1
            break
        stack.append(im_here)
        y, x = im_here
        # print(im_here, stack)
        for i in range(4):
            # print('for문 실행')
            dy = y + direction[i][0]
            dx = x + direction[i][1]
            if dy < 0 or dy >= N or dx < 0 or dx >= N:
                # print('continue 실행')
                continue
            if in_arr[dy][dx] == 3:
                im_here = [dy, dx]
                break
            if in_arr[dy][dx] == 0 and [dy, dx] not in stack:
                im_here = [dy, dx]
                # print('break 실행')
                break
        else:
            # print('else문 실행')
            in_arr[y][x] = 1
            stack.pop() # 현재위치 stack 에서 삭제
            if not stack:
                break
            im_here = stack.pop()   # 되돌아 갈 좌표 얻기
        # print(in_arr)
        # print(im_here, stack)

    print('#{} {}'.format(test_case, result))