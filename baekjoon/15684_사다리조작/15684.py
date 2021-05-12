# 사다리 조작
# https://www.acmicpc.net/problem/15684

# 사다리 게임은 N개의 세로선과 M개의 가로선으로 이루어져 있다.
# 인접한 세로선 사이에는 가로선을 놓을 수 있는데,
# 각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H이고,
# 모든 세로선이 같은 위치를 갖는다.

# 입력
# 첫째 줄에 세로선의 개수 N, 가로선의 개수 M,
# 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
# (2 <= N <= 10, 1 <= H <= 30, 0 <= M <= (N-1)*H)

# 둘째 줄부터 M개의 줄에는 가로선의 정보가 한 줄에 하나씩 주어짐
# 가로선의 정보는 두 정수 a와 b로 나타냄
# 1 <= a <= H, 1 <= b <= N-1
# b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미

# 출력
# i번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하기 위해
# 추가해야 하는 가로선 개수의 최솟값
# 정답이 3보다 큰 값이면 -1을 출력,
# 불가능한 경우에도 -1 출력

'''
2 0 3
2 1 3
1 1
5 5 6
1 1
3 2
2 3
5 1
5 4
6 5 6
1 1
3 2
1 3
2 5
5 5
5 8 6
1 1
2 2
3 3
4 4
3 1
4 2
5 3
6 4
5 12 6
1 1
1 3
2 2
2 4
3 1
3 3
4 2
4 4
5 1
5 3
6 2
6 4
5 6 6
1 1
3 1
5 2
4 3
2 3
1 4
'''

# 출발지와 도착지의 세로선 번호가 같으면 return True
# 도착지의 세로선 번호가 다르면 return False
def equal_i(start, y, x, direction):
    # finish
    if matrix[y][x] == 2:
        if start == x:
            return True, x
        return False, x
    # 사다리 갈아타기
    # 오른쪽으로 가기
    if matrix[y][x] == 1 and direction == 'down':
        return equal_i(start, y, x + 1, 'side')
    # 왼쪽으로 가기
    elif 0 <= x-1 and matrix[y][x-1] == 1 and direction == 'down':
        return equal_i(start, y, x - 1, 'side')
    # 내려가기
    else:
        return equal_i(start, y+1, x, 'down')


def my_func(start, cnt):
    global result
    # 3개 이상 가로선 추가해야 하면 실패 -> -1
    if cnt > 3:
        return
    # 모든 세로선 조사 끝나면 종료
    if start == N:
        result = cnt
        return

    # 출발지 == 도착지 이면 -> 다음 출발지 검사
    if equal_i(start, 0, start, 'down')[0]:
        # if matrix[0][2] == 1 and matrix[2][3] == 1:
            # for i in range(H + 1):
            #     print(matrix[i])
            # print(start, cnt, equal_i(start, 0, start, 'down'))
            # print()
        my_func(start + 1, cnt)
    # 출발지 != 도착지 이면 -> 사다리 추가하고 처음부터 다시 검사
    else:
        for i in range(N):
            for j in range(H):
                if matrix[j][i] or (0 <= i-1 and matrix[j][i-1]) or (i+1 < N and matrix[j][i+1]): continue
                # if 0 <= i-1:
                #     matrix[j][i], matrix[j][i - 1] = 1, 1
                #     my_func(start, cnt + 1)
                #     matrix[j][i], matrix[j][i - 1] = 0, 0
                if i+1 < N:
                    matrix[j][i] = 1
                    my_func(0, cnt + 1)
                    matrix[j][i] = 0
                if result != -1:
                    return

for tc in range(1, 8):
    pass
N, M, H = map(int, input().split())
matrix = [[0] * N for _ in range(H)]
matrix += [[2] * N]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

# for i in range(H+1):
#     print(matrix[i])
# print()
result = -1
# for i in range(N):
#     print(equal_i(i, 0, i, 'down'))
my_func(0, 0)
print(result)