import sys
sys.stdin = open("input_1210_ladder1.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지 찾기(도착지에서 역으로 출발하기 위해)
    row = -1
    col = 0
    for i in range(len(arr[row])):
        if arr[-1][i] == 2:
            col = i
            break

    # 방향에 따라 칸 이동 (row, col)
    up = (-1, 0)
    left = (0, -1)
    right = (0, 1)

    # 방향 초기 설정
    direction = 'up'

    while True:
        # 위쪽 방향이면
        if direction == 'up':
            row += up[0]
            col += up[1]
            # 왼쪽으로 가는 길이 있으면 (c != 0 -> c == 0 이면 왼쪽 길이 없음)
            if col != 0 and arr[row][col - 1]:
                direction = 'left'
            # 오른쪽으로 가는 길이 있으면 (c != 99 -> c == 99 이면 오른쪽 길이 없음)
            elif col != 99 and arr[row][col + 1]:
                direction = 'right'
            # 도착하면 출력 후 종료
            elif row == -100:
                print('#{} {}'.format(test_case, col))
                break
        # 왼쪽 방향이면
        elif direction == 'left':
            row += left[0]
            col += left[1]
            # 위쪽으로 가는 길이 있으면
            if arr[row - 1][col]:
                direction = 'up'
        # 오른쪽 방향이면
        elif direction == 'right':
            row += right[0]
            col += right[1]
            # 위쪽으로 가는 길이 있으면
            if arr[row - 1][col]:
                direction = 'up'