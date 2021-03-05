# 러시아 깃발 만든기
# D4
import sys
sys.stdin = open('input_4613.txt')

def find_casese():
    if len(tmp) < 3:
        if sum(tmp) >= N: return
    elif len(tmp) == 3:
        if sum(tmp) == N:
            cases.append(tmp.copy())
        return
    for i in range(1, max_row + 1):
        tmp.append(i)
        find_casese()
        tmp.pop()

def change_color(w, b, r):
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

    min_v = None
    for i in range(len(cases)):
        w, b, r = cases[i]
        val = change_color(w, b, r)
        if i == 0: min_v = val
        else:
            if min_v > val:
                min_v = val
    print("#{} {}".format(tc, min_v))