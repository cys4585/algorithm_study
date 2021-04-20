# 동철이의 일 분배 (D4)

# 동철이가 차린 전자회사에는 N명의 직원이 있다.
# 그런데 어느 날 해야할 일이 N개가 생겼다.
# 동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.

# 직원들의 번호가 1부터 N까지 매겨져 있고,
# 해야할 일에도 번호가 1부터 N까지 매겨져 있을 때,
# i번 직원이 j번 일을 하면 성공할 확률이 Pij이다.

# 여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.
# 직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.
# 우리는 여러 방법 중에서 생길 수 있는 "주어진 일이 모두 성공할 확률"의  최댓값을 구하는 프로그램을 작성해야 한다.

import sys
sys.stdin = open('input_1865.txt')


def my_func(work, percentage):
    global max_per
    # 모든 직원이 일을 다 맡으면 최대값 갱신 후 리턴
    if work == N:
        if max_per < percentage:
            max_per = percentage
        return
    # 확률은 점점 구해갈수록 작아지기 때문에
    # 계산 중간에 최대값보다 작으면 가망이 없는 경우의 수임
    if max_per >= percentage:
        return
    # i : 직원 idx
    for i in range(N):
        # i 직원이 일을 맡고 있는 경우 pass
        if used[i]: continue
        # i 직원이 해당 work를 성공할 확률이 0이면 pass
        if in_arr[i][work] == 0: continue
        used[i] = 1
        my_func(work + 1, percentage * in_arr[i][work] / 100)
        used[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    # 일을 성공할 확률
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    max_per = 0
    used = [0] * N
    my_func(0, 1)

    print(f'#{tc} {max_per * 100:.6f}')
