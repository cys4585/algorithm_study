import sys
sys.stdin = open('./4839_sample_input.txt', 'r')

def my_func(l, r, goal, cnt):
    c = (l+r) // 2
    if goal == c:
        return cnt
    if l < goal < c:
        return my_func(l, c, goal, cnt + 1)
    elif c < goal < r:
        return my_func(c, r, goal, cnt + 1)

T = int(input())
for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))

    a_cnt = my_func(1, P, A, 1)
    b_cnt = my_func(1, P, B, 1)

    if a_cnt == b_cnt: result = 0
    elif a_cnt < b_cnt: result = 'A'
    else: result = 'B'

    print(f'#{tc} {result}')
