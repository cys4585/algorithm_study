# 러시아 깃발 만들기
# D4
import sys
sys.stdin = open('input_4613.txt')

def find_casese():
    if len(tmp) < 2:
        if sum(tmp) >= N: return
    elif len(tmp) == 2:
        if sum(tmp) < N:
            cases.append(tmp.copy())
        return
    for i in range(1, max_row + 1):
        tmp.append(i)
        find_casese()
        tmp.pop()

def change_color(w, b):
    cnt = 0
    for i in range(N):
        # 하얀 row 만들기
        if i < w:
            for j in range(M):
                if in_arr[i][j] != 'W': cnt += 1
        # 파란 row 만들기
        elif i < w + b:
            for j in range(M):
                if in_arr[i][j] != 'B': cnt += 1
        # 빨간 row 만들기
        else:
            for j in range(M):
                if in_arr[i][j] != 'R': cnt += 1
    return cnt

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    in_arr = [list(map(str, input())) for _ in range(N)]
    # print(N, M, in_arr)

    max_row = N - 2
    tmp = list()
    cases = list()

    find_casese()
    # print(cases)
    max_v = None
    for i in range(len(cases)):
        w, b = cases[i]
        val = change_color(w, b)
        if i == 0: max_v = val
        else:
            if max_v > val:
                max_v = val
    print("#{} {}".format(tc, max_v))